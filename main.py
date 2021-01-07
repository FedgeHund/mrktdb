

"""main.py allows you to start the scraper."""

import datetime
from scraper import HoldingsScraper
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import Company

cik = ''
# Pass the ciks for the companies for which you want 13-F data
# To get the data of 13-F for all the companies we just need to have a list containing ciks of all the companies.
cikmaster=[]

for companyobject in Company.objects.all():
    cikmaster.append(companyobject.cik)


ciks = ["0001067983"]


# To find information about any 1 company uncomment line 14 -15 and comment line 19-20
# while len(cik) < 1:
#     cik = input('Please enter a cik: ')


for cik in ciks:
    if cik not in cikmaster:
        sys.stdout.write('Scraping started at %s\n' % str(datetime.datetime.now()))
        holdings = HoldingsScraper(cik)
        holdings.scrape()
    else:
        print("holdings for",cik,"already present")

try:
    holdings.remove_temp_file()
except:
    pass

sys.stdout.write('Scraping completed at %s\n' % str(datetime.datetime.now()))
