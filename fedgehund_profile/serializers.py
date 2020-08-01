from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'location', 
        			'occupation', 'company', 'state', 'zip_code', 'phone', 'user']