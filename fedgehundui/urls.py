from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index),
	path('signup/', views.index),
	path('signin/', views.index),
	path('contactus/', views.index),
	path('faq/', views.index),
	path('stock/<securityName>/', views.index),
	path('filer/<cik>/', views.index),
	path('404/', views.index),
	path('500/', views.index),
	re_path(r'^.*$', views.index),
]