from rest_framework import serializers
from .models import Individuality

from teams.serializers import TeamSerializer
from players.serializers import PlayerSerializer


class IndividualitySerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    team = TeamSerializer()

    class Meta:
        model = Individuality
        fields = ["id", "description", "player", "team", "video"]
