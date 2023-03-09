from django.contrib import admin
from .models import User, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """User 관련 admin 패널 세팅"""

    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    """Teacher 관련 admin 패널 세팅"""

    pass
