from rest_auth.registration.views import RegisterView, LoginView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class UserRegistrationView(RegisterView):
	serializer_class = UserRegisterSerializer

class UserLoginView(LoginView):
	serializer_class = UserLoginSerializer

class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)