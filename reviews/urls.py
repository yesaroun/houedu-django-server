from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns: list[URLPattern] = [
    path("", views.Reviews.as_view()),
    path("<int:pk>/", views.ReviewDetail.as_view()),
]
