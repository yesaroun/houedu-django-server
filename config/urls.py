from django.contrib import admin
from django.urls import path, include
import courses

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls")),
]
