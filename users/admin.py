from .models import User, Teacher
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """User 관련 admin 패널 세팅"""

    # fields = ("id", "email", "nickname", "is_staff")

    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    """Teacher 관련 admin 패널 세팅"""

    list_display = ("id", "user_id", "tcr_name")
