from rest_framework import serializers
from .models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'quarter',
            'securityName',
            'filerName',
            'filerId_id',
            'securityId_id',
            'cik',
            'cusip',
            'ticker',
            'type1',
            'type2',
            'investmentDiscretion',
            'quantity',
            'marketValue',
            'weightPercent',
            'previousWeightPercent',
            'estimatedAverageCost',
            'lastPrice',
            'estimatedProfit',
            'ranking',
            'changeInShares',
            'changeInPositionPercent',
            'sourceType',
            'sourcedOn',
            'positionType',
            'positionId',
            'createdAt',
            'updatedAt',
            'deletedAt']
