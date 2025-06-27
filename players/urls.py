from django.urls import path
from . import views

urlpatterns = [
    path("player/<int:player_id>/pdf/", views.player_profile, name="player_profile"),
]
