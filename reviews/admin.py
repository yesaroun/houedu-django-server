from django.contrib import admin
from .models import Review
from typing import Tuple


@admin.register(Review)
class AdminReview(admin.ModelAdmin):

    """review 관련 admin 패널 세팅"""

    list_display: Tuple[str, ...] = (
        "id",
        "__str__",
        "star",
    )
    list_filter: Tuple[str, ...] = ("star",)
