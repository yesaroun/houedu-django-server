from django.contrib import admin
from .models import Course, Lecture
from typing import Tuple


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    """
    관리자 페이지에서 Course 모델을 위한 설정
    """

    list_display: Tuple[str] = (
        "id",
        "tcr_id",
        "crs_name",
        "thumbnail",
    )
    search_fields: Tuple[str] = ("crs_name",)
    list_display_links: Tuple[str] = ("crs_name",)


@admin.register(Lecture)
class AdminLecture(admin.ModelAdmin):
    """
    관리자 페이지에서 Lecture 모델을 위한 설정
    """

    list_display: Tuple[str] = (
        "id",
        "crs_id",
        "lctr_name",
    )
    search_fields: Tuple[str] = ("lctr_name",)
    list_display_links: Tuple[str] = ("lctr_name",)
