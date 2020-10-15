import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import sys
import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DOMAIN = "https://www.sec.gov"


class Latest13FExtractor:
    def __init__(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)
        self.links = []


    def find_filings(self):
        URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent"
        self.browser.get(URL)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        try:

            wait = WebDriverWait(self.browser, 20)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div")))
            search = self.browser.find_element_by_name('type')
            filing_type = '13F-HR' or '13F-HR/A'
            search.send_keys(filing_type)
            search.send_keys(Keys.RETURN)
            time.sleep(5)
            self.retrieve_filings()

        except:
            sys.stdout.write('No results found \n')


    def retrieve_filings(self):
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        self.links.extend(soup('a', text='[html]'))
        sys.stdout.write('13F filings found: %d\n' % len(self.links))

        try:
            next = self.browser.find_element_by_xpath("//input[@value='Next 40']")
            next.click()
            self.retrieve_filings()
        except:
            for link in self.links:
                url = DOMAIN + link.get('href', None)
                print(url)
                # self.parse_filing(url)
                # Uncomment parse_filing function and copy other functions from previous 13F code as required





    # def parse_filing(self, url):
    #     self.browser.get(url)
    #     soup = BeautifulSoup(self.browser.page_source, "html.parser")
    #
    #     # Find report information for text file headers
    #     filing_date_loc = soup.find("div", text="Filing Date")
    #     filing_date = filing_date_loc.findNext('div').text
    #     period_of_report_loc = soup.find("div", text="Period of Report")
    #     period_of_report = period_of_report_loc.findNext('div').text
    #
    #     # Prepare report header and file_name for each text file
    #     report_detail = self.report_info(filing_date, period_of_report)
    #     file_name = report_detail[0]
    #     report_headers = report_detail[1]
    #
    #     # Determine if xml file exists, if not look for ASCII text file
    #     try:
    #         xml = soup.find('td', text="2")
    #         xml2 = soup.find('td', text="1")
    #
    #         xml_link = xml.findNext('a', text=re.compile("\.xml$"))
    #         xml_link2 = xml2.findNext('a', text=re.compile("\.xml$"))
    #
    #         xml_file = DOMAIN + xml_link.get('href', None)
    #         xml_file2 = DOMAIN + xml_link2.get('href', None)
    #
    #         print(xml_file)
    #         print(xml_file2)
    #
    #         sys.stdout.write('Getting holdings from: %s\n' % xml_file)
    #         holdings = self.infoTable(xml_file)
    #         col_headers = holdings[0]
    #         data = holdings[1]
    #
    #         sys.stdout.write('Getting holdings from: %s\n' % xml_file2)
    #         coverPage = self.primaryDoc(xml_file2)
    #         col_headers2 = coverPage[0]
    #         coverPageData = coverPage[1]
    #         # self.save_holdings_xml(file_name, report_headers, col_headers, data, col_headers2, coverPageData)
    #
    #     except:
    #         pass


    def scrape(self):
        self.find_filings()
        self.browser.quit()










latest_extractor = Latest13FExtractor()
latest_extractor.scrape()
