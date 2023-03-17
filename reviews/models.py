from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import Optional, Text
from users.models import User
from courses.models import Course
from common.models import CommonModel


class Review(CommonModel):
    """
    Model representing a Review for a course.
    """

    class StarChoices(models.IntegerChoices):
        """
        Class to define available star choices for the review.
        """

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
        managed: bool = True
        db_table: str = "review"

    def __str__(self) -> Text:
        return f"{self.user}의 {self.crs} 리뷰"
