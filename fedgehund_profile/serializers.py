from .models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['location', 'occupation', 'company', 'state', 'zip_code', 'phone']

class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	class Meta:
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'profile')


