from .views import ProfileAPI
from django.urls import path

urlpatterns = [
    path('<user_id>/',  ProfileAPI.as_view())
]