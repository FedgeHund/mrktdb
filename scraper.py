

"""
scraper.py contains the main functionality to find and scrape
holdings data from 13F filings on https://www.sec.gov.

See comments in README.md for instructions on how to run
the scraper.

Note, the scraper will find all filings for a cik and
generated a text file for each in the current directory.
"""
from csv import writer
from csv import DictWriter
import csv
import datetime
import os
import time
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from edgar.models import Company, Filer, QuarterlyHolding, Security, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager
import re
import sys
import time
import urllib.request
import urllib.parse
from django.utils.timezone import now
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
SEC_LINK = "https://www.sec.gov/edgar/searchedgar/companysearch.html"
CIK_SEARCH_URL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK="
DOMAIN = "https://www.sec.gov"
infoTableData=[]
securitymaster=[]
cusiplist=[]

for se in Security.objects.all():
    securitymaster.append(se.cusip)

print(securitymaster)
print(len(securitymaster))
# valuelist=[]
# amountlist=[]
# holdingTypelist=[]
# investmentDiscretionlist=[]
# solelist=[]
# sharedlist=[]
# nonelist=[]
uinlist=[]
class HoldingsScraper:
    """Find holdings data in funds by scraping data from the SEC."""

    def __init__(self, cik):
        # Using Chrome Driver
        #self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

        # Using Firefox Driver
        # caps = DesiredCapabilities.FIREFOX.copy()
        # caps['marionette'] = False
        # self.browser = webdriver.Firefox(capabilities=caps,executable_path=r'C:\\geckodriver-v0.26.0-win64\\geckodriver.exe')

        # Using PhantomJS driver
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)
        self.cik = cik
        self.links = []

    def find_filings(self):
        """Open SEC page, feed HTML into BeautifulSoup, and find filings."""
        url = CIK_SEARCH_URL + self.cik
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
            sys.stdout.write('No results found for cik: %s\n' % self.cik)

    def retrieve_filings(self):
        """Retrieve links for all 13F filing from search results."""
        sys.stdout.write('Retrieving filings for: %s\n' % self.cik)
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
            holdings = self.infoTable(xml_file)
            col_headers = holdings[0]
            data = holdings[1]

            sys.stdout.write('Getting holdings from: %s\n' % xml_file2)
            coverPage = self.primaryDoc(xml_file2)
            col_headers2 = coverPage[0]
            coverPageData = coverPage[1]
            # self.save_holdings_xml(file_name, report_headers, col_headers, data, col_headers2, coverPageData)

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
        file_name = self.cik + '_' + str(date) + '_filing_date.csv'
        headers = []

        # # To get the cik, filing date and period of report in dictionary form, uncomment the below 5 lines
        # header_report = {}
        # header_report['cik'] = self.cik
        # header_report['Filing_Date'] = str(date)
        # header_report['Period_Of_Report'] = str(period)
        # headers.append(header_report)

        # headers.append('cik: ' + self.cik)
        # headers.append('Filing Date: ' + str(date))
        # headers.append('Period of Report: ' + str(period))

        headers.append(self.cik)
        headers.append(str(date))
        headers.append(str(period))

        # col_report = list(header_report.keys())
        return(file_name, headers)

    def infoTable(self, xml_file):
        """Get holdings detail from xml file and store data.

        XML format for filings was required by SEC in 2013.
        """
        self.browser.get(xml_file)
        soup = BeautifulSoup(self.browser.page_source, "xml")
        infoTable = soup.find_all('infoTable')
        data = []
        objs=[]
        toBeSaved=[]
        infoTableRow = {}
        cusiplist.clear()
        uinlist.clear()
        # Attempt retrieval of available attributes for 13F filings
        for i in range(len(infoTable)):
            infoTableRow = {}
            
            try:
                infoTableRow['nameOfIssuer'] = infoTable[i].find('nameOfIssuer').text
            except:
                pass
            try:
                infoTableRow['titleOfClass'] = infoTable[i].find('titleOfClass').text
            except:
                pass
            try:
                infoTableRow['cusip'] = infoTable[i].find('cusip').text
            except:
                pass
            try:
                infoTableRow['value'] = infoTable[i].find('value').text
            except:
                pass
            try:
                infoTableRow['sshPrnamt'] = infoTable[i].find('shrsOrPrnAmt').find('sshPrnamt').text
            except:
                pass
            try:
                infoTableRow['sshPrnamtType'] = infoTable[i].find('shrsOrPrnAmt').find('sshPrnamtType').text
            except:
                pass
            try:
                infoTableRow['putCall'] = infoTable[i].find('putCall').text
            except:
                 pass
            try:
                infoTableRow['investmentDiscretion'] = infoTable[i].find('investmentDiscretion').text
            except:
                pass
            try:
                infoTableRow['otherManager'] = infoTable[i].find('otherManager').text
            except:
                pass
            try:
                infoTableRow['votingAuthoritySole'] = infoTable[i].find('votingAuthority').find('Sole').text
            except:
                pass
            try:
                infoTableRow['votingAuthorityShared'] = infoTable[i].find('votingAuthority').find('Shared').text
            except:
                pass
            try:
                infoTableRow['votingAuthorityNone'] = infoTable[i].find('votingAuthority').find('None').text
            except:
                pass
            infoTableData.append(infoTableRow)
            randomNumber=random.randint(0,1000)
            uin=infoTableRow['cusip']+str(randomNumber)+infoTableRow['votingAuthoritySole']+infoTableRow['value']
            uinlist.append(uin)
            cusiplist.append(infoTableRow['cusip'])
            try:
                if infoTableRow['cusip'] not in securitymaster:
                    securitymaster.append(infoTableRow['cusip'])
                    toBeSaved.append(infoTableRow)
            except:
                print("No new security to be saved")
                pass

        try:        
            securityObjects = [
                Security(
                    cusip = toBeSaved[items]['cusip'],securityName = toBeSaved[items]['nameOfIssuer'] ,securityType = 'STOCK',titleOfClass = toBeSaved[items]['titleOfClass']
                )
                for items in range(len(toBeSaved))
            ]
        except:
            print("caught exception while creating security objects and appending them to the securityObjects list")
            pass

        print("Bulk Save for Securities Started")
        try:
            Security.objects.bulk_create(securityObjects)
        except:
            print("caught exception while saving securities")
            pass
        print("Bulk Save for Securities Ended")
        securityObjects.clear()
        toBeSaved.clear()
            
        col_headers = list(infoTableRow.keys())
        return(col_headers, data)

      
    def primaryDoc(self, xml_file2):
        self.browser.get(xml_file2)
        soup = BeautifulSoup(self.browser.page_source, "xml")
        coverPage = soup.find_all('coverPage')
        coverPageData = []
        
        filingtype=''
        for i in range(len(coverPage)):
            d2 = {}
            try:
                d2['reportCalendarOrQuarter'] = coverPage[i].find('reportCalendarOrQuarter').text
            except:
                pass
            try:
                d2['isAmendment'] = coverPage[i].find('isAmendment').text
            except:
                pass
            try:
                d2['amendmentType'] = coverPage[i].find('amendmentInfo').find('amendmentType').text
            except:
                pass
            try:
                d2['filing_manager_name'] = coverPage[i].find('filingManager').find('name').text
            except:
                pass
# =============================================================================================================================================
            try:
                d2['filingManager_address1_street1'] = coverPage[i].find('filingManager').find('address').find('com:street1').text
            except:
                pass

            try:
                d2['filingManager_address1_street1'] = coverPage[i].find('filingManager').find('address').find('ns1:street1').text
            except:
                pass
# =============================================================================================================================================
            try:
                d2['filingManager_address2_street2'] = coverPage[i].find('filingManager').find('address').find('com:street2').text
            except:
                pass

            try:
                d2['filingManager_address2_street2'] = coverPage[i].find('filingManager').find('address').find('ns1:street2').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['filingManager_address3_city'] = coverPage[i].find('filingManager').find('address').find('com:city').text
            except:
                pass

            try:
                d2['filingManager_address3_city'] = coverPage[i].find('filingManager').find('address').find('ns1:city').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['filingManager_address4_state-or-country'] = coverPage[i].find('filingManager').find('address').find('com:stateOrCountry').text
            except:
                pass

            try:
                d2['filingManager_address4_state-or-country'] = coverPage[i].find('filingManager').find('address').find('ns1:stateOrCountry').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['filingManager_address5_zipCode'] = coverPage[i].find('filingManager').find('address').find('com:zipCode').text
            except:
                pass

            try:
                d2['filingManager_address5_zipCode'] = coverPage[i].find('filingManager').find('address').find('ns1:zipCode').text
            except:
                pass

# =============================================================================================================================================
            try:
                d2['reportType'] = coverPage[i].find('reportType').text
            except:
                pass
            try:
                d2['form13FFileNumber'] = coverPage[i].find('form13FFileNumber').text
            except:
                pass
            try:
                d2['otherManager_form13fFileNumber'] = coverPage[i].find('otherManager').find('form13FFileNumber').text
            except:
                pass
            try:
                d2['otherManager_name'] = coverPage[i].find('otherManager').find('name').text
            except:
                pass    
            try:
                d2['provideInfoForInstruction5'] = coverPage[i].find('provideInfoForInstruction5').find('Sole').text
            except:
                pass
# ========================================================================================================================================
            coverPageData.append(d2)
            address=d2['filingManager_address1_street1']+', '+d2['filingManager_address3_city']+', '+d2['filingManager_address4_state-or-country']+', '+d2['filingManager_address5_zipCode']
            try:
                Company.objects.get_or_create(name=d2['filing_manager_name'].lower(),address=address.lower(),companyType='HF',cik=self.cik)
            except:
                print("caught exception while creating Company object")
                pass
            filenumber=''
            if(d2['form13FFileNumber'][0]=='0'):
                filenumber=d2['form13FFileNumber']
            else:
                filenumber='0'+d2['form13FFileNumber']
            
            try:
                if(filenumber[4]!='0' and len(filenumber)==8):
                    finalfilenumber=filenumber[0:4]+'0'+filenumber[4:10]
                else:
                    finalfilenumber=filenumber
            except:
                pass
            # =========================================================================================================================
            companyObject = Company.objects.get(cik=self.cik)
            print(companyObject)

            filerObject, created = Filer.objects.update_or_create(
                fileNumber=finalfilenumber ,fileType='13F',
                defaults={'companyId': companyObject},
            )
                        
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
                print(otherparentfinalfilenumber)
            except:
                pass


            try:
                parentFilerObject, created = Filer.objects.get_or_create(fileNumber=otherparentfinalfilenumber)
            except:
                pass
            print(coverPageData)
        col_headers2 = list(d2.keys())
# ==================================================================================================      
        signatureBlock = soup.find_all('signatureBlock')
        d7 = {}
        
        try:
            d7['signatureDate'] = signatureBlock[i].find('signatureDate').text
        except:
            print("FiledOn / Signature Date is not present for this filer")
            pass


        summaryPage = soup.find_all('summaryPage')
        d3 = {}
        summaryPageData = []
        otherManagerCount=0
        try:
            d3['otherIncludedManagersCount'] = summaryPage[i].find('otherIncludedManagersCount').text
        except:
            pass

        try:
            d3['tableEntryTotal'] = summaryPage[i].find('tableEntryTotal').text
        except:
            pass

        try:
            d3['tableValueTotal'] = summaryPage[i].find('tableValueTotal').text
        except:
            pass

        try:
            d3['isConfidentialOmitted'] = summaryPage[i].find('isConfidentialOmitted').text
        except:
            pass
 
        summaryPageData.append(d3)
        otherManagerCount = d3['otherIncludedManagersCount']
        
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
        
        try:
            if d2['isAmendment']=='true':
                filingtype=filingtype+'A' 
        except:
            pass
        isNewHolding=False
        try:
            if(d2['amendmentType']=='NEW HOLDINGS'):
                isNewHolding=True
        except:
            pass
        try:
            if(isNewHolding==True):
                QuarterlyHolding.objects.filter(filerId = filerObject,quarter=Quarter).update(filingType=filingType)
            else:
                qflag=False
                try:
                    if QuarterlyHolding.objects.get(filerId = filerObject,quarter=Quarter).filingType[2:3]=='A':
                        qflag=True
                except:
                    pass
                filedon = datetime.datetime.strptime(d7['signatureDate'][:8], '%m-%d-%y')
                try:
                    QuarterlyHolding.objects.get_or_create(filerId = filerObject, quarter =Quarter  ,filingType=filingtype ,filedOn = filedon ,acceptedAt = filedon,totalValue =d3['tableValueTotal'] ,totalEntry =d3['tableEntryTotal'])
                except:
                    print("Exception caught while creating QuarterlyHolding Object")
                    pass
                try:
                    if qflag==True:
                        QuarterlyHolding.objects.filter(filerId = filerObject,filingType=filingtype,quarter=Quarter).update(deletedAt=datetime.datetime.now())
                except:
                    pass
        except:
            pass
        
        quarterlyHoldingObject = QuarterlyHolding.objects.get(filerId = filerObject,quarter=Quarter,totalValue =d3['tableValueTotal'])
        print(quarterlyHoldingObject)
# ===========================================================================================================
        
        otherManager2 = soup.find_all('otherManager2')
        otherManager2Data = []
        childFilerObjectList= []
        sequenceNumberList = []
        childFilerObjectLists = []
        print(len(otherManager2))
        for i in range(len(otherManager2)):
            d4 = {}
            try:
                d4['sequenceNumber'] = otherManager2[i].find('sequenceNumber').text
            except:
                pass

            try:
                d4['form13FFileNumber'] = otherManager2[i].find('otherManager').find('form13FFileNumber').text
            except:
                pass

            try:
                d4['name'] = otherManager2[i].find('otherManager').find('name').text
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
                childFilerObject = Filer.objects.get(fileNumber=otherchildfinalfilenumber)
            except:
                pass
            
            try:
                QuarterlyOtherManager.objects.get_or_create(parentFilerId =parentFilerObject ,childFilerId =childFilerObject ,quarterlyHoldingId = quarterlyHoldingObject,number=d4['sequenceNumber'] )
            except:
                pass
            
            try:
                QuarterlyOtherManager.objects.get_or_create(childFilerId =childFilerObject ,quarterlyHoldingId = quarterlyHoldingObject,number=d4['sequenceNumber'] )
            except:
                pass
            try:
                QuarterlyOtherManager.objects.get_or_create(parentFilerId =parentFilerObject ,quarterlyHoldingId = quarterlyHoldingObject,number=d4['sequenceNumber'] )
            except:
                pass
            # try:
            #     QuarterlyOtherManagerObject = QuarterlyOtherManager.objects.get(quarterlyHoldingId = quarterlyHoldingObject,number=otherManagerCount )

            # except:
            #     pass\
            try:
                print(d4['sequenceNumber'])
            except:
                print("Exception caught at line 611")
                pass
            try:
                childFilerObjectList.append(childFilerObject)
                childFilerObjectLists=QuarterlyOtherManager.objects.filter(childFilerId__in=childFilerObjectList)

                sequenceNumberList.append(d4['sequenceNumber'])
                otherManager2Data.append(d4)
            except:
                print("Exception caught at line 614")
                pass
        try:
            childFilerMap = {}
            for i in range(len(sequenceNumberList)):
                childFilerMap[sequenceNumberList[i]] = childFilerObjectLists[i]

            for i in range(len(childFilerObjectLists)):
                correspondingsecurity = childFilerMap[childFilerObjectLists[i]]
        except:
            print("Exception caugth at line 624")
            pass
        print(childFilerMap)
          
        QuarterlySecurityHoldingObjectstbs=[]
        QuarterlyOtherManagerObjectstbs=[]
        # sss=[]
        print(quarterlyHoldingObject)
        print(len(cusiplist))
        print(len(infoTableData))

        # ===================================================================================================================

        # for i in range(len(infoTableData)):
        #     try:
        #         ss=Security.objects.get(cusip = infoTableData[i]['cusip'])
        #         sss.append(ss)
        #     except:
        #         print("Exception caught while getting security")
        #         pass
        SecurityList=[]
        FinalSecurityList=[]
        unique_cusip_list = [] 
      
    
        for x in cusiplist:         
            if x not in unique_cusip_list: 
                unique_cusip_list.append(x) 
        SecurityList=Security.objects.filter(cusip__in=unique_cusip_list)
        # print(len(SecurityList))
        # print(len(cusiplist))
        # for j in range(len(cusiplist)):
        #     for i in range(len(SecurityList)):
        #         try:
        #             if cusiplist[j] == SecurityList[i].cusip:
        #                 FinalSecurityList.append(SecurityList[i])
        #         except:
        #             pass
        map = {}
        for i in range(len(SecurityList)):
            map[SecurityList[i].cusip] = SecurityList[i]

        for i in range(len(unique_cusip_list)):
            correspondingsecurity = map[unique_cusip_list[i]]

       


        
        print(map)
       
        try:
            QuarterlySecurityHoldingObjectstbs = [
                QuarterlySecurityHolding(
                    securityId = map.get(cusiplist[i]),
                    quarterlyHoldingId = quarterlyHoldingObject,
                    marketvalue = infoTableData[i]['value'],
                    quantity = infoTableData[i]['sshPrnamt'], 
                    holdingType = infoTableData[i]['sshPrnamtType'],
                    investmentDiscretion = infoTableData[i]['investmentDiscretion'],
                    sole = infoTableData[i]['votingAuthoritySole'],
                    shared = infoTableData[i]['votingAuthorityShared'],
                    none = infoTableData[i]['votingAuthorityNone'],
                    uin=uinlist[i]
                    )for i in range(len(infoTableData))
            ]
        except:
            print("Exception caught while creating QuarterlySecurityHoldingObjectstbs list")
            pass
        print("Bulk Save for QuarterlySecurityHolding Started")
        try:
            QuarterlySecurityHolding.objects.bulk_create(QuarterlySecurityHoldingObjectstbs)
        except:
            print("Exception caught while saving QuarterlySecurityHolding")
            pass
        print("Bulk Save for QuarterlySecurityHolding Ended")
        try:
            print(QuarterlyOtherManagerObject)
        except:
            pass
        print(len(uinlist))
        QuarterlyOtherManagerObjectsList=[]
        QuarterlyOtherManagerObjectsList.clear()
        try:
            for i in range(len(infoTableData)):
                print(infoTableData[i]['otherManager'][0])                
                print(childFilerMap.get(infoTableData[i]['otherManager'][0]))
        except:
            print("PRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOBBBBBBBBBBBBBLEM")
            pass
        try:
            try:
                QuarterlyOtherManagerObjectsList=QuarterlySecurityHolding.objects.filter(uin__in=uinlist)
                print(len(QuarterlyOtherManagerObjectsList))
                QuarterlySecurityHoldingOM=[]
                QuarterlySecurityHoldingOM.clear()
                sequenceList=[]
                sequenceList.clear()
            except:
                print("Exception at 730")
                pass
            k=0
            try:
                print(infoTableData[0]['otherManager'].split(","))
            except:
                print("Exception at 736")
                pass
            for item in QuarterlyOtherManagerObjectsList:
                for items in infoTableData[k]['otherManager'].split(","):
                    print(item)
                    print(items)
                    sequenceList.append(items)
                    QuarterlySecurityHoldingOM.append(item)
                k=k+1
            print(len(QuarterlySecurityHoldingOM))
            try:
                QuarterlyOtherManagerObjectstbs = [
                    QuarterlyOtherManagerDistribution(
                        quarterlyOtherManagerId =childFilerMap.get(sequenceList[i]) ,
                        quarterlySecurityHoldingId = QuarterlySecurityHoldingOM[i]
                        )for i in range(len(QuarterlySecurityHoldingOM))
                ]
            except:
                print("Exception caught while creating QuarterlyOtherManagerObjectstbs list")
                pass
            
            
            print("Bulk Save for QuarterlyOtherManagerDistribution Started")
            
            try:
                QuarterlyOtherManagerDistribution.objects.bulk_create(QuarterlyOtherManagerObjectstbs)
            except:
                print("Exception caught while saving QuarterlyOtherManagerDistribution")
                pass
            print("Bulk Save for QuarterlyOtherManagerDistribution Ended")

        except:
            print("No other managers for this holding/filer")
            pass
        infoTableData.clear()
        sss.clear()
        cusiplist.clear()
        uinlist.clear()
        QuarterlyOtherManagerObjectsList.clear()

        return(col_headers2, coverPageData)



    def save_holdings_xml(self, file_name, report_headers, col_headers, data, col_headers2, coverPageData):
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
            for row in coverPageData:
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
