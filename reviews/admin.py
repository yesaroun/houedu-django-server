from django.contrib import admin
from .models import Review
from typing import Tuple


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    """
    관리자 페이지에서 Review 모델을 위한 설정
    """

    list_display: Tuple[str] = (
        "id",
        "__str__",
        "star",
    )
    list_filter: Tuple[str] = ("star",)
