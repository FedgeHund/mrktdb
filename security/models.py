from django.db import models
from edgar.models import Security


class Price(models.Model):
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    value = models.FloatField(blank=True)
    quarter = models.IntegerField(blank=True)
    cusip = models.TextField(blank=True)
    name = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)

    class Meta:
        ordering = ['createdAt']
