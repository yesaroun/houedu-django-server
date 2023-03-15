from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.urls import path, include
from typing import List


urlpatterns: List[URLPattern] = [
    path("admin/", admin.site.urls),
    path("/", include("main.urls")),
    path("api/v1/courses/", include("courses.urls")),
    path("api/v1/reviews/", include("reviews.urls")),
    path("api/v1/users/", include("users.urls")),
]
