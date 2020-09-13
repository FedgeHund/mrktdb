from django_cron import CronJobBase, Schedule
import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
from edgar.models import CikCusipMapping

class CikCusipCronJob(CronJobBase):
    RUN_EVERY_MINS=1 # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.cik-cusip'    # a unique code

    def do(self):
    	with open('../static/admin/csv_files/CIK_CUSIP.csv', 'rt')as f:
        	data = csv.reader(f)

        	try:
        		Objects = [
        			CikCusipMapping(
        				year = row[0], cik = row[1], sec_name = row[2], cusip = row[3], cusip6 = row[4]
        			)
        			for row in data
        		]
        		print("Starting...")
        		CikCusipMapping.objects.bulk_create(Objects)
        		print("End!")
        	except:
        		print("Failed to store")
