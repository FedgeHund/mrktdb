import os
from django_cron import CronJobBase, Schedule
from edgar.models import FailsToDeliver, Security
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
# file deepcode ignore C0325:


class CusipTickerMappingSecurityUpdate(CronJobBase):
    # we dont run this every minute, we will be using linux crontab to setup
    # when the job will run
    RUN_EVERY_MINS = 0.01

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.cusipTickerMappingSecurityUpdate'    # a unique code

    def do(self):
        print("Cusip Ticker Mapping update started")

        security_items = Security.objects.all()
        failsToDeliver_items = FailsToDeliver.objects.all()

        item_no = 0
        matched_items = 0
        for item in failsToDeliver_items:
            item_no += 1
            print("Item:", item_no)
            for security in security_items:
                if(security.cusip == item.cusip):
                    matched_items += 1
                    print("Matched:", matched_items)
                    security.ticker = item.ticker
                    security.save()
        print("Ticker mapping ended")
