from rest_framework import serializers
from .models import FailsToDeliver

class FailsToDeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailsToDeliver
        fields = ('settlementDate', 'createdAt', 'cusip', 'ticker', 'quantity', 'description')


# class FailsToDeliverSerializer(serializers.ModelSerializer):
#     settlementDate = serializers.DateTimeField(format="%Y%m%d")
#     createdAt = serializers.DateTimeField()
#     cusip = serializers.TextField()
#     ticker = serializers.CharField()
#     quantity = serializers.IntegerField()
#     description = serializers.TextField()
#
#     class Meta:
#         model = FailsToDeliver
