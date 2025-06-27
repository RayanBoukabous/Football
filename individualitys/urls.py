# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path(
        "api/individuality/", IndividualityListView.as_view(), name="Individuality-list"
    ),
    path(
        "api/Individuality/<int:pk>/",
        IndividualityDetailView.as_view(),
        name="Individuality-detail",
    ),
]
