from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    MyInfo,
    Users,
    MyReviews,
    MyReviewsDetail,
    ChangePassword,
    LogIn,
    LogOut,
    GithubLogIn,
    KakaoLogIn,
)
from typing import List


urlpatterns: List[URLPattern] = [
    path("signup/", Users.as_view()),
    path(
        "myinfo/",
        include(
            [
                path("", MyInfo.as_view()),
                path("myreviews/", MyReviews.as_view()),
                path("myreviews/<int:pk>/", MyReviewsDetail.as_view()),
            ]
        ),
    ),
    path("password/", ChangePassword.as_view()),
    path("login/", LogIn.as_view()),
    path("logout/", LogOut.as_view()),
    path("github/", GithubLogIn.as_view()),
    path("kakao/", KakaoLogIn.as_view()),
]
