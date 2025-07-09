from rest_framework import serializers
from .models import Team


from rest_framework.serializers import ImageField


class TeamSerializer(serializers.ModelSerializer):
    flag = ImageField(max_length=None, use_url=True)

    class Meta:
        model = Team
        fields = ["name", "flag"]
