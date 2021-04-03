from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	occupation = models.CharField(max_length=100, null=True, blank=True)
	company = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=200, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	phone = models.CharField(max_length=50, null=True, blank=True)
	zip_code = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return str(self.user)