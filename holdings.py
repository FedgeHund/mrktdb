import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from edgar.models import QuarterlyHolding, QuarterlySecurityHolding, Filer
from holdings.models import Position
from security.models import Price

quarterly_holdings = quarterly_security_holdings = []
filers = Filer.objects.all()

for filer in filers:
    quarterly_holdings = QuarterlyHolding.objects.filter(filerId=filer).order_by('filedOn')
    positions_to_create = []
    prev_quarterly_holding = None
    qtrly_sec_holdings_for_prev_qtrly_holding = []

    # Add logic to figure out which was the first quarter the security was owned
    first_qtrly_holding_by_sec_id = {}

    for quarterly_holding in quarterly_holdings:
        quarterly_security_holdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=quarterly_holding)

        prev_total_market_value = 0
        for qtrly_sec_holding_for_prev_qtrly_holding in qtrly_sec_holdings_for_prev_qtrly_holding:
            prev_total_market_value = qtrly_sec_holding_for_prev_qtrly_holding.marketvalue + prev_total_market_value

        total_market_value = 0
        for quarterly_security_holding in quarterly_security_holdings:
            total_market_value = quarterly_security_holding.marketvalue + total_market_value

        distinct_security_ids_for_qtrly_holdings = []  # find unique security per quarter holding
        for security in distinct_security_ids_for_qtrly_holdings:

            ##########################################
            # START: Find totals for current quarter #
            ##########################################
            total_market_value_of_sec = 0
            total_quantity_of_sec = 0
            total_sole_of_sec = 0
            total_shared_of_sec = 0
            total_none_of_sec = 0
            qtrly_sec_holdings_for_sec_and_qtrly_holding = quarterly_security_holdings.filter(securityId=security)
            for qtrly_sec_holding_for_sec_and_qtrly_holding in qtrly_sec_holdings_for_sec_and_qtrly_holding:
                total_market_value_of_sec = total_market_value_of_sec + qtrly_sec_holding_for_sec_and_qtrly_holding.marketvalue
                total_quantity_of_sec = total_quantity_of_sec + qtrly_sec_holding_for_sec_and_qtrly_holding.quantity
                total_sole_of_sec = total_sole_of_sec + qtrly_sec_holding_for_sec_and_qtrly_holding.sole
                total_shared_of_sec = total_shared_of_sec + qtrly_sec_holding_for_sec_and_qtrly_holding.shared
                total_none_of_sec = total_none_of_sec + qtrly_sec_holding_for_sec_and_qtrly_holding.none

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
            prev_total_sole_of_sec = 0
            prev_total_shared_of_sec = 0
            prev_total_none_of_sec = 0

            qtrly_sec_holdings_for_sec_and_prev_qtrly_holding = []
            if not qtrly_sec_holdings_for_prev_qtrly_holding:
                qtrly_sec_holdings_for_sec_and_prev_qtrly_holding = qtrly_sec_holdings_for_prev_qtrly_holding.filter(
                    securityId=security)
                for qtrly_sec_holding_for_sec_and_prev_qtrly_holding in qtrly_sec_holdings_for_sec_and_prev_qtrly_holding:
                    prev_total_market_value_of_sec = prev_total_market_value_of_sec + qtrly_sec_holding_for_sec_and_prev_qtrly_holding.marketvalue
                    prev_total_quantity_of_sec = prev_total_quantity_of_sec + qtrly_sec_holding_for_sec_and_prev_qtrly_holding.quantity
                    prev_total_sole_of_sec = prev_total_sole_of_sec + qtrly_sec_holding_for_sec_and_prev_qtrly_holding.sole
                    prev_total_shared_of_sec = prev_total_shared_of_sec + qtrly_sec_holding_for_sec_and_prev_qtrly_holding.shared
                    prev_total_none_of_sec = prev_total_none_of_sec + qtrly_sec_holding_for_sec_and_prev_qtrly_holding.none

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

            price = Price.objects.filter(securityId=security.securityId, quarter=quarterly_holding.quarter).first()
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

            position_to_create = Position(securityId=security, quarterId=quarterly_holding, filerId=filer,
                                          quarter=quarterly_holding.quarter, securityName=security.securityName,
                                          filerName=filer.companyId.name, cusip=security.cusip, cik=filer.companyId.cik,
                                          quarterFirstOwned=first_qtrly_holding_by_sec_id.get(security.securityId),
                                          quantity=total_quantity_of_sec, marketValue=total_market_value_of_sec,
                                          weightPercent=weight_percent_of_sec,
                                          previousWeightPercent=prev_weight_percent_of_sec, lastPrice=last_price,
                                          changeInShares=change_in_shares, changeInPositionPercent=position_change,
                                          sourceType=filer.fileType, sourcedOn=quarterly_holding.filedOn,
                                          positionType=position_type)
            positions_to_create.append(position_to_create)

            ###############################
            # END: Create position object #
            ###############################

        #######################################################
        # START: Reassign to current to prev for next quarter #
        #######################################################

        prev_quarterly_holding = quarterly_holding
        qtrly_sec_holdings_for_prev_qtrly_holding = quarterly_security_holdings

        #####################################################
        # END: Reassign to current to prev for next quarter #
        #####################################################

    Position.objects.bulk_create(positions_to_create)
