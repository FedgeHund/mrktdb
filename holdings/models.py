from django.db import models
from edgar.models import QuarterlyHolding, Security, Filer


class Position(models.Model):
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    quarterId = models.ForeignKey(
        QuarterlyHolding,
        on_delete=models.CASCADE,
        related_name='quarter_Id')
    filerId = models.ForeignKey(
        Filer,
        on_delete=models.CASCADE,
        related_name='filer_id')
    quarter = models.IntegerField(blank=True)
    securityName = models.TextField(blank=True)
    filerName = models.TextField(blank=True)
    cusip = models.TextField(blank=True)
    cik = models.TextField(blank=True)
    ticker = models.TextField(blank=True)
    type1 = models.TextField(blank=True)
    type2 = models.TextField(blank=True)
    quarterFirstOwned = models.ForeignKey(
        QuarterlyHolding,
        on_delete=models.CASCADE,
        related_name='quarterFirstOwned_Id')
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
    positionType = models.TextField(blank=True)
    positionId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)

    class Meta:
        ordering = ['createdAt']
