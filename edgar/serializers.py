from rest_framework import serializers
from .models import Company, Filer, QuarterlyHolding, Security, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager, FailsToDeliver

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'createdAt', 'updatedAt', 'deletedAt', 'companyId', 'cik','address', 'companyType']

class FilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filer
        fields = ['companyId', 'fileNumber', 'createdAt', 'updatedAt', 'deletedAt', 'filerId', 'fileType']


class QuarterlyHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyHolding
        fields = ['filerId', 'quarter', 'filingType', 'filedOn', 'acceptedAt', 'totalValue', 'createdAt', 'updatedAt', 'deletedAt', 'quarterlyHoldingId']



class QuarterlyOtherManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyOtherManager
        fields = ['parentFilerId', 'childFilerId', 'quarterlyHoldingId', 'number', 'createdAt', 'updatedAt', 'deletedAt', 'otherManagerId']
    

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ['companyId', 'cusip', 'securityName', 'securityType', 'ticker', 'titleOfClass', 'createdAt', 'updatedAt', 'deletedAt', 'securityId']


class QuarterlySecurityHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlySecurityHolding
        fields = ['securityId', 'quarterlyHoldingId', 'marketvalue', 'amount', 'holdingType', 'investmentDiscretion', 'sole', 'shared', 'none', 'createdAt', 'updatedAt', 'deletedAt', 'quarterlySecurityHoldingId']


class QuarterlyOtherManagerDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyOtherManagerDistribution
        fields = ['quarterlyOtherManagerId', 'quarterlySecurityHoldingId', 'createdAt', 'updatedAt', 'deletedAt', 'quarterlyOtherManagerDistributionId']

class FailsToDeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailsToDeliver
        fields = ('settlementDate', 'createdAt', 'cusip', 'ticker', 'quantity', 'description')