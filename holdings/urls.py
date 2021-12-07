from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from holdings import views

urlpatterns = [
    path(
        'positions/',
        views.PositionList.as_view()),
    path(
        'positions/<int:pk>/',
        views.PositionDetail.as_view()),
    path(
        'latestquarterbiggestholdings/',
        views.LatestQuarterBiggestHoldings.as_view()),
    path(
        'latestquartertopsells/',
        views.LatestQuarterTopSells.as_view()),
    path(
        'latestquartertopbuys/',
        views.LatestQuarterTopBuys.as_view()),
    path(
        'ownershiphistory/',
        views.OwnershipHistory.as_view()),
    path(
        'allownedsecurities/',
        views.AllOwnedSecurities.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
