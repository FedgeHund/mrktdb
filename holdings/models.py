from django.db import models

class Filer(models.Model):
    name = models.TextField(max_length=80)
    cik = models.TextField(blank=True)
    filer_type = models.TextField(blank=True)
    cusip = models.TextField(max_length=10,blank=True)
    filerId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']

class Quarter(models.Model):
    filerId = models.ForeignKey(Filer, on_delete=models.CASCADE)
    quarter = models.TextField()
    quarterId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']

class Security(models.Model):
    name = models.TextField(blank=True)
    symbol = models.TextField(max_length=7,blank=True)
    titleOfClass = models.TextField(blank=True)
    sector = models.TextField(blank=True)
    securityId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']

class Position(models.Model):
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    quarterId = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='quarter_Id')
    quarterFirstOwned = models.TextField(blank=True)
    investmentDiscretion = models.TextField(blank=True)
    quantity = models.FloatField(blank=True)
    marketValue = models.FloatField(blank=True)
    weightPercent = models.FloatField(blank=True)
    previousWeightPercent = models.FloatField(blank=True)
    estimatedAverageCost = models.FloatField(blank=True)
    lastPrice = models.FloatField(blank=True)
    estimatedProfit = models.FloatField(blank=True)
    ranking = models.FloatField(blank=True)
    changeInShares = models.FloatField(blank=True)
    changeInPositionPercent = models.FloatField(blank=True)
    sourceType = models.TextField(blank=True)
    sourcedOn = models.DateTimeField(blank=True)
    positionType = models.TextField(blank=True) #change this quarter foreign key
    positionId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']



