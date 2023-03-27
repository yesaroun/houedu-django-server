from django.db import models
from common.models import CommonModel
from typing import Text


class Category(CommonModel):
    """
    카테고리를 나타내는 모델
    """

    name: Text = models.CharField(
        max_length=50,
        help_text="카테고리 명",
    )

    def __str__(self) -> str:
        """
        카테고리 이름 반환

        :return: 카테고리 이름
        """
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
