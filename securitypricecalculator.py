import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from next_prev import next_in_order, prev_in_order
from edgar.models import QuarterlyHolding, QuarterlySecurityHolding, Filer, Security
from security.models import Price

quarterlyholdings_all = securities = quarterlysecurityholdings = quarterlysecurityholdings_all = []
securities = Security.objects.all()
filers = Filer.objects.all()
quarterlyholdings_all = QuarterlyHolding.objects.all()
quarterlysecurityholdings = QuarterlySecurityHolding.objects.all()
quarter = [42019,12020,22020,32020,42020]
#############################################################################################################################
securities_securities=Security.objects.all()
for security in securities_securities:
    print(security.name)
    quarterlysecurityholdingsforsecurity = QuarterlySecurityHolding.objects.filter(securityId=security)
    # saare quarterly security holding for a security for all filers ke liye value divide by quantity
    for quarter in quarters:
        total_value = 0
        total_quantity = 0
        avg_value = 0
        quarterlyholdingforquarter = QuarterlyHolding.objects.filter(quarter=quarter)
        quarterlysecurityholdingsforsecurity = QuarterlySecurityHolding.objects.filter(securityId=security,quarterId__in=quarterlyholdingforquarter)
        for quarterlysecurityholdingforsecurity in quarterlysecurityholdingsforsecurity:        
            try:                
                total_value = total_value + quarterlysecurityholdingforsecurity.marketvalue*1000
            except:
                print('Here')
                pass
            try:
                total_quantity = total_quantity + quarterlysecurityholdingforsecurity.quantity
            except:
                print('Here')
                pass
        try:
            if(total_quantity==0):
                q = Price(securityId=security, value = None, quarter = quarter, cusip = quarterlysecurityholdingforsecurity.cusip, name = security.name)
            else:
                avg_value = total_value/total_quantity
                try:
                    q = Price(securityId=security, value = avg_value, quarter = quarter, cusip = quarterlysecurityholdingforsecurity.cusip, name = security.name)
                except:
                    print('herrrr')
                    pass
            try:    
                q.save()
            except:
                print('Problem while saving')
                pass
        except:
            print('Problem while saving')
            pass
