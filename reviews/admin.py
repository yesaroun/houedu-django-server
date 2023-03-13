from django.contrib import admin
from .models import Review


@admin.register(Review)
class AdminReview(admin.ModelAdmin):

    """review 관련 admin 패널 세팅"""

    list_display: tuple = "id", "__str__", "star"
    list_filter: tuple = ("star",)
