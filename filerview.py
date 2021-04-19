from edgar.models import QuarterlyHolding, Company, Security, Filer
from filer.models import QuarterlyFilerView
from holdings.models import Position
from next_prev import next_in_order, prev_in_order
import datetime
import sys
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fedgehundapi.settings')
django.setup()

quarters = filers = positions = securities = quarterlyfilerviews = []
filers = Filer.objects.all()


##########################################################################

for filer in filers:
    quarterlyholdings = QuarterlyHolding.objects.filter(filerId=filer)
    print(quarterlyholdings)
    for quarterlyholding in quarterlyholdings:
        company = Company.objects.filter(
            companyId=filer.companyId.companyId).first()
        # q = Quarter.objects.get(quarter=quarterlyholding.quarter,filerId=filer_for_positions)
        positions = Position.objects.filter(quarterId=quarterlyholding)
        if (len(positions) > 0):
            previous_market_value = 0
            previous_entry_count = 0
            try:
                previous_quarterlyholding_totalValue = next_in_order(
                    quarterlyholding)
                previous_market_value = previous_quarterlyholding_totalValue.totalValue
                previous_entry_count = previous_quarterlyholding_totalValue.totalEntry
            except BaseException:
                pass
            new_holdings = decreasedHoldingsCount = soldOutHoldingsCount = increasedHoldingsCount = newHoldingsCount = top10holdingspercent = total_market_value = 0
            description = ''
            description = '{} is a {} located out of {}. Their latest 13F filings show that they have at least {} AUM.'.format(
                company.name, company.companyType, company.address, quarterlyholding.totalValue)
            top10_positions_by_marketValue = positions.order_by(
                '-marketValue')[:10]
            for position in positions:
                if(position.positionType == 'Decreased' and position.quantity > 0):
                    decreasedHoldingsCount = decreasedHoldingsCount + 1
                if(position.positionType == 'Decreased' and position.quantity == 0):
                    soldOutHoldingsCount = soldOutHoldingsCount + 1
                if(position.positionType == 'Increased'):
                    increasedHoldingsCount = increasedHoldingsCount + 1
                if(position.positionType == 'New'):
                    newHoldingsCount = newHoldingsCount + 1
                total_market_value = total_market_value + position.marketValue
            for position in top10_positions_by_marketValue:
                top10holdingspercent = top10holdingspercent + position.marketValue
            top10holdingspercent = (
                top10holdingspercent / total_market_value) * 100
            q = QuarterlyFilerView(
                filerName=company.name,
                quarter=quarterlyholding.quarter,
                filerId=filer,
                cik=company.cik,
                filerType=company.companyType,
                marketValue=quarterlyholding.totalValue,
                previousMarketValue=previous_market_value,
                previousHoldingsCount=previous_entry_count,
                soldOutHoldingsCount=soldOutHoldingsCount,
                increasedHoldingsCount=increasedHoldingsCount,
                newHoldingsCount=newHoldingsCount,
                decreasedHoldingsCount=decreasedHoldingsCount,
                top10HoldingsPercent=top10holdingspercent,
                filerDescription=description)
            q.save()
