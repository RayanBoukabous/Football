# urls.py
from django.urls import path
from .views import MatchListView, MatchDetailView, MatchDetails

urlpatterns = [
    path("api/matches/", MatchListView.as_view(), name="match-list"),
    path("api/matches/<int:pk>/", MatchDetailView.as_view(), name="matches"),
    path("api/match_details", MatchDetails.as_view(), name="match-detail"),
]
