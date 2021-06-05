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

# ciks = ["0001364742"] # Blackrock
# ciks = ["0001067983"] # Berkshire
ciks = ["0001037389", "0001637460", "0001167483", "0001350694", "0001179392", "0001273087", "0001048445", "0001423053", "0001167557", "0001535943", "0001218710", "0001380393", "0001259313", "0001603466", "0001525907", "0000860662", "0001535630", "0001103804", "0001288136", "0000949509", "0001426486", "0001534949", "0001595082", "0001448574", "0001315421", "0000909661", "0001218199", "0001135730", "0001352851", "0000872573", "0001484836", "0001279913", "0001040273", "0001074034", "0001543160", "0001480532", "0001425040"]


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
