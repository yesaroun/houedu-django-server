from django.contrib import admin
from django.template.defaulttags import url
from django.urls.resolvers import URLPattern
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from typing import List
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="houedu",
        default_version="1.0.0",
        description="houedu API 문서",
    ),
    public=True,
)


urlpatterns: List[URLPattern] = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path(
        "api/v1/",
        include(
            [
                path("courses/", include("courses.urls")),
                path("reviews/", include("reviews.urls")),
                path("users/", include("users.urls")),
                path(
                    "swagger/schema/",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="swagger-schema",
                ),
            ]
        ),
    ),
    # path("api/v1/courses/", include("courses.urls")),
    # path("api/v1/reviews/", include("reviews.urls")),
    # path("api/v1/users/", include("users.urls")),
]
