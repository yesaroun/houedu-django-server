from django.urls import path
from django.urls.resolvers import URLPattern
from .views import Main


urlpatterns: list[URLPattern] = [
    path("", Main.as_view()),
]
