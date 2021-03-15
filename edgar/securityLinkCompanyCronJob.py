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
        cikCusipMapping_items = CikCusipMapping.objects.order_by('year').all()

        mapping_no = 0
        found_items = 0
        for mapping in cikCusipMapping_items:
            print("Mapping:", mapping_no)
            for security in security_items:
                if(security.cusip == mapping.cusip or security.cusip == mapping.cusip6):
                    for company in company_items:
                        if int(company.cik) == mapping.cik:
                            found_items += 1
                            print("Found:", found_items)
                            security.companyId = company.companyId
                            security.cikCusipMappingId = mapping.cikCusipMappingId
                            security.save()
            mapping_no += 1
        print("Linking ended")
