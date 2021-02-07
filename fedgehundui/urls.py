from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('signup/', views.index),
	path('signin/', views.index),
	path('contactus/', views.index),
]