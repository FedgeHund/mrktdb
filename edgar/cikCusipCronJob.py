from edgar.models import CikCusipMapping
import os
import csv
# file deepcode ignore C0412
from django_cron import CronJobBase, Schedule
import time
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')


class CikCusipCronJob(CronJobBase):
    # we dont run this every minute, we will be using linux crontab to setup
    # when the job will run
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.cikCusipCronJob'    # a unique code

    def do(self):
        print("Start")
        with open('../static/admin/csv_files/final_cik_cusip_mapping.csv', 'rt')as f:
            data = csv.reader(f)

            Objects = [
                CikCusipMapping(
                    cik=row[0], cusip=row[1], cikCusipMappingId=row[0] + row[1] + str(round(time.time() * 10000000))
                )
                for row in data
            ]
            CikCusipMapping.objects.bulk_create(Objects, batch_size=1000)
        print("End")
