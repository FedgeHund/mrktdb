from rest_framework import serializers
from .models import QuarterlyFilerView


class QuarterlyFilerViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyFilerView
        fields = [
            'filerId',
            'filerName',
            'marketValue',
            'filerType',
            'cik',
            'quarter',
            'previousMarketValue',
            'previousHoldingsCount',
            'newHoldingsCount',
            'increasedHoldingsCount',
            'decreasedHoldingsCount',
            'soldOutHoldingsCount',
            'top10HoldingsPercent',
            'averageHoldingPeriod',
            'filerDescription',
            'quarterlyFilerViewId',
            'createdAt',
            'updatedAt',
            'deletedAt']
