from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.Login, name="login"),
    path("signup/", views.Signup, name="signup"),
    path("logout/", views.Logout, name="logout"),
]
