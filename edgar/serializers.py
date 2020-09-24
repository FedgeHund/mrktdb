from rest_framework import serializers
from .models import FailsToDeliver

class FailsToDeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailsToDeliver
        fields = ('settlementDate', 'createdAt', 'cusip', 'ticker', 'quantity', 'description') 
