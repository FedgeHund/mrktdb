import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from next_prev import next_in_order, prev_in_order
from edgar.models import Company, QuarterlyHolding, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager
from edgar.models import Filer as edgarFiler 
from edgar.models import Security as edgarSecurity 
from holdings.models import Quarter, Filer, Position, Security

companies = filers = quarterlyholdings = securities = quarterlyothermanagerdistributions = quarterlysecurityholdings = quarterlysecurityholdings_all = quarterlyothermanagers = []
companies = Company.objects.all()
filers = edgarFiler.objects.all()
securities = edgarSecurity.objects.all()
quarterlyholdings_all = QuarterlyHolding.objects.all()
quarterlyothermanagerdistributions = QuarterlyOtherManagerDistribution.objects.all()
quarterlysecurityholdings = QuarterlySecurityHolding.objects.all()
quarterlyothermanagers = QuarterlyOtherManager.objects.all()

#############################################################################################################################

# Saving all securities from edgar's security model

securityObjects=[]
try:        
    securityObjects = [
        Security(
            name = security.securityName ,titleOfClass = security.titleOfClass
        )
        for security in securities
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

#############################################################################################################################

#############################################################################################################################

for company in companies:
    ef = edgarFiler.objects.get(companyId=company)
    try:
        f = Filer(name=company.name,cik=company.cik,filer_type=company.companyType)
        f.save()
        f = Filer.objects.get(name=company.name,cik=company.cik,filer_type=company.companyType)
    except:
        print("Error saving filer")
        pass
    quarterlyholdings = QuarterlyHolding.objects.filter(filerId=ef)
    for quarterlyholding in quarterlyholdings:
        q = Quarter(quarter=quarterlyholding.quarter,filerId=f)
        q.save()
        q = Quarter.objects.get(quarter=quarterlyholding.quarter,filerId=f)
        quarterlysecurityholdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=quarterlyholding)
        previous_quarterlysecurityholdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding))
        print(len(quarterlysecurityholdings))
        total_market_value = 0
        previous_total_market_value = 0
        
        for quarterlysecurityholding in quarterlysecurityholdings:
            total_market_value = quarterlysecurityholding.marketvalue + total_market_value 
        for quarterlysecurityholding in previous_quarterlysecurityholdings:
            previous_total_market_value = quarterlysecurityholding.marketvalue + previous_total_market_value 
        for quarterlysecurityholding in quarterlysecurityholdings:
            security_id = Security.objects.get(name=quarterlysecurityholding.securityId.securityName,titleOfClass = quarterlysecurityholding.securityId.titleOfClass)
            weight_percent = 0
            previous_weight_percent = 0
            weight_percent = (quarterlysecurityholding.marketvalue/total_market_value)*100

            try:
                # print(QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding),securityId = edgarSecurity.objects.filter(securityName=quarterlysecurityholding.securityId.securityName,titleOfClass = quarterlysecurityholding.securityId.titleOfClass).first()).first())
                if(QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding),securityId = edgarSecurity.objects.filter(securityName=quarterlysecurityholding.securityId.securityName,titleOfClass = quarterlysecurityholding.securityId.titleOfClass).first()).first()!=None):
                    previous_weight_percent = (QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding),securityId = edgarSecurity.objects.filter(securityName=quarterlysecurityholding.securityId.securityName,titleOfClass = quarterlysecurityholding.securityId.titleOfClass).first()).first().marketvalue/previous_total_market_value)*100
            except:
                print("Error while calculating previous weight percent")
                pass
            # Get previous quarter
            prev_quarter_id_e = next_in_order(quarterlyholding)
            prev_quarter_id_h = next_in_order(q)
            print(prev_quarter_id_e)
            
            #Get previous quarterly security holding id for that security
            change_in_shares = 0
            position_type = ''
            # previous_weight = 0
            position_change = 0
            allsecurityobjects = QuarterlySecurityHolding.objects.filter(securityId = edgarSecurity.objects.filter(securityName=quarterlysecurityholding.securityId.securityName,titleOfClass = quarterlysecurityholding.securityId.titleOfClass).first())
            qtrfirstowned = None
            for i in range(len(allsecurityobjects)-1):
                if(i<len(allsecurityobjects)):
                    if (allsecurityobjects[i+1].quantity == 0):
                        qtrfirstowned = allsecurityobjects[i+1].quarterId
                        break
                else:
                    break
            try:
                if(prev_quarter_id_e!=None):
                    prev_quarterly_security_holding_id_e = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId = prev_quarter_id_e, securityId = edgarSecurity.objects.filter(securityName=quarterlysecurityholding.securityId.securityName,titleOfClass = quarterlysecurityholding.securityId.titleOfClass).first() ).first()
                    print(prev_quarterly_security_holding_id_e)
                    try:
                        

                        if(prev_quarterly_security_holding_id_e.quantity!=None):
                            change_in_shares = quarterlysecurityholding.quantity - prev_quarterly_security_holding_id_e.quantity

                            if(prev_quarterly_security_holding_id_e.quantity > quarterlysecurityholding.quantity):
                                position_type = 'Decreased'
                            if(prev_quarterly_security_holding_id_e.quantity < quarterlysecurityholding.quantity):
                                position_type = 'Increased'
                            if(prev_quarterly_security_holding_id_e.quantity == quarterlysecurityholding.quantity):
                                position_type = 'No Change'
                            position_change = ((quarterlysecurityholding.quantity/prev_quarterly_security_holding_id_e.quantity)-1)*100 #doubt: what happens when a security is added in this quarter
                            
                        else:
                            position_type = 'New'
                            position_change = None

                        
                    except:
                        print("=======>============>")
                        pass
                else:
                    print("=======>")
                    pass
            except:
                print("No prev quarter")
                pass

            if(qtrfirstowned!=None):
                position = Position(securityId=security_id,quarterId=q,investmentDiscretion=quarterlysecurityholding.investmentDiscretion,marketValue=quarterlysecurityholding.marketvalue,quantity=quarterlysecurityholding.quantity, weightPercent=weight_percent, changeInShares = change_in_shares, positionType = position_type, previousWeightPercent = previous_weight_percent, changeInPositionPercent = position_change, sourceType = ef.fileType, sourcedOn=quarterlyholding.filedOn, quarterFirstOwned=qtrfirstowned.quarter)
            else:
                position = Position(securityId=security_id,quarterId=q,investmentDiscretion=quarterlysecurityholding.investmentDiscretion,marketValue=quarterlysecurityholding.marketvalue,quantity=quarterlysecurityholding.quantity, weightPercent=weight_percent, changeInShares = change_in_shares, positionType = position_type, previousWeightPercent = previous_weight_percent, changeInPositionPercent = position_change, sourceType = ef.fileType, sourcedOn=quarterlyholding.filedOn)
            position.save()

