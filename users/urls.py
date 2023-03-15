from django.urls import path
from django.urls.resolvers import URLPattern
from .views import MyInfo, User, ChangePwd
from typing import List


urlpatterns: List[URLPattern] = [
    path("", User.as_view()),
    path("myinfo/", MyInfo.as_view()),
    path("password/", ChangePwd.as_view()),
]
