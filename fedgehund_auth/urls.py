from django.urls import path, include
from .views import UserRegistrationView, UserLoginView
from .views import UserAPIView, FacebookLogin, GoogleLogin

urlpatterns = [
    path(
        'user/',
        UserAPIView.as_view()),
    path(
        'registration/',
        UserRegistrationView.as_view(),
        name="rest_name_register"),
    path(
        'login/',
        UserLoginView.as_view(),
        name="rest_name_login"),
    path(
        'facebook/',
        FacebookLogin.as_view(),
        name='fb_login'),
    path(
        'google/',
        GoogleLogin.as_view(),
        name='google_login'),
    path(
        '',
        include('rest_auth.urls')),
]
