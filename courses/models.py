from django.db import models
from django.db.models import QuerySet
from users.models import Teacher, User
from common.models import CommonModel
from typing import Optional, Text


class Course(models.Model):

    """Courses를 정의한 모델"""

    tcr: Optional[Teacher] = models.ForeignKey(
        "users.Teacher",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="courses",
    )
    crs_name: Text = models.CharField(
        max_length=50,
    )
    crs_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
    )
    thumbnail: Optional[Text] = models.TextField(
        blank=True,
        null=True,
    )
    prcie: int = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        managed = True
        db_table = "course"

    def __str__(self) -> Text:
        return self.crs_name

    def rating(self) -> float:
        count: int = self.reviews.count()
        if count == 0:
            return 0.0
        else:
            total_rating: int = 0
            for review in self.reviews.all().values(
                "star"
            ):  # type: QuerySet[dict[str, int]]
                total_rating += review["star"]
            return round(total_rating / count, 2)


class Lecture(models.Model):

    """Lectures를 정의한 모델"""

    crs: Optional[Course] = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="lectures",
    )
    lctr_name: Text = models.CharField(
        max_length=50,
    )
    lctr_source: Text = models.TextField()
    lctr_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "lecture"

    def __str__(self) -> Text:
        return self.lctr_name
