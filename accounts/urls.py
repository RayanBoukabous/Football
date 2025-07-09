# users/urls.py
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "dashboard/", views.list_matches, name="list_matches"
    ),  # 👈 nom à bien définir ici
    path("", login_page, name="home"),  # racine du site = login.html
]
