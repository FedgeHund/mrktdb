from django_cron import CronJobBase, Schedule
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
from edgar.models import CikCusipMapping, Security, Company
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['market-db-local']
cikcusipmapping_collection = db['edgar_cikcusipmapping']
cikCusipMapping_items = list(cikcusipmapping_collection.find())

class SecurityLinkCompanyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # we dont run this every minute, we will be using linux crontab to setup when the job will run

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.securityLinkCompanyCronJob'    # a unique code

    def do(self):
        security_items = Security.objects.all()
        company_items = Company.objects.all()

        for security in security_items:
            for mapping in cikCusipMapping_items:
                if(security.cusip == mapping.get('cusip')):
                    for company in company_items:
                        if(company.cik == mapping.get('cik')):
                            security.companyId = company.companyId
                            security.cikCusipMappingId = mapping.get('_id')
                            security.save()