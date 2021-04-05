import getopt
import os
import sys
import logging
import time

import django

from joblib import Parallel, delayed, wrap_non_picklable_objects
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from django.db.models import Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from edgar.models import QuarterlyHolding, QuarterlySecurityHolding, Filer
from holdings.models import Position
from security.models import Price

logger = logging.getLogger("holdings_job")


@transaction.atomic
def bulk_get_or_create(positions_dict_to_create):
    for position_dict in positions_dict_to_create:
        try:
            Position.objects.get_or_create(securityId=position_dict.get("securityId"),
                                           quarterId=position_dict.get("quarterId"),
                                           quarter=position_dict.get("quarter"),
                                           defaults=position_dict)
        except MultipleObjectsReturned:
            logger.exception(
                "Multiple objects returned. "
                "This is bad, we will need to remove this duplication SecurityId: %0s quarterId: %1s quarter: %2s",
                position_dict.get("securityId").securityId,
                position_dict.get("quarterId").quarterlyHoldingId, position_dict.get("quarter"))


def get_prev_quarter(quarter):
    q_num = int(quarter[0])
    year = int(quarter[1:])

    prev_q_num = q_num - 1
    if prev_q_num <= 0:
        prev_q_num = 4
        year = year - 1

    return str(prev_q_num) + str(year)


@delayed
@wrap_non_picklable_objects
def calculate_positions(filer, number_of_threads=8):
    logger.info("Starting positions calculation for filer: %s", filer.filerId)

    quarterly_holdings = QuarterlyHolding.objects.filter(filerId=filer)
    first_qtrly_holding_by_sec_id = {}

    positions = Position.objects.filter(filerId=filer).select_related("securityId", "quarterId")

    for quarterly_holding in quarterly_holdings:
        logger.info("Starting positions calculation for filer: %0s quarter: %1s", filer.filerId,
                    quarterly_holding.quarter)

        quarterly_security_holdings = QuarterlySecurityHolding.objects.select_related("quarterlyHoldingId").filter(
            quarterlyHoldingId=quarterly_holding)
        total_market_value = quarterly_security_holdings.aggregate(Sum("marketvalue")).get("marketvalue__sum", 0)
        if total_market_value is None:
            total_market_value = 0
        distinct_securities_in_qtrly_sec_holdings = set()
        # Security.objects.filter(
        #    quarterlysecurityholding__in=quarterly_security_holdings).distinct()

        for quarterly_security_holding in quarterly_security_holdings.select_related("securityId"):
            distinct_securities_in_qtrly_sec_holdings.add(quarterly_security_holding.securityId)

        ####################################################################
        # START: Ignore securities we have already calculated position for #
        ####################################################################

        for position in positions.filter(quarterId=quarterly_holding, quarter=quarterly_holding.quarter):
            distinct_securities_in_qtrly_sec_holdings.remove(position.securityId)

        if len(distinct_securities_in_qtrly_sec_holdings) == 0:
            logger.info("All done for filer: %0s quarter: %1s", filer.filerId, quarterly_holding.quarter)
            continue

        ##################################################################
        # END: Ignore securities we have already calculated position for #
        ##################################################################

        #####################################
        # START: Calculate previous quarter #
        #####################################

        qtrly_sec_holdings_for_prev_qtrly_holding = quarterly_security_holdings.filter(
            quarterlyHoldingId__quarter=get_prev_quarter(quarterly_holding.quarter))
        prev_total_market_value = qtrly_sec_holdings_for_prev_qtrly_holding.aggregate(
            Sum("marketvalue")).get("marketvalue__sum", 0)
        if prev_total_market_value is None:
            prev_total_market_value = 0

        ###################################
        # END: Calculate previous quarter #
        ###################################

        for security in distinct_securities_in_qtrly_sec_holdings:
            ####################################
            # START: Store quarter first owned #
            ####################################

            if security.securityId not in first_qtrly_holding_by_sec_id:
                first_qtrly_holding_by_sec_id[security.securityId] = quarterly_holding

            ##################################
            # END: Store quarter first owned #
            ##################################

        positions_to_create = Parallel(n_jobs=number_of_threads, prefer="threads")(
            calculate_positions_per_sec(filer=filer, security=security, total_market_value=total_market_value,
                                        prev_total_market_value=prev_total_market_value,
                                        quarterly_holding=quarterly_holding,
                                        quarterly_security_holdings=quarterly_security_holdings,
                                        qtrly_sec_holdings_for_prev_qtrly_holding=qtrly_sec_holdings_for_prev_qtrly_holding,
                                        first_qtrly_holding_by_sec_id=first_qtrly_holding_by_sec_id) for security in
            distinct_securities_in_qtrly_sec_holdings)

        #####################
        # START: Bulk write #
        #####################

        logger.info("Bulk writing %0s positions for filer: %1s quarter: %2s", len(positions_to_create), filer.filerId,
                    quarterly_holding.quarter)
        Position.objects.bulk_create(positions_to_create)
        # bulk_get_or_create(positions_to_create)

        ###################
        # END: Bulk write #
        ###################


@delayed
@wrap_non_picklable_objects
def calculate_positions_per_sec(filer, security, total_market_value,
                                prev_total_market_value,
                                quarterly_holding, quarterly_security_holdings,
                                qtrly_sec_holdings_for_prev_qtrly_holding, first_qtrly_holding_by_sec_id):
    logger.info("Starting positions calculation for filer: %0s quarter: %1s security: %2s|%3s ", filer.filerId,
                quarterly_holding.quarter, security.securityName, security.cusip)

    ##########################################
    # START: Find totals for current quarter #
    ##########################################

    totals_of_sec = quarterly_security_holdings.filter(securityId=security).aggregate(
        totalMarketValue=Sum("marketvalue"), totalQuantity=Sum("quantity"))
    total_market_value_of_sec = totals_of_sec.get("totalMarketValue", 0)
    if total_market_value_of_sec is None:
        total_market_value_of_sec = 0
    total_quantity_of_sec = totals_of_sec.get("totalQuantity", 0)
    if total_quantity_of_sec is None:
        total_quantity_of_sec = 0

    weight_percent_of_sec = None
    if total_market_value != 0:
        weight_percent_of_sec = (total_market_value_of_sec * 100) / total_market_value

    ########################################
    # END: Find totals for current quarter #
    ########################################

    ###########################################
    # START: Find totals for previous quarter #
    ###########################################

    prev_total_market_value_of_sec = 0
    prev_total_quantity_of_sec = 0

    if qtrly_sec_holdings_for_prev_qtrly_holding is not None:
        prev_totals_of_sec = qtrly_sec_holdings_for_prev_qtrly_holding.filter(securityId=security).aggregate(
            totalMarketValue=Sum("marketvalue"),
            totalQuantity=Sum("quantity"))
        prev_total_market_value_of_sec = prev_totals_of_sec.get("totalMarketValue", 0)
        if prev_total_market_value_of_sec is None:
            prev_total_market_value_of_sec = 0
        prev_total_quantity_of_sec = prev_totals_of_sec.get("totalQuantity", 0)
        if prev_total_quantity_of_sec is None:
            prev_total_quantity_of_sec = 0

    prev_weight_percent_of_sec = None
    if prev_total_market_value != 0:
        prev_weight_percent_of_sec = (prev_total_market_value_of_sec * 100) / prev_total_market_value

    #########################################
    # END: Find totals for previous quarter #
    #########################################

    #########################################
    # START: Compare current vs prev totals #
    #########################################

    change_in_shares = total_quantity_of_sec - prev_total_quantity_of_sec
    position_change = None
    position_type = 'New'
    if prev_total_quantity_of_sec != 0:
        position_change = (
                            change_in_shares / prev_total_quantity_of_sec) * 100
        # doubt: what happens when a security is added in this quarter
        if prev_total_quantity_of_sec > total_quantity_of_sec:
            position_type = 'Decreased'
        elif prev_total_quantity_of_sec < total_quantity_of_sec:
            position_type = 'Increased'
        elif prev_total_quantity_of_sec == total_quantity_of_sec:
            position_type = 'No Change'

    #######################################
    # END: Compare current vs prev totals #
    #######################################

    #########################
    # START: Get last price #
    #########################

    price = Price.objects.filter(securityId=security, quarter=quarterly_holding.quarter).first()
    last_price = None
    if price is not None:
        last_price = price.value

    #######################
    # END: Get last price #
    #######################

    #################################
    # START: Create position object #
    #################################

    ## Need to think about investmentDiscretion. Different rows in quaterly holding for same security can have the different investmentDiscretion
    # position_to_create = {"securityId": security, "quarterId": quarterly_holding, "filerId": filer,
    #                      "quarter": quarterly_holding.quarter, "securityName": security.securityName,
    #                      "filerName": filer.companyId.name, "cusip": security.cusip,
    #                      "cik": filer.companyId.cik,
    #                      "quarterFirstOwned": first_qtrly_holding_by_sec_id.get(security.securityId),
    #                      "quantity": total_quantity_of_sec, "marketValue": total_market_value_of_sec,
    #                      "weightPercent": weight_percent_of_sec,
    #                      "previousWeightPercent": prev_weight_percent_of_sec, "lastPrice": last_price,
    #                      "changeInShares": change_in_shares, "changeInPositionPercent": position_change,
    #                      "sourceType": filer.fileType, "sourcedOn": quarterly_holding.filedOn,
    #                      "positionType": position_type}
    # return position_to_create
    return Position(securityId=security, quarterId=quarterly_holding, filerId=filer,
                    quarter=quarterly_holding.quarter, securityName=security.securityName,
                    filerName=filer.companyId.name, cusip=security.cusip,
                    cik=filer.companyId.cik,
                    quarterFirstOwned=first_qtrly_holding_by_sec_id.get(security.securityId),
                    quantity=total_quantity_of_sec, marketValue=total_market_value_of_sec,
                    weightPercent=weight_percent_of_sec,
                    previousWeightPercent=prev_weight_percent_of_sec, lastPrice=last_price,
                    changeInShares=change_in_shares, changeInPositionPercent=position_change,
                    sourceType=filer.fileType, sourcedOn=quarterly_holding.filedOn,
                    positionType=position_type)

    ###############################
    # END: Create position object #
    ###############################


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:f:", ["numThreads=", "filerStartId="])
    except getopt.GetoptError:
        print('holdings.py -n <numberOfThreads>')
        sys.exit(2)
    n_jobs = 2
    filer_start_id = 0
    for opt, arg in opts:
        if opt == '-n':
            n_jobs = int(arg)
        if opt == '-f':
            filer_start_id = int(arg)

    filers = Filer.objects.filter(filerId__gt=filer_start_id).prefetch_related("companyId")
    start_time = time.time()
    Parallel(n_jobs=n_jobs, backend="multiprocessing")(
        calculate_positions(filer=filer, number_of_threads=n_jobs) for filer in filers)
    logger.info("Time taken: %0s", time.time() - start_time)


if __name__ == "__main__":
    main(sys.argv[1:])
