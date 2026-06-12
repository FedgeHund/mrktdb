import getopt
import logging
import os
import sys
import django
import positions_job
from joblib import Parallel, wrap_non_picklable_objects, delayed

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from holdings.models import Position
from filer.models import QuarterlyFilerView
from edgar.models import QuarterlyHolding, Company

logger = logging.getLogger("console_logger")


@delayed
@wrap_non_picklable_objects
def calculate_quarterly_filer_view(quarterly_holding):
    logger.info("Calculate quarterly filer view [Quarter: %1s | FilerId: %2s]", quarterly_holding.quarter,
                quarterly_holding.filerId.filerId)
    positions = Position.objects.filter(quarterId=quarterly_holding)
    if len(positions) <= 0:
        return

    filer = quarterly_holding.filerId
    company = Company.objects.filter(companyId=filer.companyId_id).first()

    previous_quarterly_holdings = QuarterlyHolding.objects.filter(
        quarter=positions_job.get_prev_quarter(quarterly_holding.quarter))

    previous_market_value = 0
    previous_entry_count = 0
    for previous_quarterly_holding in previous_quarterly_holdings:
        previous_market_value = previous_market_value + previous_quarterly_holding.totalValue
        previous_entry_count = previous_entry_count + previous_quarterly_holding.totalEntry

    description = '{} is a {} located out of {}. Their latest 13F filings show that they have at least {} AUM.'.format(
        company.name, company.companyType, company.address, quarterly_holding.totalValue)

    decreased_holdings_count = 0
    sold_out_holdings_count = 0
    increased_holdings_count = 0
    new_holdings_count = 0
    total_market_value = 0
    top10_positions_by_market_value = positions.order_by('-marketValue')[:10]
    for position in positions:
        if position.positionType == 'Decreased' and position.quantity > 0:
            decreased_holdings_count = decreased_holdings_count + 1
        if position.positionType == 'Decreased' and position.quantity == 0:
            sold_out_holdings_count = sold_out_holdings_count + 1
        if position.positionType == 'Increased':
            increased_holdings_count = increased_holdings_count + 1
        if position.positionType == 'New':
            new_holdings_count = new_holdings_count + 1
        total_market_value = total_market_value + position.marketValue

    top10_holdings_market_value = 0
    for position in top10_positions_by_market_value:
        top10_holdings_market_value = top10_holdings_market_value + position.marketValue

    if total_market_value is None or total_market_value <= 0:
        return
    top10_holdings_percent = (top10_holdings_market_value / total_market_value) * 100

    QuarterlyFilerView.objects.get_or_create(quarter=quarterly_holding.quarter,
                                             filerId=filer,
                                             cik=company.cik,
                                             defaults={"filerName": company.name, "filerType": company.companyType,
                                                       "marketValue": quarterly_holding.totalValue,
                                                       "previousMarketValue": previous_market_value,
                                                       "previousHoldingsCount": previous_entry_count,
                                                       "soldOutHoldingsCount": sold_out_holdings_count,
                                                       "increasedHoldingsCount": increased_holdings_count,
                                                       "newHoldingsCount": new_holdings_count,
                                                       "decreasedHoldingsCount": decreased_holdings_count,
                                                       "top10HoldingsPercent": top10_holdings_percent,
                                                       "filerDescription": description})


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["numThreads="])
    except getopt.GetoptError:
        print('quarterly_filer_view_job.py -n <numberOfThreads>')
        sys.exit(2)
    n_jobs = 2
    for opt, arg in opts:
        if opt == '-n':
            n_jobs = int(arg)

    quarterly_holdings = QuarterlyHolding.objects.select_related("filerId").all()
    Parallel(n_jobs=n_jobs, backend="multiprocessing")(
        calculate_quarterly_filer_view(quarterly_holding=quarterly_holding) for quarterly_holding in quarterly_holdings)


if __name__ == "__main__":
    main(sys.argv[1:])
