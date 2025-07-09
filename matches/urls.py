# urls.py
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("api/matches/", MatchListView.as_view(), name="match-list"),
    path("api/matches/<int:pk>/", MatchDetailView.as_view(), name="matches"),
    path("api/match_details", MatchDetails.as_view(), name="match-detail"),
    path("list/", list_matches, name="list_matches"),
    path("match/<int:match_id>/", views.match_details, name="match_details"),
]
