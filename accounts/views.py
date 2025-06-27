# users/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
import json
from .forms import LoginForm


@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {
                "success": True,
                "redirect": "file:///Users/rayan/Documents/football_software/front_end/mainTemplate/list_matches.html",
            }
        )

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
            return JsonResponse({"success": True})
        else:
            return JsonResponse(
                {
                    "success": False,
                    "error": "Nom d'utilisateur ou mot de passe invalide",
                },
                status=401,
            )

    # Fallback pour GET ou autre méthode
    return render(request, "users/login.html", {"form": LoginForm()})


def logout_view(request):
    logout(request)
    return redirect("login")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "users/list_matches.html", {"user": request.user})
