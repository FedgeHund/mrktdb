from rest_auth.registration.views import RegisterView
from .serializers import MyRegisterSerializer

class NameRegistrationView(RegisterView):
	serializer_class = MyRegisterSerializer