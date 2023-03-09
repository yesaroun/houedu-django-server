from .models import User, Teacher


from django.contrib import admin

admin.site.register(User)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    """Teacher 관련 admin 패널 세팅"""

    pass
