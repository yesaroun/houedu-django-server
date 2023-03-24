from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, UserCourse, VideoWatches
from typing import Tuple


@admin.register(User)
class UserAdmin(UserAdmin):
    """
    관리자 페이지에서 User 모델을 위한 설정
    """

    fieldsets: Tuple[Tuple[str, dict]] = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "nickname",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display: Tuple[str] = (
        "username",
        "email",
        "nickname",
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    관리자 페이지에서 Teacher 모델을 위한 설정
    """

    list_display: Tuple[str] = (
        "id",
        "user_id",
        "tcr_name",
    )
    list_display_links: Tuple[str] = (
        "user_id",
        "tcr_name",
    )


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    """
    관리자 페이지에서 유저의 수강 과목(UserCourse) 모델을 위한 설정
    """

    list_display: Tuple[str] = (
        "id",
        "user_id",
        "course_id",
    )
    list_display_links: Tuple[str] = (
        "id",
        "user_id",
        "course_id",
    )


@admin.register(VideoWatches)
class VideoWatchesAdmin(admin.ModelAdmin):
    """
    관리자 페이지에서 수강 기록(VideoWatches) 모델을 위한 설정
    """

    pass
