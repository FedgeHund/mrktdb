from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from fedgehund_profile.models import Profile
from django.contrib.auth.models import User
from fedgehund_profile.serializers import ProfileSerializer
# file deepcode ignore E1003:

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
# file deepcode ignore super~first~argument~should~be~the~enclosing~class: <RegisterSerializer is the parent class from which the fields are being inherited>
    def __init__(self, *args, **kwargs):
	#  deepcode ignore E1003: <comment the reason here>
        super(RegisterSerializer, self).__init__(*args, **kwargs)
        self.fields["first_name"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["last_name"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["email"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["password1"].error_messages["blank"] = u"All fields on this page are required"
        self.fields["password2"].error_messages["blank"] = u"Passwords do not match"


class UserLoginSerializer(LoginSerializer):
    email = serializers.EmailField(required=True)

    def __init__(self, *args, **kwargs):
	#  deepcode ignore E1003: <comment the reason here>
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.fields["email"].error_messages["invalid"] = u"Enter a valid  address"
        self.fields["email"].error_messages["blank"] = u"Enter a valid email address"
        self.fields["email"].error_messages["required"] = u"Unable to login with the provided credentials"
        self.fields["password"].error_messages["blank"] = u"Enter your password"
        self.fields["password"].error_messages["required"] = u"Enter your password"
        self.fields["password"].error_messages["invalid"] = u"Unable to login with the provided credentials"


class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	class Meta:
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'profile')
