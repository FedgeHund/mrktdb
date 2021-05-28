from rest_framework import serializers
from .models import Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['quarter','securityName','filerName','filerId_id','securityId_id','cik', 'cusip', 'ticker', 'type1', 'type2', 'investmentDiscretion','quantity','marketValue','weightPercent','previousWeightPercent','estimatedAverageCost','lastPrice','estimatedProfit','ranking','changeInShares','changeOfValue','changeInPositionPercent','sourceType','sourcedOn','positionType','positionId','createdAt','updatedAt','deletedAt']

class NumberOfFilersHoldingTheStockSerializer(serializers.ModelSerializer):
    numberHolding = serializers.IntegerField()

    class Meta:
        model = Position
        fields = ['numberHolding', 'quarter','securityName','filerName','filerId_id','securityId_id','cik', 'cusip', 'ticker', 'type1', 'type2', 'investmentDiscretion','quantity','marketValue','weightPercent','previousWeightPercent','estimatedAverageCost','lastPrice','estimatedProfit','ranking','changeInShares','changeOfValue','changeInPositionPercent','sourceType','sourcedOn','positionType','positionId','createdAt','updatedAt','deletedAt']

class TotalNumberOfSharesHeldSerializer(serializers.ModelSerializer):
    totalSharesHeld = serializers.IntegerField()
    
    class Meta:
        model = Position
        fields = ['totalSharesHeld', 'quarter','securityName','filerName','filerId_id','securityId_id','cik', 'cusip', 'ticker', 'type1', 'type2', 'investmentDiscretion','quantity','marketValue','weightPercent','previousWeightPercent','estimatedAverageCost','lastPrice','estimatedProfit','ranking','changeInShares','changeOfValue','changeInPositionPercent','sourceType','sourcedOn','positionType','positionId','createdAt','updatedAt','deletedAt']

class NetBuysSerializer(serializers.ModelSerializer):
    netBuys = serializers.IntegerField()
    
    class Meta:
        model = Position
        fields = ['netBuys', 'quarter','securityName','filerName','filerId_id','securityId_id','cik', 'cusip', 'ticker', 'type1', 'type2', 'investmentDiscretion','quantity','marketValue','weightPercent','previousWeightPercent','estimatedAverageCost','lastPrice','estimatedProfit','ranking','changeInShares','changeOfValue','changeInPositionPercent','sourceType','sourcedOn','positionType','positionId','createdAt','updatedAt','deletedAt']

class NetSellsSerializer(serializers.ModelSerializer):
    netSells = serializers.IntegerField()
    
    class Meta:
        model = Position
        fields = ['netSells', 'quarter','securityName','filerName','filerId_id','securityId_id','cik', 'cusip', 'ticker', 'type1', 'type2', 'investmentDiscretion','quantity','marketValue','weightPercent','previousWeightPercent','estimatedAverageCost','lastPrice','estimatedProfit','ranking','changeInShares','changeOfValue','changeInPositionPercent','sourceType','sourcedOn','positionType','positionId','createdAt','updatedAt','deletedAt']