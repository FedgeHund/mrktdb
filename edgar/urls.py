from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from edgar import views

urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<cik>/', views.CompanyDetail.as_view()),
    path('filer/', views.FilerList.as_view()),
    path('filer/<int:pk>/', views.FilerDetail.as_view()),
    path('quarterlyholding/', views.QuarterlyHoldingList.as_view()),
    path('quarterlyholding/<int:pk>/', views.QuarterlyHoldingDetail.as_view()),
    path('security/', views.SecurityList.as_view()),
    path('security/<ticker>/', views.SecurityDetail.as_view()),
    path('quarterlyothermanager/', views.QuarterlyOtherManagerList.as_view()),
    path('quarterlyothermanager/<int:pk>/', views.QuarterlyOtherManagerDetail.as_view()),
    path('quarterlysecurityholding/', views.QuarterlySecurityHoldingList.as_view()),
    path('quarterlysecurityholding/<int:pk>/', views.QuarterlySecurityHoldingDetail.as_view()),
    path('quarterlyotherManagerdistribution/', views.QuarterlyOtherManagerDistributionList.as_view()),
    path('quarterlyotherManagerdistribution/<int:pk>/', views.QuarterlyOtherManagerDistributionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)