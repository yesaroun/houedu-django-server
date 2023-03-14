from django.urls import path
from .views import Main


urlpatterns: list = [
    path("", Main.as_view()),
]
