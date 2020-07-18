from rest_framework import serializers
from .models import Company, Filer, QuarterlyHolding, Security, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'createdAt', 'companyId', 'address', 'companyType']


# class CompanySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=80)
#     createdAt = serializers.DateTimeField()
#     companyId = serializers.IntegerField(read_only=True)
#     address = serializers.CharField(max_length=120)
#     companyType = serializers.CharField(max_length=19, default='COM')
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return CompanySerializer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.companyId = validated_data.get('companyId', instance.companyId)
#         instance.address = validated_data.get('address', instance.address)
#         instance.companyType = validated_data.get('companyType', instance.companyType)
#         instance.save()
#         return instance


class FilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filer
        fields = ['companyId', 'fileNumber', 'createdAt', 'filerId', 'fileType']

# class FilerSerializer(serializers.Serializer):
#     companyId = serializers.CharField()
#     fileNumber = serializers.CharField(max_length=10)
#     createdAt = serializers.DateTimeField()
#     filerId = serializers.IntegerField(read_only=True)
#     fileType = serializers.CharField(max_length=4)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Filer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.companyId = validated_data.get('companyId', instance.companyId)
#         instance.fileNumber = validated_data.get('fileNumber', instance.fileNumber)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.filerId = validated_data.get('filerId', instance.filerId)
#         instance.fileType = validated_data.get('fileType', instance.fileType)
#         instance.save()
#         return instance

class QuarterlyHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyHolding
        fields = ['filerId', 'quarter', 'filingType', 'filedOn', 'acceptedAt', 'valueTotal', 'createdAt', 'quarterId']


# class QuarterlyHoldingSerializer(serializers.Serializer):
#     filerId = serializers.CharField()
#     quarter = serializers.IntegerField()
#     filingType = serializers.CharField(max_length=3)
#     filedOn = serializers.IntegerField()
#     acceptedAt = serializers.IntegerField()
#     valueTotal = serializers.IntegerField()
#     createdAt = serializers.DateTimeField()
#     quarterId = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return QuarterlyHolding.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.filerId = validated_data.get('filerId', instance.filerId)
#         instance.quarter = validated_data.get('quarter', instance.quarter)
#         instance.filingType = validated_data.get('filingType', instance.filingType)
#         instance.filedOn = validated_data.get('filedOn', instance.filedOn)
#         instance.acceptedAt = validated_data.get('acceptedAt', instance.acceptedAt)
#         instance.valueTotal = validated_data.get('valueTotal', instance.valueTotal)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.quarterId = validated_data.get('quarterId', instance.quarterId)
#         instance.save()
#         return instance

class QuarterlyOtherManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyOtherManager
        fields = ['parentFilerId', 'childFilerId', 'quarterId', 'number', 'createdAt', 'otherManagerId']
    

# class QuarterlyOtherManagerSerializer(serializers.Serializer):
#     parentFilerId = serializers.CharField()
#     childFilerId = serializers.CharField()
#     quarterId = serializers.CharField()
#     number = serializers.IntegerField()
#     createdAt = serializers.DateTimeField()
#     otherManagerId = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return QuarterlyOtherManager.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.parentFilerId = validated_data.get('parentFilerId', instance.parentFilerId)
#         instance.childFilerId = validated_data.get('childFilerId', instance.childFilerId)
#         instance.quarterId = validated_data.get('quarterId', instance.quarterId)
#         instance.number = validated_data.get('number', instance.number)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.otherManagerId = validated_data.get('otherManagerId', instance.otherManagerId)
#         instance.save()
#         return instance


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ['companyId', 'CUSIP', 'securityName', 'securityType', 'ticker', 'titleOfClass', 'createdAt', 'securityId']

# class SecuritySerializer(serializers.Serializer):
#     companyId = serializers.CharField()
#     CUSIP = serializers.IntegerField()
#     securityName = serializers.CharField(max_length=3)
#     securityType = serializers.CharField(max_length=7)
#     ticker = serializers.CharField(max_length=5)
#     titleOfClass = serializers.CharField(max_length=10)
#     createdAt = serializers.DateTimeField()
#     securityId = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Security.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.companyId = validated_data.get('companyId', instance.companyId)
#         instance.CUSIP = validated_data.get('CUSIP', instance.CUSIP)
#         instance.securityName = validated_data.get('securityName', instance.securityName)
#         instance.securityType = validated_data.get('securityType', instance.securityType)
#         instance.ticker = validated_data.get('ticker', instance.ticker)
#         instance.titleOfClass = validated_data.get('titleOfClass', instance.titleOfClass)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.securityId = validated_data.get('securityId', instance.securityId)
#         instance.save()
#         return instance

class QuarterlySecurityHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlySecurityHolding
        fields = ['securityId', 'quarterId', 'value', 'amount', 'holdingType', 'investmentDiscretion', 'sole', 'shared', 'none', 'createdAt', 'quarterlySecurityHoldingId']

# class QuarterlySecurityHoldingSerializer(serializers.Serializer):
#     securityId = serializers.CharField()
#     quarterId = serializers.CharField()
#     value = serializers.IntegerField()
#     amount = serializers.IntegerField()
#     holdingType = serializers.CharField(max_length=3)
#     investmentDiscretion = serializers.CharField(max_length=5)
#     sole = serializers.IntegerField()
#     shared = serializers.IntegerField()
#     none = serializers.IntegerField()
#     createdAt = serializers.DateTimeField()
#     quarterlySecurityHoldingId = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return QuarterlySecurityHolding.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.securityId = validated_data.get('securityId', instance.securityId)
#         instance.quarterId = validated_data.get('quarterId', instance.quarterId)
#         instance.value = validated_data.get('value', instance.value)
#         instance.amount = validated_data.get('amount', instance.amount)
#         instance.holdingType = validated_data.get('holdingType', instance.holdingType)
#         instance.investmentDiscretion = validated_data.get('investmentDiscretion', instance.investmentDiscretion)
#         instance.sole = validated_data.get('sole', instance.sole)
#         instance.shared = validated_data.get('shared', instance.shared)
#         instance.none = validated_data.get('none', instance.none)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.quarterlySecurityHoldingId = validated_data.get('quarterlySecurityHoldingId', instance.quarterlySecurityHoldingId)
#         instance.save()
#         return instance
class QuarterlyOtherManagerDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyOtherManagerDistribution
        fields = ['quarterlyOtherManagerId', 'quarterlySecurityHoldingId', 'createdAt', 'quarterlyOtherManagerDistributionId']

# class QuarterlyOtherManagerDistributionSerializer(serializers.Serializer):
#     quarterlyOtherManagerId = serializers.CharField()
#     quarterlySecurityHoldingId = serializers.CharField()
#     createdAt = serializers.DateTimeField()
#     quarterlyOtherManagerDistributionId = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return QuarterlyOtherManagerDistribution.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.quarterlyOtherManagerId = validated_data.get('quarterlyOtherManagerId', instance.quarterlyOtherManagerId)
#         instance.quarterlySecurityHoldingId = validated_data.get('quarterlySecurityHoldingId', instance.quarterlySecurityHoldingId)
#         instance.createdAt = validated_data.get('createdAt', instance.createdAt)
#         instance.quarterlyOtherManagerDistributionId = validated_data.get('quarterlyOtherManagerDistributionId', instance.quarterlyOtherManagerDistributionId)
#         instance.save()
#         return instance



