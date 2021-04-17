import getopt
import os
import sys
import logging
import time

import django

from joblib import Parallel, delayed, wrap_non_picklable_objects
from django.db.models import Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from edgar.models import QuarterlyHolding, QuarterlySecurityHolding
from holdings.models import Position
from security.models import Price

logger = logging.getLogger("holdings_job")


def get_prev_quarter(quarter):
    year = int(quarter[0:4])
    q_num = int(quarter[4])

    prev_q_num = q_num - 1
    if prev_q_num <= 0:
        prev_q_num = 4
        year = year - 1

    return str(year) + str(prev_q_num)

@delayed
@wrap_non_picklable_objects
def calculate_positions(quarterly_holding, number_of_threads=8):
    filer = quarterly_holding.filerId
    logger.info("Starting positions calculation for filer: %0s quarter: %1s", filer.filerId, quarterly_holding.quarter)

    quarterly_security_holdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=quarterly_holding)

    distinct_securities_in_qtrly_sec_holdings = set()
    for quarterly_security_holding in quarterly_security_holdings.select_related("securityId"):
        distinct_securities_in_qtrly_sec_holdings.add(quarterly_security_holding.securityId)

    ####################################################################
    # START: Ignore securities we have already calculated position for #
    ####################################################################

    for position in Position.objects.select_related("securityId", "quarterId").filter(filerId=filer,
                                                                                      quarterId=quarterly_holding,
                                                                                      quarter=quarterly_holding.quarter):
        distinct_securities_in_qtrly_sec_holdings.remove(position.securityId)

    if len(distinct_securities_in_qtrly_sec_holdings) == 0:
        logger.info("All done for filer: %0s quarter: %1s", filer.filerId, quarterly_holding.quarter)
        return

    ##################################################################
    # END: Ignore securities we have already calculated position for #
    ##################################################################

    total_market_value = quarterly_security_holdings.aggregate(Sum("marketvalue")).get("marketvalue__sum", 0)
    if total_market_value is None:
        total_market_value = 0

    #####################################
    # START: Calculate previous quarter #
    #####################################

    prev_quarter = get_prev_quarter(quarterly_holding.quarter)
    prev_quarterly_holding = QuarterlyHolding.objects.get(filerId=filer, quarter=prev_quarter)
    qtrly_sec_holdings_for_prev_qtrly_holding = QuarterlySecurityHolding.objects.filter(
        quarterlyHoldingId=prev_quarterly_holding)
    prev_total_market_value = qtrly_sec_holdings_for_prev_qtrly_holding.aggregate(
        Sum("marketvalue")).get("marketvalue__sum", 0)
    if prev_total_market_value is None:
        prev_total_market_value = 0

    ###################################
    # END: Calculate previous quarter #
    ###################################

    positions_to_create = Parallel(n_jobs=number_of_threads, prefer="threads")(
        calculate_positions_per_sec(filer=filer, security=security, total_market_value=total_market_value,
                                    prev_total_market_value=prev_total_market_value,
                                    quarterly_holding=quarterly_holding,
                                    quarterly_security_holdings=quarterly_security_holdings,
                                    qtrly_sec_holdings_for_prev_qtrly_holding=qtrly_sec_holdings_for_prev_qtrly_holding)
        for security in
        distinct_securities_in_qtrly_sec_holdings)

    #####################
    # START: Bulk write #
    #####################

    logger.info("Bulk writing %0s positions for filer: %1s quarter: %2s", len(positions_to_create), filer.filerId,
                quarterly_holding.quarter)
    Position.objects.bulk_create(positions_to_create)

    ###################
    # END: Bulk write #
    ###################


@delayed
@wrap_non_picklable_objects
def calculate_positions_per_sec(filer, security, total_market_value,
                                prev_total_market_value,
                                quarterly_holding, quarterly_security_holdings,
                                qtrly_sec_holdings_for_prev_qtrly_holding):
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

    return Position(securityId=security, quarterId=quarterly_holding, filerId=filer,
                    quarter=quarterly_holding.quarter, securityName=security.securityName,
                    filerName=filer.companyId.name, cusip=security.cusip,
                    cik=filer.companyId.cik,
                    quarterFirstOwned=None,
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
        print('positions_job.py -n <numberOfThreads>')
        sys.exit(2)
    n_jobs = 2
    filer_start_id = None
    for opt, arg in opts:
        if opt == '-n':
            n_jobs = int(arg)
        if opt == '-f':
            filer_start_id = int(arg)

    quarterly_holdings = QuarterlyHolding.objects.select_related("filerId")
    if filer_start_id is None:
        quarterly_holdings = quarterly_holdings.all()
    else:
        quarterly_holdings = quarterly_holdings.filter(filerId__filerId__gt=filer_start_id)

    start_time = time.time()
    Parallel(n_jobs=n_jobs, backend="multiprocessing")(
        calculate_positions(quarterly_holding=quarterly_holding, number_of_threads=n_jobs) for quarterly_holding in
        quarterly_holdings)
    logger.info("Time taken: %0s", time.time() - start_time)

    # TODO: Update first quarter per security per filer


if __name__ == "__main__":
    main(sys.argv[1:])
