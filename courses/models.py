import datetime
from users.models import Teacher, User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):

    """Courses를 정의한 모델"""

    tcr: Teacher = models.ForeignKey(
        "users.Teacher",
        models.DO_NOTHING,
        blank=True,
        null=True,
    )
    crs_name: str = models.CharField(
        max_length=50,
    )
    crs_info: str = models.TextField(
        blank=True,
        null=True,
    )
    thumbnail: str = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "course"


class Lecture(models.Model):

    """Lectures를 정의한 모델"""

    crs: Course = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
    )
    lctr_name: str = models.CharField(
        max_length=50,
    )
    lctr_source: str = models.TextField()
    lctr_info: str = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "lecture"


class Review(models.Model):

    """Reviews를 정의한 모델"""

    class StarChoices(models.IntegerChoices):
        """별점 선택 클래스"""

        ONE_STAR = 1, _("★")
        TWO_STAR = 2, _("★★")
        THREE_STAR = 3, _("★★★")
        FOUR_STAR = 4, _("★★★★")
        FIVE_STAR = 5, _("★★★★★")

    user: User = models.ForeignKey(
        "users.User",
        models.DO_NOTHING,
        blank=True,
        null=True,
    )
    crs: Course = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
    )
    star: int = models.IntegerField(
        blank=True,
        null=True,
        choices=StarChoices.choices,
    )
    content: str = models.TextField()
    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at: datetime = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "review"
