import os
from django_cron import CronJobBase, Schedule
from edgar.models import CikCusipMapping, Security, Company
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
# file deepcode ignore C0325:

class SecurityLinkCompanyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0.01 # we dont run this every minute, we will be using linux crontab to setup when the job will run

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.securityLinkCompanyCronJob'    # a unique code

    def do(self):
        print("Linking started")

        security_items = Security.objects.all()
        company_items = Company.objects.all()
        cikCusipMapping_items = CikCusipMapping.objects.all()

        for mapping in cikCusipMapping_items:
            for security in security_items:
                if(mapping.cusip == security.cusip):
                    for company in company_items:
                        if company.cik == mapping.cik:
                            security.companyId_id = company.companyId
                            security.cikCusipMappingId = mapping.cikCusipMappingId
                            security.save() 
        print("Linking ended")
