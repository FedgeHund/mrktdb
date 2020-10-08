from django_cron import CronJobBase, Schedule
import csv
import time
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
from edgar.models import CikCusipMapping

class CikCusipCronJob(CronJobBase):
    RUN_EVERY_MINS = 0.01 # we dont run this every minute, we will be using linux crontab to setup when the job will run

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.cikCusipCronJob'    # a unique code

    def do(self):
        with open('../static/admin/csv_files/CIK_CUSIP.csv', 'rt')as f:
            data = csv.reader(f)

            Objects = [
                CikCusipMapping(
                    year = row[0], cik = row[1], sec_name = row[2], cusip = row[3], cusip6 = row[4], cikCusipMappingId = row[1]+row[3]+row[0]+str(round(time.time()*10000000))
                )
                for row in data
            ]
            CikCusipMapping.objects.bulk_create(Objects, batch_size = 1000)