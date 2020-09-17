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

    def __init__(self, *args, **kwargs):
        super(RegisterSerializer, self).__init__(*args, **kwargs)
        self.fields["first_name"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["last_name"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["email"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["password1"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["password2"].error_messages["blank"] = u"Passwords do not match"

class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	class Meta:
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'profile')