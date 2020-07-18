from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=80)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    companyId = models.AutoField(primary_key=True)
    address = models.TextField(max_length=120)
    companyType = models.CharField(max_length=19, default=None)

    class Meta:
        ordering = ['createdAt']

class Filer(models.Model):
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    fileNumber = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    filerId = models.AutoField(primary_key=True)
    fileType = models.CharField(max_length=4)

    class Meta:
        ordering = ['companyId']

class QuarterlyHolding(models.Model):
    filerId = models.ForeignKey(Filer, on_delete=models.CASCADE)
    quarter = models.IntegerField()
    filingType = models.CharField(max_length=3)
    filedOn = models.IntegerField()
    acceptedAt = models.IntegerField()
    valueTotal = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    quarterId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['createdAt']

class QuarterlyOtherManager(models.Model):
    parentFilerId = models.ForeignKey(Filer, on_delete=models.CASCADE, related_name='parent_Filer')
    childFilerId = models.ForeignKey(Filer, on_delete=models.CASCADE, related_name='child_Filer')
    quarterId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    number = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    otherManagerId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['quarterId']


class Security(models.Model):
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    CUSIP = models.IntegerField()
    securityName = models.CharField(max_length=40)
    securityType = models.CharField(max_length=7)
    ticker = models.CharField(max_length=5)
    titleOfClass = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    securityId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['ticker']

class QuarterlySecurityHolding(models.Model):
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    quarterId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    value = models.IntegerField()
    amount = models.IntegerField()
    holdingType = models.CharField(max_length=3)
    investmentDiscretion = models.CharField(max_length=5)
    sole = models.IntegerField()
    shared = models.IntegerField()
    none = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    quarterlySecurityHoldingId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['quarterId']

class QuarterlyOtherManagerDistribution(models.Model):
    quarterlyOtherManagerId = models.ForeignKey(QuarterlyOtherManager, on_delete=models.CASCADE)
    quarterlySecurityHoldingId = models.ForeignKey(QuarterlySecurityHolding, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None)
    deletedAt = models.DateTimeField(default=None)
    quarterlyOtherManagerDistributionId = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['createdAt']


