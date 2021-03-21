import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from next_prev import next_in_order, prev_in_order
from edgar.models import Company, QuarterlyHolding, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager, Filer, Security
from holdings.models import Position
from security.models import Price
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
    arrr = []
    for quarterlyholding in quarterlyholdings:
        arr = {}
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
                qq = QuarterlySecurityHolding.objects.filter(quarterlyHoldingId=next_in_order(quarterlyholding),securityId = security_id).first()
                if(qq!=None):
                    previous_weight_percent = (qq.marketvalue/previous_total_market_value)*100
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
            for quarterlyholdingobject in quarterlyholdings:
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
            price = None
            
            try:
                priceobject = Price.objects.filter(name=security_id.securityName,quarter=quarterlyholding.quarter).first()
                if(priceobject):
                    arr['lastPrice'] = priceobject.value
                    print(price)
            except:
                print('price for security not available')
                pass
            arr['quarter'] = quarterlyholding.quarter
            arr['filerId'] = filer
            arr['securityName'] = security_id.securityName
            arr['filerName'] = quarterlyholding.filerId.companyId.name
            arr['securityId']=security_id
            arr['quarterId']=quarterlyholding
            arr['investmentDiscretion']=quarterlysecurityholding.investmentDiscretion
            arr['marketValue']=quarterlysecurityholding.marketvalue
            arr['quantity']=quarterlysecurityholding.quantity
            arr['weightPercent']=weight_percent 
            arr['changeInShares'] = change_in_shares
            arr['positionType'] = position_type
            arr['previousWeightPercent'] = previous_weight_percent
            arr['changeInPositionPercent'] = position_change
            arr['sourceType'] = filer.fileType
            arr['sourcedOn']=quarterlyholding.filedOn
            if(qtr_first_owned!=None):
                arr['quarterFirstOwned']=qtr_first_owned
            arrr.append(arr)
            
    try:
        PositionObjectstbs = [
            Position(
                quarter = arrr[i]['quarter'],
                filerId = arrr[i]['filerId'],
                securityName = arrr[i]['securityName'],
                filerName = arrr[i]['filerName'],
                securityId = arrr[i]['securityId'],
                quarterId = arrr[i]['quarterId'],
                investmentDiscretion = arrr[i]['investmentDiscretion'],
                marketValue = arrr[i]['marketValue'],
                quantity = arrr[i]['quantity'],
                weightPercent = arrr[i]['weightPercent'],
                changeInShares = arrr[i]['changeInShares'],
                positionType = arrr[i]['positionType'],
                previousWeightPercent = arrr[i]['previousWeightPercent'],
                changeInPositionPercent = arrr[i]['changeInPositionPercent'],
                sourceType = arrr[i]['sourceType'],
                sourcedOn = arrr[i]['sourcedOn']
            )for i in range(len(arrr))
        ]
    except:
        print("Exception caught while creating PositionObjectstbs list")
        pass
    print("Bulk Save for Position Started")
    try:
        Position.objects.bulk_create(PositionObjectstbs)
    except:
        print("Exception caught while saving Position")
        pass
    print("Bulk Save for Position Ended")    
            # if(qtr_first_owned!=None):
            #     position = Position(lastPrice=price,quarter=quarterlyholding.quarter,securityName=security_id.securityName,filerName=quarterlyholding.filerId.companyId.name,securityId=security_id,quarterId=quarterlyholding,investmentDiscretion=quarterlysecurityholding.investmentDiscretion,marketValue=quarterlysecurityholding.marketvalue,quantity=quarterlysecurityholding.quantity, weightPercent=weight_percent, changeInShares = change_in_shares, positionType = position_type, previousWeightPercent = previous_weight_percent, changeInPositionPercent = position_change, sourceType = filer.fileType, sourcedOn=quarterlyholding.filedOn, quarterFirstOwned=qtr_first_owned)
            # else:
            #     position = Position(lastPrice=price,quarter=quarterlyholding.quarter,securityName=security_id.securityName,filerName=quarterlyholding.filerId.companyId.name,securityId=security_id,quarterId=quarterlyholding,investmentDiscretion=quarterlysecurityholding.investmentDiscretion,marketValue=quarterlysecurityholding.marketvalue,quantity=quarterlysecurityholding.quantity, weightPercent=weight_percent, changeInShares = change_in_shares, positionType = position_type, previousWeightPercent = previous_weight_percent, changeInPositionPercent = position_change, sourceType = filer.fileType, sourcedOn=quarterlyholding.filedOn)
            # position.save()

