import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

from scraper import HoldingsScraper
from edgar.models import Company, Filer, QuarterlyHolding, Security, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager

ticker = ''
# Pass the ciks for the companies for which you want 13-F data
# To get the data of 13-F for all the companies we just need to have a list containing ciks of all the companies.
cikmaster=[]

for companyobject in Company.objects.all():
    cikmaster.append(companyobject.cik)

ciks = ["0001637460"]
# ciks = ["0001037389", "0001637460", "0001364742", "0001067983", "0001167483", "0001350694", "0001179392", "0001273087", "0001048445", "0001423053"]


# To find information about any 1 company uncomment line 14 -15 and comment line 19-20
# while len(ticker) < 1:
#     ticker = input('Please enter a ticker: ')


for cik in ciks:
    if cik not in cikmaster:
        print("Currently running for CIK:", str(cik))
        ticker = cik
        sys.stdout.write('Scraping started at %s\n' % str(datetime.datetime.now()))
        holdings = HoldingsScraper(ticker)
        holdings.scrape()
    else:
        print("Holdings for",cik,"already present")

try:
    holdings.remove_temp_file()
except:
    pass

sys.stdout.write('Scraping completed at %s\n' % str(datetime.datetime.now()))
