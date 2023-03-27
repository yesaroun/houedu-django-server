from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import Optional, Text
from users.models import User
from courses.models import Course
from common.models import CommonModel


class Review(CommonModel):
    """
    코스의 리뷰를 나타내는 모델
    """

    class StarChoices(models.IntegerChoices):
        """
        리뷰에서 별점을 정의하는 클래스
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
        help_text="리뷰를 작성한 유저, 없으면 Null",
    )
    crs: Optional[Course] = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="reviews",
        help_text="리뷰가 작성된 코스",
    )
    star: Optional[int] = models.IntegerField(
        blank=True,
        null=True,
        choices=StarChoices.choices,
        help_text="리뷰 별점, 없으면 Null",
    )
    content: Text = models.TextField(
        help_text="리뷰 내용",
    )

    class Meta:
        managed: bool = True
        db_table: str = "review"

    def __str__(self) -> Text:
        """
        리뷰의 문자열 표현 반환

        :return: 리뷰 문자열
        """
        return f"{self.user}의 {self.crs} 리뷰"
