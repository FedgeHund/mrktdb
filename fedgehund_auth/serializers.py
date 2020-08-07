from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from fedgehund_profile.models import Profile
from django.contrib.auth.models import User
from fedgehund_profile.serializers import ProfileSerializer

class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }


class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	class Meta:
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'profile')