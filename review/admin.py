from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "crs_id", "star", "created_at")


admin.site.register(Review, ReviewAdmin)
