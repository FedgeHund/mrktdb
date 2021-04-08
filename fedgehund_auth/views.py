from rest_auth.registration.views import RegisterView, LoginView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


class UserRegistrationView(RegisterView):
	serializer_class = UserRegisterSerializer

class UserLoginView(LoginView):
	serializer_class = UserLoginSerializer

class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)