from django.db import models
from datetime import datetime


class CommonModel(models.Model):
    """
    Model representing common fields for created and updated date and time.
    """

    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the object was created.",
    )
    updated_at: datetime = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        help_text="The date and time the objec was last updated.",
    )

    class Meta:
        abstract = True  # 추상화
