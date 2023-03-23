from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home


urlpatterns: list[URLPattern] = [
    # path("", Main.as_view()),
    path("", home),
]
