from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from filer import views

urlpatterns = [
    path(
        'quarterlyfiler/',
        views.QuarterlyFilerViewList.as_view()),
    path(
        'quarterlyfiler/<int:pk>/',
        views.QuarterlyFilerViewDetail.as_view()),
    path(
        'summarytable13f/',
        views.LatestQuarterData13FSummaryTable.as_view()),
    path(
        'quarterlymarketvaluechart/',
        views.QuarterlyMarketValueChart.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
