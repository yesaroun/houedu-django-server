from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "tcr_id", "crs_name", "crs_info")


admin.site.register(Course, CourseAdmin)
