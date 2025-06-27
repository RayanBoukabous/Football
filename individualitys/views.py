from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import IndividualitySerializer


class IndividualityListView(generics.ListCreateAPIView):
    queryset = Individuality.objects.all()
    print("hey")
    print("hey")
    print("hey")
    print("hey")
    print("hey")
    print("hey")
    serializer_class = IndividualitySerializer


class IndividualityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individuality.objects.all()
    serializer_class = IndividualitySerializer
