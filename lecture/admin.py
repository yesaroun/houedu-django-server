from django.contrib import admin
from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ("id", "crs_id", "lctr_name", "lctr_info")


admin.site.register(Lecture, LectureAdmin)
