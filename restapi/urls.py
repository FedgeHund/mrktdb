from django.urls import path
from restapi import views

urlpatterns = [
    path('restapi/', views.company_list),
    path('restapi/<int:pk>/', views.company_detail),
]
