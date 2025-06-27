from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    flag = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Team
        fields = ["name", "flag"]
