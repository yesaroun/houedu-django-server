from django.urls import path
from django.urls.resolvers import URLPattern
from .views import MyInfo, User, ChangePassword, LogIn, LogOut
from typing import List


urlpatterns: List[URLPattern] = [
    path("", User.as_view()),
    path("myinfo/", MyInfo.as_view()),
    path("password/", ChangePassword.as_view()),
    path("login/", LogIn.as_view()),
    path("logout/", LogOut.as_view()),
]
