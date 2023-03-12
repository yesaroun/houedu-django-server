from typing import Optional, Text
from users.models import Teacher, User
from common.models import CommonModel
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _


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


class Review(CommonModel):

    """Reviews를 정의한 모델"""

    class StarChoices(models.IntegerChoices):
        """별점 선택 클래스"""

        ONE_STAR = 1, _("★")
        TWO_STAR = 2, _("★★")
        THREE_STAR = 3, _("★★★")
        FOUR_STAR = 4, _("★★★★")
        FIVE_STAR = 5, _("★★★★★")

    user: Optional[User] = models.ForeignKey(
        "users.User",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="reviews",
    )
    crs: Optional[Course] = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="reviews",
    )
    star: Optional[int] = models.IntegerField(
        blank=True,
        null=True,
        choices=StarChoices.choices,
    )
    content: Text = models.TextField()

    class Meta:
        managed = True
        db_table = "review"

    def __str__(self) -> Text:
        return f"{self.user}의 {self.crs} 리뷰"
