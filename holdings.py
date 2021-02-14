import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from next_prev import next_in_order, prev_in_order
from edgar.models import Company, QuarterlyHolding, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager, Filer, Security
from holdings.models import Position

companies = filers = quarterlyholdings = securities = quarterlyothermanagerdistributions = quarterlysecurityholdings = quarterlysecurityholdings_all = quarterlyothermanagers = []
companies = Company.objects.all()
filers = Filer.objects.all()
securities = Security.objects.all()
quarterlyholdings_all = QuarterlyHolding.objects.all()
quarterlyothermanagerdistributions = QuarterlyOtherManagerDistribution.objects.all()
quarterlysecurityholdings = QuarterlySecurityHolding.objects.all()
quarterlyothermanagers = QuarterlyOtherManager.objects.all()


#############################################################################################################################

#############################################################################################################################

for filer in filers:
    quarterlyholdings = QuarterlyHolding.objects.filter(filerId=filer)
    for quarterlyholding in quarterlyholdings:
        quarterlysecurityholdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=quarterlyholding)
        previous_quarterlysecurityholdings = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding))
        total_market_value = 0
        previous_total_market_value = 0
        
        for quarterlysecurityholding in previous_quarterlysecurityholdings:
            previous_total_market_value = quarterlysecurityholding.marketvalue + previous_total_market_value 
        for quarterlysecurityholding in quarterlysecurityholdings:
            total_market_value = quarterlysecurityholding.marketvalue + total_market_value 
            security_id = quarterlysecurityholding.securityId
            weight_percent = 0
            previous_weight_percent = 0
            weight_percent = (quarterlysecurityholding.marketvalue/total_market_value)*100

            try:
                if(QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding),securityId = security_id).first()!=None):
                    previous_weight_percent = (QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding),securityId = security_id).first().marketvalue/previous_total_market_value)*100
            except:
                print("Error while calculating previous weight percent")
                pass
            # Get previous quarter
            prev_quarter_id = next_in_order(quarterlyholding)
            
            #Get previous quarterly security holding id for that security
            change_in_shares = 0
            position_type = ''
            position_change = 0
            quarterlysecurityholdings_for_filer_for_security=[]
            quarterlyholdingobjects = QuarterlyHolding.objects.filter(filerId = filer)
            for quarterlyholdingobject in quarterlyholdingobjects:
                quarterlysecurityholding_for_filer_for_security = QuarterlySecurityHolding.objects.filter(securityId = security_id, quarterlyHoldingId = quarterlyholdingobject).first()
                if (quarterlysecurityholding_for_filer_for_security!=None):
                    quarterlysecurityholdings_for_filer_for_security.append(quarterlysecurityholding_for_filer_for_security)
            qtr_first_owned = None
            try:
                for i in range(len(quarterlysecurityholdings_for_filer_for_security)-1):
                    if(i<len(quarterlysecurityholdings_for_filer_for_security)):
                        print(quarterlysecurityholdings_for_filer_for_security[i+1].quantity)
                        if (quarterlysecurityholdings_for_filer_for_security[i+1].quantity == 0):
                            qtr_first_owned = quarterlysecurityholdings_for_filer_for_security[i+1].quarterId
                            break
                    else:
                        break
            except:
                pass

            try:
                if(prev_quarter_id!=None):
                    prev_quarterly_security_holding_id_e = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId = prev_quarter_id, securityId = security_id ).first()
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
                        pass
                else:
                    pass
            except:
                print("No prev quarter")
                pass

            if(qtr_first_owned!=None):
                position = Position(securityId=security_id,quarterId=quarterlyholding,investmentDiscretion=quarterlysecurityholding.investmentDiscretion,marketValue=quarterlysecurityholding.marketvalue,quantity=quarterlysecurityholding.quantity, weightPercent=weight_percent, changeInShares = change_in_shares, positionType = position_type, previousWeightPercent = previous_weight_percent, changeInPositionPercent = position_change, sourceType = filer.fileType, sourcedOn=quarterlyholding.filedOn, quarterFirstOwned=qtr_first_owned)
            else:
                position = Position(securityId=security_id,quarterId=quarterlyholding,investmentDiscretion=quarterlysecurityholding.investmentDiscretion,marketValue=quarterlysecurityholding.marketvalue,quantity=quarterlysecurityholding.quantity, weightPercent=weight_percent, changeInShares = change_in_shares, positionType = position_type, previousWeightPercent = previous_weight_percent, changeInPositionPercent = position_change, sourceType = filer.fileType, sourcedOn=quarterlyholding.filedOn)
            position.save()

