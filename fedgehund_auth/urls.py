from django.urls import path
from .views import NameRegistrationView

urlpatterns = [
    path('', NameRegistrationView.as_view(), name="rest_name_register")
]