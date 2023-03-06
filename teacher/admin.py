from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "tcr_name")


admin.site.register(Teacher, TeacherAdmin)
