from django_cron import CronJobBase, Schedule
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
from edgar.models import CikCusipMapping, Security, Company

class SecurityLinkCompanyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # we dont run this every minute, we will be using linux crontab to setup when the job will run

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'edgar.securityLinkCompanyCronJob'    # a unique code

    def do(self):
        security_items = Security.objects.all()
        company_items = Company.objects.all()
        cikCusipMapping_items = CikCusipMapping.objects.order_by('year').all()

        for mapping in cikCusipMapping_items:
            for security in security_items:
                if(security.cusip == mapping.cusip or security.cusip == mapping.cusip6):
                    for company in company_items:
                        if(company.cik == mapping.cik):
                            security.companyId = company.companyId
                            security.cikCusipMappingId = mapping.cikCusipMappingId
                            security.save()