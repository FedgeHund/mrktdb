import getopt
import os
import sys
import django
import logging

from joblib import Parallel, delayed, wrap_non_picklable_objects

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from django.db.models import Sum
from django.db import transaction
from edgar.models import QuarterlySecurityHolding, Security
from security.models import Price

logger = logging.getLogger("positions_job")


@transaction.atomic
def bulk_get_or_create(prices_dict_to_create):
    for price_dict in prices_dict_to_create:
        Price.objects.get_or_create(securityId=price_dict.get('securityId'), value=price_dict.get('value'),
                                    quarter=price_dict.get('quarter'), cusip=price_dict.get('cusip'),
                                    name=price_dict.get('name'))


@delayed
@wrap_non_picklable_objects
def calculate_price(security):
    logger.info("Starting price calculation for security: %1s|%2s ", security.securityName, security.cusip)
    totals_per_quarter = QuarterlySecurityHolding.objects.filter(securityId=security).values(
        'quarterlyHoldingId__quarter').annotate(
        total_market_value=Sum('marketvalue'), total_quantity=Sum('quantity'))

    prices = []
    for total_per_quarter in totals_per_quarter:
        quarter = total_per_quarter.get('quarterlyHoldingId__quarter')
        if quarter is None:
            continue

        total_value = total_per_quarter.get('total_market_value', 0)
        if total_value is None or total_value == 0:
            continue

        total_quantity = total_per_quarter.get('total_quantity', 0)
        if total_quantity is None or total_quantity == 0:
            continue
        price = {'securityId': security, 'value': total_value / total_quantity, 'quarter': quarter,
                 'cusip': security.cusip, 'name': security.securityName}

        prices.append(price)
    bulk_get_or_create(prices)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["numThreads="])
    except getopt.GetoptError:
        print('positions_job.py -n <numberOfThreads>')
        sys.exit(2)
    n_jobs = 2
    for opt, arg in opts:
        if opt == '-n':
            n_jobs = int(arg)

    securities = Security.objects.all()
    Parallel(n_jobs=n_jobs, backend="multiprocessing")(calculate_price(security=security) for security in securities)


if __name__ == "__main__":
    main(sys.argv[1:])
