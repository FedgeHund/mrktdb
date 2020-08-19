#!/usr/bin/env python3

"""main.py allows you to start the scraper."""

import datetime
from scraper import HoldingsScraper
import sys

ticker = ''
# Pass the ciks for the companies for which you want 13-F data
# To get the data of 13-F for all the companies we just need to have a list containing ciks of all the companies.
ciks = ["0001350694"]


# To find information about any 1 company uncomment line 14 -15 and comment line 19-20
# while len(ticker) < 1:
#     ticker = input('Please enter a ticker: ')


for cik in ciks:
    ticker = cik
    sys.stdout.write('Scraping started at %s\n' % str(datetime.datetime.now()))
    holdings = HoldingsScraper(ticker)
    holdings.scrape()

try:
    holdings.remove_temp_file()
except:
    pass

sys.stdout.write('Scraping completed at %s\n' % str(datetime.datetime.now()))
