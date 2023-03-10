from django.contrib import admin
from .models import Course, Lecture


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):

    """course 관련 admin 패널 세팅"""

    list_display: tuple = "id", "tcr_id", "crs_name", "thumbnail"
    search_fields: tuple = ("crs_name",)
    list_display_links: tuple = ("crs_name",)


@admin.register(Lecture)
class AdminLecture(admin.ModelAdmin):

    """lecture 관련 admin 패널 세팅"""

    list_display: tuple = "id", "crs_id", "lctr_name"
    search_fields: tuple = ("lctr_name",)
    list_display_links: tuple = ("lctr_name",)
