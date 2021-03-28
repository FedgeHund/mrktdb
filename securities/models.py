from django.db import models

class Security(models.Model):
    name = models.TextField(blank=True)
    titleOfClass = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']

class Quarter(models.Model):
    securityId = models.ForeignKey(Security, on_delete=models.CASCADE)
    value = models.FloatField(blank=True)
    quarter = models.TextField(blank=True)
    quarterId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']