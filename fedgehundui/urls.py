from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index),
	path('signup/', views.index),
	path('signin/', views.index),
	path('404/', views.index),
	re_path(r'^.*$', views.index),
]