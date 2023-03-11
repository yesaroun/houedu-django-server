from django.db import models


class CommonModel(models.Model):

    """공통으로 사용할 생성, 수정 필드 정의 모델"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True  # 추상화
