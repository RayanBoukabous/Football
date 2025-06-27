from rest_framework import serializers

from categorys.serializers import CategorySerializer
from countrys.serializers import *
from teams.serializers import *
from analyses.serializer import *
from individualitys.serializers import *
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = CountrySerializer()
    first = TeamSerializer()
    second = TeamSerializer()
    individualities = serializers.SerializerMethodField()
    analyses = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            "id",
            "category",
            "match_date",
            "location",
            "video",
            "first",
            "second",
            "finale_result",
            "individualities",
            "analyses",
        ]

    def get_individualities(self, obj):
        individualities = Individuality.objects.filter(match=obj)
        return IndividualitySerializer(individualities, many=True).data

    def get_analyses(self, obj):
        analyses = Analyse.objects.filter(match=obj)
        return AnalyseSerializer(analyses, many=True).data
