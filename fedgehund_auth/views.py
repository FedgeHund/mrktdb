from rest_auth.registration.views import RegisterView
from .serializers import UserRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


class UserRegistrationView(RegisterView):
	serializer_class = UserRegisterSerializer


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)