from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, UserCourse, VideoWatches


@admin.register(User)
class UserAdmin(UserAdmin):

    """User 관련 admin 패널 세팅"""

    fieldsets: tuple = (
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

    list_display: tuple = (
        "username",
        "email",
        "nickname",
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    """Teacher 관련 admin 패널 세팅"""

    list_display: tuple = "id", "user_id", "tcr_name"
    list_display_links: tuple = "user_id", "tcr_name"


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):

    """유저의 수강 과목 관련 admin 패널 세팅"""

    pass


@admin.register(VideoWatches)
class VideoWatchesAdmin(admin.ModelAdmin):

    """수강 기록 관련 admin 패널 세팅"""

    pass
