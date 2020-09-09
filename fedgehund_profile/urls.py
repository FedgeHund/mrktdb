from django.urls import path

from .views import WatchlistView
from .views import ProfileView

app_name = "Company_watchlist"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('watchlist/', WatchlistView.as_view()),
    path('fields/', ProfileView.as_view()),
]