```python
from django.db import models
from django.db.models import QuerySet
from users.models import Teacher, User
from common.models import CommonModel
from typing import Optional, Text


class Course(models.Model):
    """
    Model representing a Course.
    """

    tcr: Optional[Teacher] = models.ForeignKey(
        "users.Teacher",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="courses",
        help_text="The teacher associated with the course, if any.",
    )
    crs_name: Text = models.CharField(
        max_length=50, help_text="The name of the course."
    )
    crs_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information about the course, if any.",
    )
    thumbnail: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="The thumbnail image URL for the course, if any.",
    )
    price: int = models.PositiveIntegerField(
        default=0,
        help_text="The price of the course.",
    )

    class Meta:
        managed: bool = True
        db_table = "course"
```
이 django python 코드의 문서화와 typhinting 적용해줘

