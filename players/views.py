from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Player


def player_profile(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, "player_profile.html", {"player": player})
