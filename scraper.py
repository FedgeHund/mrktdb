#!/usr/bin/env python3

"""
scraper.py contains the main functionality to find and scrape
holdings data from 13F filings on https://www.sec.gov.

See comments in README.md for instructions on how to run
the scraper.

Note, the scraper will find all filings for a ticker and
generated a text file for each in the current directory.
"""
from csv import writer
from csv import DictWriter
import csv
import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import Company, Filer, QuarterlyHolding, Security, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager
import re
import sys
import time
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SEC_LINK = "https://www.sec.gov/edgar/searchedgar/companysearch.html"
CIK_SEARCH_URL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK="
DOMAIN = "https://www.sec.gov"
data1=[]

class HoldingsScraper:
    """Find holdings data in funds by scraping data from the SEC."""

    def __init__(self, ticker):
        # Using Chrome Driver
        # self.browser = webdriver.Chrome(executable_path='C:\\chromedriver_win32\\Chromedriver')

        # Using Firefox Driver
        # caps = DesiredCapabilities.FIREFOX.copy()
        # caps['marionette'] = False
        # self.browser = webdriver.Firefox(capabilities=caps,executable_path=r'C:\\geckodriver-v0.26.0-win64\\geckodriver.exe')

        # Using PhantomJS driver
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)
        self.ticker = ticker
        self.links = []

    def find_filings(self):
        """Open SEC page, feed HTML into BeautifulSoup, and find filings."""
        url = CIK_SEARCH_URL + self.ticker
        self.browser.get(url)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        wait = WebDriverWait(self.browser, 20)

        try:
            wait = WebDriverWait(self.browser, 20)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tableFile2")))

            # Filter search results by '13F-HR' filings
            search = self.browser.find_element_by_name('type')
            filing_type = '13F-HR' or '13F-HR/A'
            search.send_keys(filing_type)
            search.send_keys(Keys.RETURN)
            time.sleep(5)
            self.retrieve_filings()
        except:
            sys.stdout.write('No results found for ticker: %s\n' % self.ticker)

    def retrieve_filings(self):
        """Retrieve links for all 13F filing from search results."""
        sys.stdout.write('Retrieving filings for: %s\n' % self.ticker)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        self.links.extend(soup('a', id='documentsbutton'))
        sys.stdout.write('13F filings found: %d\n' % len(self.links))

        # Comment out try/except lines below to run most recent filing only
        # Checks for more results and click next page
        try:
            next = self.browser.find_element_by_xpath("//input[@value='Next 40']")
            next.click()
            self.retrieve_filings()
        except:
            # Otherwise loop through all filings found to get data
            for link in self.links:
                url = DOMAIN + link.get('href', None)
                self.parse_filing(url)
        # Uncomment below to run most recent filing only
        # url = DOMAIN + self.links[0].get('href', None)
        # self.parse_filing(url)

    def parse_filing(self, url):
        """Examines filing to determine how to parse holdings data.

        Opens filing url, get filing and report end dates, and determine
        parsing by either XML or ASCII based on 2013 filing format change.
        """
        self.browser.get(url)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")

        # Find report information for text file headers
        filing_date_loc = soup.find("div", text="Filing Date")
        filing_date = filing_date_loc.findNext('div').text
        period_of_report_loc = soup.find("div", text="Period of Report")
        period_of_report = period_of_report_loc.findNext('div').text

        # Prepare report header and file_name for each text file
        report_detail = self.report_info(filing_date, period_of_report)
        file_name = report_detail[0]
        report_headers = report_detail[1]

        # Determine if xml file exists, if not look for ASCII text file
        try:
            xml = soup.find('td', text="2")
            xml2 = soup.find('td', text="1")

            xml_link = xml.findNext('a', text=re.compile("\.xml$"))
            xml_link2 = xml2.findNext('a', text=re.compile("\.xml$"))

            xml_file = DOMAIN + xml_link.get('href', None)
            xml_file2 = DOMAIN + xml_link2.get('href', None)

            print(xml_file)
            print(xml_file2)

            sys.stdout.write('Getting holdings from: %s\n' % xml_file)
            holdings = self.get_holdings_xml(xml_file)
            col_headers = holdings[0]
            data = holdings[1]

            sys.stdout.write('Getting holdings from: %s\n' % xml_file2)
            holdings2 = self.get_holdings_xml2(xml_file2)
            col_headers2 = holdings2[0]
            data2 = holdings2[1]
            # self.save_holdings_xml(file_name, report_headers, col_headers, data, col_headers2, data2)



        except:
            pass
            # ascii = soup.find('td', text="Complete submission text file")
            # ascii_link = ascii.findNext('a', text=re.compile("\.txt$"))
            # txt_file = DOMAIN + ascii_link.get('href', None)
            # sys.stdout.write('Getting holdings from (ascii): %s\n' % txt_file)
            # holdings = self.get_holdings_ascii(txt_file)
            # self.save_holdings_ascii(file_name, report_headers, holdings)

    def report_info(self, date, period):
        """Prep report headers to be written to text file. """
        file_name = self.ticker + '_' + str(date) + '_filing_date.csv'
        headers = []

        # # To get the ticker, filing date and period of report in dictionary form, uncomment the below 5 lines
        # header_report = {}
        # header_report['Ticker'] = self.ticker
        # header_report['Filing_Date'] = str(date)
        # header_report['Period_Of_Report'] = str(period)
        # headers.append(header_report)

        # headers.append('Ticker: ' + self.ticker)
        # headers.append('Filing Date: ' + str(date))
        # headers.append('Period of Report: ' + str(period))

        headers.append(self.ticker)
        headers.append(str(date))
        headers.append(str(period))

        # col_report = list(header_report.keys())
        return(file_name, headers)

    def get_holdings_xml(self, xml_file):
        """Get holdings detail from xml file and store data.

        XML format for filings was required by SEC in 2013.
        """
        self.browser.get(xml_file)
        soup = BeautifulSoup(self.browser.page_source, "xml")
        holdings = soup.find_all('infoTable')
        data = []

        # Attempt retrieval of available attributes for 13F filings
        for i in range(len(holdings)):
            d = {}
            try:
                d['nameOfIssuer'] = holdings[i].find('nameOfIssuer').text
            except:
                pass
            try:
                d['titleOfClass'] = holdings[i].find('titleOfClass').text
            except:
                pass
            try:
                d['cusip'] = holdings[i].find('cusip').text
            except:
                pass
            try:
                d['value'] = holdings[i].find('value').text
            except:
                pass
            try:
                d['sshPrnamt'] = holdings[i].find('shrsOrPrnAmt').find('sshPrnamt').text
            except:
                pass
            try:
                d['sshPrnamtType'] = holdings[i].find('shrsOrPrnAmt').find('sshPrnamtType').text
            except:
                pass
            try:
                d['putCall'] = holdings[i].find('putCall').text
            except:
                 pass
            try:
                d['investmentDiscretion'] = holdings[i].find('investmentDiscretion').text
            except:
                pass
            try:
                d['otherManager'] = holdings[i].find('otherManager').text
            except:
                pass
            try:
                d['votingAuthoritySole'] = holdings[i].find('votingAuthority').find('Sole').text
            except:
                pass
            try:
                d['votingAuthorityShared'] = holdings[i].find('votingAuthority').find('Shared').text
            except:
                pass
            try:
                d['votingAuthorityNone'] = holdings[i].find('votingAuthority').find('None').text
            except:
                pass

        for items in range(len(data1)):    
            try:
                Security.objects.get_or_create(cusip = data1['cusip'],securityName = data1['nameOfIssuer'] ,securityType = 'STOCK',titleOfClass = data1['titleOfClass'])
            except:
                pass
            data1.append(d)
        col_headers = list(d.keys())
        return(col_headers, data)

      
    def get_holdings_xml2(self, xml_file2):
        self.browser.get(xml_file2)
        soup = BeautifulSoup(self.browser.page_source, "xml")
        holdings2 = soup.find_all('coverPage')
        data2 = []
        
        filingtype=''
        for i in range(len(holdings2)):
            d2 = {}
            try:
                d2['reportCalendarOrQuarter'] = holdings2[i].find('reportCalendarOrQuarter').text
            except:
                pass
            try:
                d2['isAmendment'] = holdings2[i].find('isAmendment').text
            except:
                pass
            try:
                d2['filing_manager_name'] = holdings2[i].find('filingManager').find('name').text
            except:
                pass
# =============================================================================================================================================
            try:
                d2['filingManager_address1_street1'] = holdings2[i].find('filingManager').find('address').find('com:street1').text
            except:
                pass

            try:
                d2['filingManager_address1_street1'] = holdings2[i].find('filingManager').find('address').find('ns1:street1').text
            except:
                pass
# =============================================================================================================================================
            try:
                d2['filingManager_address2_street2'] = holdings2[i].find('filingManager').find('address').find('com:street2').text
            except:
                pass

            try:
                d2['filingManager_address2_street2'] = holdings2[i].find('filingManager').find('address').find('ns1:street2').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['filingManager_address3_city'] = holdings2[i].find('filingManager').find('address').find('com:city').text
            except:
                pass

            try:
                d2['filingManager_address3_city'] = holdings2[i].find('filingManager').find('address').find('ns1:city').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['filingManager_address4_state-or-country'] = holdings2[i].find('filingManager').find('address').find('com:stateOrCountry').text
            except:
                pass

            try:
                d2['filingManager_address4_state-or-country'] = holdings2[i].find('filingManager').find('address').find('ns1:stateOrCountry').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['filingManager_address5_zipCode'] = holdings2[i].find('filingManager').find('address').find('com:zipCode').text
            except:
                pass

            try:
                d2['filingManager_address5_zipCode'] = holdings2[i].find('filingManager').find('address').find('ns1:zipCode').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['reportType'] = holdings2[i].find('reportType').text
            except:
                 pass
            try:
                d2['form13FFileNumber'] = holdings2[i].find('form13FFileNumber').text
            except:
                pass
            try:
                d2['otherManager_form13fFileNumber'] = holdings2[i].find('otherManager').find('form13FFileNumber').text
            except:
                pass
            try:
                d2['otherManager_name'] = holdings2[i].find('otherManager').find('name').text
            except:
                pass    
            try:
                d2['provideInfoForInstruction5'] = holdings2[i].find('provideInfoForInstruction5').find('Sole').text
            except:
                pass

          
            data2.append(d2)

            
            ad=d2['filingManager_address1_street1']+', '+d2['filingManager_address3_city']+', '+d2['filingManager_address4_state-or-country']+', '+d2['filingManager_address5_zipCode']
            
            Company.objects.get_or_create(name=d2['filing_manager_name'].lower(),address=ad.lower(),companyType='HF',cik=self.ticker)


            filenumber=''
            if(d2['form13FFileNumber'][0]=='0'):
                filenumber=d2['form13FFileNumber']
            else:
                filenumber='0'+d2['form13FFileNumber']

            
            
            if(filenumber[4]!='0' and len(filenumber)==8):
                finalfilenumber=filenumber[0:4]+'0'+filenumber[4:10]
            else:
                finalfilenumber=filenumber


            # =========================================================================================================================
            cc = Company.objects.get(cik=self.ticker)
            Filer.objects.get_or_create(companyId=cc,fileNumber=finalfilenumber,fileType='13F')
            ff = Filer.objects.get(fileNumber=finalfilenumber,companyId=cc)  
            
            try:
                otherparentfilenumber=''
                if(d2['otherManager_form13fFileNumber'][0]=='0'):
                    otherparentfilenumber=d2['otherManager_form13fFileNumber']
                else:
                    otherparentfilenumber='0'+d2['otherManager_form13fFileNumber']

                
                if(otherparentfilenumber[4]!='0' and len(otherparentfilenumber)==8):
                    otherparentfinalfilenumber=otherparentfilenumber[0:4]+'0'+otherparentfilenumber[4:10]
                else:
                    otherparentfinalfilenumber=otherparentfilenumber

            except:
                pass


            try:
                Filer.objects.get_or_create(fileNumber=otherparentfinalfilenumber)
            except:
                pass
            try:
                ffp = Filer.objects.get(fileNumber=otherparentfinalfilenumber)
            except:
                pass
            
        col_headers2 = list(d2.keys())
      

        holdings3 = soup.find_all('summaryPage')
        d3 = {}
        data3 = []
        oc=0
        try:
            d3['otherIncludedManagersCount'] = holdings3[i].find('otherIncludedManagersCount').text
        except:
            pass

        try:
            d3['tableEntryTotal'] = holdings3[i].find('tableEntryTotal').text
        except:
            pass

        try:
            d3['tableValueTotal'] = holdings3[i].find('tableValueTotal').text
        except:
            pass

        try:
            d3['isConfidentialOmitted'] = holdings3[i].find('isConfidentialOmitted').text
        except:
            pass

        data3.append(d3)
 
        oc = d3['otherIncludedManagersCount']
        
        if d2['reportType']=='13F HOLDINGS REPORT':
            filingtype='HR'
        elif d2['reportType']=='13F COMBINATION REPORT':
            filingtype='CR'
        else:
            filingtype='NT'

        Quarter=''
        if(d2['reportCalendarOrQuarter'][:2]=='03'):
            Quarter='1'+d2['reportCalendarOrQuarter'][6:11]
        elif(d2['reportCalendarOrQuarter'][:2]=='06'):
            Quarter='2'+d2['reportCalendarOrQuarter'][6:11]
        elif(d2['reportCalendarOrQuarter'][:2]=='09'):
            Quarter='3'+d2['reportCalendarOrQuarter'][6:11]
        else:
            Quarter='4'+d2['reportCalendarOrQuarter'][6:11]

        QuarterlyHolding.objects.get_or_create(filerId = ff, quarter =Quarter  ,filingType=filingtype ,filedOn = d2['reportCalendarOrQuarter'] ,acceptedAt = d2['reportCalendarOrQuarter'],totalValue =d3['tableValueTotal'] )
        
        qq = QuarterlyHolding.objects.get(filerId = ff,quarter=Quarter)
# ===========================================================================================================

        holdings4 = soup.find_all('otherManager2')
        data4 = []

        for i in range(len(holdings4)):
            d4 = {}
            try:
                d4['sequenceNumber'] = holdings4[i].find('sequenceNumber').text
            except:
                pass

            try:
                d4['form13FFileNumber'] = holdings4[i].find('otherManager').find('form13FFileNumber').text
            except:
                pass

            try:
                d4['name'] = holdings4[i].find('otherManager').find('name').text
            except:
                pass
            
            try:
                otherchildfilenumber=''
                if(d4['form13FFileNumber'][0]=='0'):
                    otherchildfilenumber=d4['form13FFileNumber']
                else:
                    otherchildfilenumber='0'+d4['form13FFileNumber']
  
                otherchildfinalfilenumber=''
                if(otherchildfilenumber[4]!='0' and len(otherchildfilenumber)==8):
                    otherchildfinalfilenumber=otherchildfilenumber[0:4]+'0'+otherchildfilenumber[4:10]
                else:
                    otherchildfinalfilenumber=otherchildfilenumber

            except:
                pass
            try:
                Filer.objects.get_or_create(fileNumber=otherchildfinalfilenumber)                
            except:
                pass

            try:
                ffc = Filer.objects.get(fileNumber=otherchildfinalfilenumber)
            except:
                pass
            
            try:
                QuarterlyOtherManager.objects.get_or_create(parentFilerId =ffp ,childFilerId =ffc ,quarterlyHoldingId = qq,number=oc )
            except:
                pass
            
            try:
                QuarterlyOtherManager.objects.get_or_create(childFilerId =ffc ,quarterlyHoldingId = qq,number=oc )
            except:
                pass
            try:
                QuarterlyOtherManager.objects.get_or_create(parentFilerId =ffp ,quarterlyHoldingId = qq,number=oc )
            except:
                pass
            try:
                qom = QuarterlyOtherManager.objects.get(quarterlyHoldingId = qq,number=oc )

            except:
                pass
            data4.append(d4)
          
        for i in range(len(data1)):
     
            try:
         
                ss=Security.objects.get(cusip = data1[i]['cusip'],securityName = data1[i]['nameOfIssuer'],titleOfClass = data1[i]['titleOfClass'])
                
            except:
                print("Ss not retreived")
                pass
            try:
                QuarterlySecurityHolding.objects.get_or_create(securityId = ss,quarterlyHoldingId = qq,value = data1[i]['value'],amount = data1[i]['sshPrnamt'], holdingType = data1[i]['sshPrnamtType'],investmentDiscretion = data1[i]['investmentDiscretion'],sole = data1[i]['votingAuthoritySole'],shared = data1[i]['votingAuthorityShared'],none = data1[i]['votingAuthorityNone'])
                qsh = QuarterlySecurityHolding.objects.get(securityId = ss,quarterlyHoldingId = qq,value = data1[i]['value'],amount = data1[i]['sshPrnamt'], holdingType = data1[i]['sshPrnamtType'],investmentDiscretion = data1[i]['investmentDiscretion'],sole = data1[i]['votingAuthoritySole'],shared = data1[i]['votingAuthorityShared'],none = data1[i]['votingAuthorityNone'])
                print(qsh)
            except:
                print("Problem is here")
                pass
            try:
                QuarterlyOtherManagerDistribution.objects.get_or_create(quarterlyOtherManagerId =qom ,quarterlySecurityHoldingId =qsh)
            except:
                print("Problem was here")
                pass
        data1.clear()
        return(col_headers2, data2)



    def save_holdings_xml(self, file_name, report_headers, col_headers, data, col_headers2, data2):
        """Create and write holdings data from XML to tab-delimited text file."""
        with open(file_name, 'w', newline='') as f:

            # writing data to csv as lists
            csv_writer = writer(f, dialect='excel')

            # for d in report_headers:
                # csv_writer.writerow([d.get(k, 'n/a') for k in col_report])
                # csv_writer.writerow(d)
            for i in range(len(report_headers)):
                csv_writer.writerow([report_headers[i]])

            csv_writer.writerow(col_headers)
            for row in data:
                csv_writer.writerow([row.get(k, 'n/a') for k in col_headers])


            csv_writer.writerow(col_headers2)
            for row in data2:
                csv_writer.writerow([row.get(k, 'n/a') for k in col_headers2])

        # print(col_headers2)



            # # writing data to csv as dictionary
            # dict_writer = DictWriter(f,dialect='excel',fieldnames=col_headers)
            # # for i in range(len(report_headers)):
            # #     csv_writer.writerow([report_headers[i]])
            # dict_writer.writeheader()
            # # dict_writer.writerows(data)
            # for row in data:
            #     dict_writer.writerow([row.get(k, 'n/a') for k in col_headers])
            #     # dict_writer.writerow(row)   #For dictionary

    def get_holdings_ascii(self, txt_file):
        """Get holdings detail from ASCII file and store data.

        ASCII format was used pre-2013 decision to use XML. Read and find
        holdings details from ASCII text file. Store data in 'temp_holdings.txt'
        file for save_holdings_ascii().
        """
        data = urllib.request.urlopen(txt_file)
        parse = False
        temp_file = 'temp_holdings.txt'
        with open(temp_file, 'w', newline='') as f:
            writer = csv.writer(f)
            # Look for table storing holdings data before writing to file
            for line in data:
                line = line.decode('UTF-8').strip()
                if re.search('^<TABLE>', line) or re.search('^<Table>', line):
                    parse = True
                if re.search('^</TABLE>$', line) or re.search('^</Table>$', line):
                    parse = False
                if parse:
                    writer.writerow([line])

        return(temp_file)

    def save_holdings_ascii(self, file_name, report_headers, data):
        """Retrieves and reads 'temp_holdings.txt', then writes to tab-delimited file.

        Parse holdings data in ASCII text format, splitting each line
        by looking for 2 or more whitespaces, stores each line in 'holdings',
        then writes to tab-delimited text file.
        """
        with open(data, 'r') as f:
            holdings = []
            for line in f:
                line = line.strip()
                columns = re.split(r'\s{2,}', line)
                holdings.append(columns)

        # Write comma delimited file
        file_name = 'ASCII_' + file_name
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            for i in range(len(report_headers)):
                writer.writerow([report_headers[i]])
            for row in holdings:
                writer.writerow([row[i] for i in range(len(row))])

    def remove_temp_file(self):
        """Deletes temp file used to parse ASCII data."""
        os.remove('temp_holdings.txt')

    def scrape(self):
        """Main method to start scraper and find SEC holdings data."""
        self.find_filings()
        self.browser.quit()
