import getopt
import os
import sys

import django
from joblib import Parallel, delayed
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from django.db.models import Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from edgar.models import QuarterlyHolding, QuarterlySecurityHolding, Filer
from holdings.models import Position
from security.models import Price


@transaction.atomic
def bulk_get_or_create(positions_dict_to_create):
    for position_dict in positions_dict_to_create:
        try:
            Position.objects.get_or_create(securityId=position_dict.get("securityId"),
                                           quarterId=position_dict.get("quarterId"),
                                           quarter=position_dict.get("quarter"),
                                           defaults=position_dict)
        except MultipleObjectsReturned:
            print("Multiple objects returned. This is bad, we will need to remove this duplication SecurityId: ",
                  position_dict.get("securityId").securityId, " quarterId: ",
                  position_dict.get("quarterId").quarterlyHoldingId, " quarter: ", position_dict.get("quarter"))


def calculate_positions(filer):
    print("Starting positions calculation for filer: ", filer.filerId)

    quarterly_holdings = QuarterlyHolding.objects.filter(filerId=filer).order_by('quarter')
    prev_total_market_value = 0
    qtrly_sec_holdings_for_prev_qtrly_holding = None
    first_qtrly_holding_by_sec_id = {}

    for quarterly_holding in quarterly_holdings:
        positions_to_create = []
        print("Starting positions calculation for filer: ", filer.filerId, " quarter: ", quarterly_holding.quarter)

        quarterly_security_holdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=quarterly_holding)
        total_market_value = quarterly_security_holdings.aggregate(Sum("marketvalue")).get("marketvalue__sum", 0)
        distinct_securities_in_qtrly_sec_holdings = set()
        # Security.objects.filter(
        #    quarterlysecurityholding__in=quarterly_security_holdings).distinct()

        for quarterly_security_holding in quarterly_security_holdings.select_related("securityId"):
            distinct_securities_in_qtrly_sec_holdings.add(quarterly_security_holding.securityId)

        for security in distinct_securities_in_qtrly_sec_holdings:
            print("Starting positions calculation for filer: ", filer.filerId, " quarter: ", quarterly_holding.quarter,
                  " security: ", security.cusip, "|", security.securityName)

            ##########################################
            # START: Find totals for current quarter #
            ##########################################

            totals_of_sec = quarterly_security_holdings.filter(securityId=security).aggregate(Sum("marketvalue"),
                                                                                              Sum("quantity"))
            total_market_value_of_sec = totals_of_sec.get("marketvalue__sum", 0)
            total_quantity_of_sec = totals_of_sec.get("quantity__sum", 0)

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
                    Sum("marketvalue"), Sum("quantity"))
                prev_total_market_value_of_sec = prev_totals_of_sec.get("marketvalue__sum", 0)
                prev_total_quantity_of_sec = prev_totals_of_sec.get("quantity__sum", 0)

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
                                    change_in_shares / prev_total_quantity_of_sec) * 100  # doubt: what happens when a security is added in this quarter
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
            position_to_create = {"securityId": security, "quarterId": quarterly_holding, "filerId": filer,
                                  "quarter": quarterly_holding.quarter, "securityName": security.securityName,
                                  "filerName": filer.companyId.name, "cusip": security.cusip,
                                  "cik": filer.companyId.cik,
                                  "quarterFirstOwned": first_qtrly_holding_by_sec_id.get(security.securityId),
                                  "quantity": total_quantity_of_sec, "marketValue": total_market_value_of_sec,
                                  "weightPercent": weight_percent_of_sec,
                                  "previousWeightPercent": prev_weight_percent_of_sec, "lastPrice": last_price,
                                  "changeInShares": change_in_shares, "changeInPositionPercent": position_change,
                                  "sourceType": filer.fileType, "sourcedOn": quarterly_holding.filedOn,
                                  "positionType": position_type}

            positions_to_create.append(position_to_create)

            ###############################
            # END: Create position object #
            ###############################

            ####################################
            # START: Store quarter first owned #
            ####################################

            if security.securityId not in first_qtrly_holding_by_sec_id:
                first_qtrly_holding_by_sec_id[security.securityId] = quarterly_holding

            ##################################
            # END: Store quarter first owned #
            ##################################

        #######################################################
        # START: Reassign to current to prev for next quarter #
        #######################################################

        prev_quarterly_holding = quarterly_holding
        qtrly_sec_holdings_for_prev_qtrly_holding = quarterly_security_holdings
        prev_total_market_value = total_market_value

        #####################################################
        # END: Reassign to current to prev for next quarter #
        #####################################################

        #####################
        # START: Bulk write #
        #####################

        print("Bulk writing ", len(positions_to_create), " positions for filer: ", filer.filerId, " quarter: ",
              quarterly_holding.quarter)
        bulk_get_or_create(positions_to_create)

        ###################
        # END: Bulk write #
        ###################


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["numThreads=", ])
    except getopt.GetoptError:
        print('holdings.py -n <numberOfThreads>')
        sys.exit(2)
    n_jobs = 2
    for opt, arg in opts:
        if opt == '-n':
            n_jobs = int(arg)

    filers = Filer.objects.all()
    Parallel(n_jobs=n_jobs, prefer="threads")(delayed(calculate_positions)(filer) for filer in filers)


if __name__ == "__main__":
    main(sys.argv[1:])
