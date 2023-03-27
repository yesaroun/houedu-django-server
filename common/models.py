from django.db import models
from datetime import datetime


class CommonModel(models.Model):
    """
    생성 및 업데이트 날짜와 시간을 나타내는 Common 필드
    """

    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        help_text="생성 날짜 및 시간",
    )
    updated_at: datetime = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        help_text="수정 날짜 및 시간",
    )

    class Meta:
        abstract: bool = True  # 추상화
