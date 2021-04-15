from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from holdings import views

urlpatterns = [
    path('positions/', views.PositionList.as_view()),
    path('positions/<int:pk>/', views.PositionDetail.as_view()),
    path('latestquarterpositions/', views.LatestQuarterPositionList.as_view()),
    path('ownershiphistory/', views.OwnershipHistory.as_view()),
    path('allownedsecurities/', views.AllOwnedSecurities.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)