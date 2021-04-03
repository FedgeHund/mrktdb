from .models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['occupation', 'company', 'city', 'state', 'phone', 'zip_code']