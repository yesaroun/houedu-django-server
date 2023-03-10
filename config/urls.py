from django.contrib import admin
from django.urls import path, include

# import courses

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/courses/", include("courses.urls")),
    path("api/v1/users/", include("users.urls")),
]
