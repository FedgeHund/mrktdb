from django.db import models

class Company(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    companyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=120)
    typeCo = models.CharField(max_length=1, choices=type)
    code = models.TextField()

    class Meta:
        ordering = ['createdAt']

