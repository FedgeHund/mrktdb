import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()
from next_prev import next_in_order, prev_in_order
from edgar.models import QuarterlyHolding, QuarterlySecurityHolding, Filer
from edgar.models import Security as edgarSecurity 
from securities.models import Quarter, Security

quarterlyholdings_all = securities = quarterlysecurityholdings = quarterlysecurityholdings_all = []
securities = edgarSecurity.objects.all()
filers = Filer.objects.all()
quarterlyholdings_all = QuarterlyHolding.objects.all()
quarterlysecurityholdings = QuarterlySecurityHolding.objects.all()

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
securities_securities=Security.objects.all()
for security in securities_securities:
    
    # saare quarterly security holding for a security for all filers ke liye value divide by quantity
    for quarter in quarterlyholdings_all:
        total_value = 0
        total_quantity = 0
        avg_value = 0
        for filer in filers:
            try:
                print(security.name,security.titleOfClass)
                print(edgarSecurity.objects.filter(securityName=security.name,titleOfClass=security.titleOfClass).first())
                print(QuarterlySecurityHolding.objects.filter(securityId=edgarSecurity.objects.filter(securityName=security.name,titleOfClass=security.titleOfClass).first(),quarterlyHoldingId=QuarterlyHolding.objects.filter(quarter = quarter.quarter,filerId=filer).first()).first())
                total_value = total_value + QuarterlySecurityHolding.objects.filter(securityId=edgarSecurity.objects.filter(securityName=security.name,titleOfClass=security.titleOfClass).first(),quarterlyHoldingId=QuarterlyHolding.objects.filter(quarter = quarter.quarter,filerId=filer).first()).first().marketvalue*1000
            except:
                print('Here')
                pass
            try:
                total_quantity = total_quantity + QuarterlySecurityHolding.objects.filter(securityId=edgarSecurity.objects.filter(securityName=security.name,titleOfClass=security.titleOfClass).first(),quarterlyHoldingId=QuarterlyHolding.objects.filter(quarter = quarter.quarter,filerId=filer).first()).first().quantity
            except:
                print('Here')
                pass
        try:
            if(total_quantity==0):
                q = Quarter(value=None,quarter=quarter.quarter, securityId=security)
            else:
                avg_value = total_value/total_quantity
                try:
                    q = Quarter(value=avg_value,quarter=quarter.quarter, securityId=security)
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
