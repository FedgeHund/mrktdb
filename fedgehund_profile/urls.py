from django.urls import path

from .views import WatchlistView

app_name = "Company_watchlist"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('company_watchlist/', WatchlistView.as_view()),
]