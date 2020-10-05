from django.db import models

class Company(models.Model):
    COMPANY_TYPES = (
        ('HF', 'Hedge Fund'),
        ('IA', 'Investment Advisor'),
        ('HC', 'Holdings Company'),
    )
    name = models.TextField(max_length=80)
    cik = models.IntegerField(default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    companyId = models.AutoField(primary_key=True)
    address = models.TextField(max_length=120)
    companyType = models.CharField(max_length=2, choices=COMPANY_TYPES, default=None)

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

class Security(models.Model):
    companyId = models.IntegerField(default=None)
    cusip = models.TextField()
    securityName = models.TextField()
    securityType = models.TextField()
    ticker = models.CharField(max_length=5)
    titleOfClass = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    securityId = models.AutoField(primary_key=True)
    cikCusipMappingId = models.TextField(default=None, blank=True)

    class Meta:
        ordering = ['ticker']
        verbose_name_plural = "Securities"

class Filer(models.Model):
    FILE_TYPES = (
        ('13F', '13F'),
        ('13G', '13G'),
        ('13D', '13D'),
    )
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    fileNumber = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    filerId = models.AutoField(primary_key=True)
    fileType = models.CharField(max_length=3, choices=FILE_TYPES)

    class Meta:
        ordering = ['companyId']

class QuarterlyHolding(models.Model):
    FILING_TYPES = (
        ('CR', 'Combined Report'),
        ('NT', 'Notice'),
        ('HR', 'Holdings Report'),
    )
    filerId = models.ForeignKey(Filer, on_delete=models.CASCADE)
    quarter = models.IntegerField()
    filingType = models.CharField(max_length=2, choices=FILING_TYPES)
    filedOn = models.DateTimeField(default=None, blank=True)
    acceptedAt = models.DateTimeField(default=None, blank=True)
    totalValue = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    quarterlyHoldingId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['createdAt']

class QuarterlyOtherManager(models.Model):
    parentFilerId = models.ForeignKey(Filer, on_delete=models.CASCADE, related_name='parent_filer')
    childFilerId = models.ForeignKey(Filer, on_delete=models.CASCADE, related_name='child_filer')
    quarterlyHoldingId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    number = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    otherManagerId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['quarterlyHoldingId']

class QuarterlySecurityHolding(models.Model):
    HOLDING_TYPES = (
        ('SHR', 'SH'),
        ('PRN', 'PRN'),
        ('PUT', 'PUT'),
        ('CAL', 'CALL'),
    )
    DISCRETION_TYPES = (
        ('SOLE', 'SOLE'),
        ('DFND', 'DFND'),
        ('OTHR', 'OTHER'),
    )
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    quarterlyHoldingId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    value = models.FloatField()
    amount = models.FloatField()
    holdingType = models.CharField(max_length=3, choices=HOLDING_TYPES)
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