from django.db import models

class Company(models.Model):
    COMPANY_TYPES = (
        ('F', 'Hedge Fund'),
        ('I', 'Investment Advisor'),
        ('H', 'Holdings Company'),
    )
    name = models.TextField(max_length=80)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    companyId = models.AutoField(primary_key=True)
    address = models.TextField(max_length=120)
    companyType = models.CharField(max_length=1, choices=COMPANY_TYPES, default=None)

    class Meta:
        ordering = ['createdAt']

class Filer(models.Model):
    FILE_TYPES = (
        ('F', '13F'),
        ('G', '13G'),
        ('D', '13D'),
    )
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    fileNumber = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    filerId = models.AutoField(primary_key=True)
    fileType = models.CharField(max_length=1, choices=FILE_TYPES)

    class Meta:
        ordering = ['companyId']

class QuarterlyHolding(models.Model):
    FILING_TYPES = (
        ('C', 'Combined Report'),
        ('N', 'Notice'),
        ('H', 'Holdings Report'),
    )
    filerId = models.ForeignKey(Filer, on_delete=models.CASCADE)
    quarter = models.IntegerField()
    filingType = models.CharField(max_length=1, choices=FILING_TYPES)
    filedOn = models.IntegerField()
    acceptedAt = models.IntegerField()
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


class Security(models.Model):
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    cusip = models.TextField()
    securityName = models.TextField()
    securityType = models.TextField()
    ticker = models.CharField(max_length=5)
    titleOfClass = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    securityId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['ticker']

class QuarterlySecurityHolding(models.Model):
    HOLDING_TYPES = (
        ('S', 'SH'),
        ('P', 'PRN'),
        ('U', 'PUT'),
        ('C', 'CALL'),
    )
    DISCRETION_TYPES = (
        ('S', 'SOLE'),
        ('D', 'DFND'),
        ('O', 'OTHER'),
    )
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    quarterlyHoldingId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    value = models.FloatField()
    amount = models.FloatField()
    holdingType = models.CharField(max_length=1, choices=HOLDING_TYPES)
    investmentDiscretion = models.CharField(max_length=5)
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


