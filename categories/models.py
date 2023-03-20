from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
