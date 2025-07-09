import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import LoginForm
from django.conf import settings


@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"success": True, "redirect": reverse("list_matches")})

    if (
        request.method == "POST"
        and request.headers.get("Content-Type") == "application/json"
    ):
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse(
                {
                    "success": True,
                    "redirect": reverse("list_matches"),  # ✅ c'est le bon nom ici
                }
            )
        else:
            return JsonResponse(
                {
                    "success": False,
                    "error": "Nom d'utilisateur ou mot de passe invalide",
                },
                status=401,
            )

    return render(request, "accounts/login.html", {"form": LoginForm()})


def logout_view(request):
    logout(request)
    return redirect("login")


def login_page(request):
    return render(request, "accounts/login.html", {"api_url": settings.API_URL})


def list_matches(request):
    if not request.user.is_authenticated:
        return redirect("login")  # ou 'accounts:login' si espace de noms
    return render(request, "matches/list_matches.html", {"user": request.user})
