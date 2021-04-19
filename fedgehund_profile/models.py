from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from edgar.models import Company, Security


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile')
    occupation = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    companies_watchlist = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.CASCADE)
    stock_watchlist = models.ForeignKey(
        Security, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
