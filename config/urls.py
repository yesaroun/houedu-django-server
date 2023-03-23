from django.contrib import admin
from django.template.defaulttags import url
from django.urls.resolvers import URLPattern
from django.urls import path, include
from django.views.generic import TemplateView
from typing import List


urlpatterns: List[URLPattern] = [
    # url(r"^$", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
    # path("api/v1/", include("main.urls")),
    path("api/v1/courses/", include("courses.urls")),
    path("api/v1/reviews/", include("reviews.urls")),
    path("api/v1/users/", include("users.urls")),
]
