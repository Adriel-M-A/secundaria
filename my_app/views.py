from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError


@login_required(login_url="login")
def home(request):
    return render(request, "app/home.html")


def Signup(request):
    if request.method == "GET":
        print("hola mundo nose 1")
        return render(request, "registration/signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "registration/signup.html",
                    {"form": UserCreationForm, "error": "Username already exists."},
                )

        return render(
            request,
            "registration/signup.html",
            {"form": UserCreationForm, "error": "Passwords did not match."},
        )


def Login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("password")

        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        # falta el else en caso de ingresar mal

    return render(request, "registration/login.html")


def Logout(request):
    logout(request)
    return redirect("login")
