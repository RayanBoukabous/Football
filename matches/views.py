# views.py
from urllib import response
from rest_framework import generics
from .models import Match
from .serializers import MatchSerializer


class MatchListView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response


class MatchDetails(APIView):

    def get(self, request):
        match_id = request.GET.get("match")
        match = get_object_or_404(Match, id=match_id)
        serializer = MatchSerializer(match)
        return Response(serializer.data)
        # return Response(status=200)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.conf import settings


@login_required
def list_matches(request):
    return render(request, "matches/list_matches.html", {"api_url": settings.API_URL})


from django.shortcuts import render, get_object_or_404
from .models import Match


from django.shortcuts import render, get_object_or_404
from .models import Match


def match_details(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, "matches/match_details.html", {"match": match})
