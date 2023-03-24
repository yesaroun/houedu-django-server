from django.contrib import admin
from .models import Category
from typing import Tuple


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    관리자 페이지에서 Category 모델을 위한 설정
    """

    list_display: Tuple[str] = (
        "id",
        "name",
    )
