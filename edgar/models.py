from django.db import models

class Company(models.Model):
    COMPANY_TYPES = (
        ('HF', 'Hedge Fund'),
        ('IA', 'Investment Advisor'),
        ('HC', 'Holdings Company'),
    )
    name = models.TextField(max_length=80)
    cik = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    companyId = models.AutoField(primary_key=True)
    address = models.TextField(max_length=120,blank=True)
    companyType = models.CharField(max_length=2, choices=COMPANY_TYPES, default=None)

    class Meta:
        ordering = ['createdAt']

class Filer(models.Model):
    FILE_TYPES = (
        ('13F', '13F'),
        ('13G', '13G'),
        ('13D', '13D'),
    )
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True)
    fileNumber = models.CharField(max_length=10,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    filerId = models.AutoField(primary_key=True)
    fileType = models.CharField(max_length=3, choices=FILE_TYPES,blank=True)

    class Meta:
        ordering = ['companyId']

class QuarterlyHolding(models.Model):
    FILING_TYPES = (
        ('CR', 'Combined Report'),
        ('CRA', 'Combined Report Amendment'),
        ('NT', 'Notice'),
        ('NTA', 'Notice Amendment'),
        ('HR', 'Holdings Report'),
        ('HRA', 'Holdings Report Amendment'),
    )
    filerId = models.ForeignKey(Filer, on_delete=models.CASCADE)
    quarter = models.TextField()
    filingType = models.CharField(max_length=3, choices=FILING_TYPES)
    filedOn = models.DateTimeField(blank=True)
    acceptedAt = models.DateTimeField(blank=True)
    totalValue = models.FloatField()
    totalEntry = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(  blank=True)
    quarterlyHoldingId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['createdAt']

class QuarterlyOtherManager(models.Model):
    parentFilerId = models.ForeignKey(Filer, on_delete=models.CASCADE, related_name='parent_filer',blank=True)
    childFilerId = models.ForeignKey(Filer, on_delete=models.CASCADE, related_name='child_filer',blank=True)
    quarterlyHoldingId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    number = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    otherManagerId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['quarterlyHoldingId']


class Security(models.Model):
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True)
    cusip = models.TextField()
    securityName = models.TextField(blank=True)
    securityType = models.TextField(blank=True)
    ticker = models.CharField(max_length=5,blank=True)
    titleOfClass = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    securityId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['ticker']

class QuarterlySecurityHolding(models.Model):
    
    DISCRETION_TYPES = (
        ('SOLE', 'SOLE'),
        ('DFND', 'DFND'),
        ('OTHR', 'OTHER'),
    )
    uin=models.TextField()
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    quarterlyHoldingId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    marketvalue = models.FloatField()
    quantity = models.FloatField()
    holdingType = models.TextField()
    investmentDiscretion = models.CharField(max_length=4, choices=DISCRETION_TYPES)
    sole = models.IntegerField()
    shared = models.IntegerField()
    none = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    quarterlySecurityHoldingId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['quarterlyHoldingId']

class QuarterlyOtherManagerDistribution(models.Model):
    quarterlyOtherManagerId = models.ForeignKey(QuarterlyOtherManager, on_delete=models.CASCADE)
    quarterlySecurityHoldingId = models.ForeignKey(QuarterlySecurityHolding, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    quarterlyOtherManagerDistributionId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['createdAt']

class FailsToDeliver(models.Model):
    settlementDate = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    cusip = models.TextField()
    ticker = models.CharField(max_length=7)
    quantity = models.IntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['createdAt']

class CikCusipMapping(models.Model):
    year = models.IntegerField()
    cik = models.IntegerField()
    sec_name = models.TextField()
    cusip = models.TextField()
    cusip6 = models.TextField()
    cikCusipMappingId = models.TextField()

    class Meta:
        ordering = ['year']
