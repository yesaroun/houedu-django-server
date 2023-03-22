from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    MyInfo,
    Users,
    # MyCourses,
    MyReviews,
    ChangePassword,
    LogIn,
    LogOut,
    JWTLogin,
    GithubLogIn,
    KakaoLogIn,
)
from typing import List


urlpatterns: List[URLPattern] = [
    path("signup/", Users.as_view()),
    path("myinfo/", MyInfo.as_view()),
    # path("myinfo/mycourses/", MyCourses.as_view()),
    path("myinfo/myreviews/", MyReviews.as_view()),
    path("password/", ChangePassword.as_view()),
    path("login/", LogIn.as_view()),
    path("token-login/", obtain_auth_token),
    path("jwt-login/", JWTLogin.as_view()),
    path("logout/", LogOut.as_view()),
    path("github/", GithubLogIn.as_view()),
    path("kakao/", KakaoLogIn.as_view()),
]
