from rest_framework import serializers
from .models import Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['quarter','securityName','filerName','securityId','quarterId','quarterFirstOwned','investmentDiscretion','quantity','marketValue','weightPercent','previousWeightPercent','estimatedAverageCost','lastPrice','estimatedProfit','ranking','changeInShares','changeInPositionPercent','sourceType','sourcedOn','positionType','positionId','createdAt','updatedAt','deletedAt']