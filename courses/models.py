from django.db import models
from django.db.models import QuerySet
from users.models import Teacher, User
from common.models import CommonModel
from typing import Optional, Text


class Course(models.Model):
    """
    Course를 나타내는 모델
    """

    tcr: Optional[Teacher] = models.ForeignKey(
        "users.Teacher",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="courses",
        help_text="코스에 연간된 강사, 없는 경우 Null",
    )
    crs_name: Text = models.CharField(
        max_length=50,
        help_text="코스 이름",
    )
    crs_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="코스에 대한 설명, 없는 경우 Null",
    )
    thumbnail: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="코스의 썸네일 이미지 URL, 없는 경우 Null",
    )
    price: int = models.PositiveIntegerField(
        default=0,
        help_text="코스의 가격",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="courses",
        help_text="코스의 카테고리",
    )
    crs_goal: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="코스 목표, 없는 경우 Null",
    )
    crs_content: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="코스 콘텐츠에 대한 정보, 없는 경우 Null",
    )

    class Meta:
        managed: bool = True
        db_table: str = "course"

    def __str__(self) -> Text:
        """
        코스 이름 반환

        :return: 코스 이름
        """
        return self.crs_name

    def count_reviews(self) -> int:
        """
        리뷰 수 세기

        :return: 리뷰 수
        """
        count: int = self.reviews.count()
        return count

    def rating(self) -> float:
        """
        코스의 평점 평균 계산

        :return: 코스 평균 평점
        """
        count = self.count_reviews()
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
    """
    강의(세부 강의)를 나타내는 모델
    """

    crs: Optional[Course] = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="lectures",
        help_text="세부 강의를 감싸는 Course",
    )
    lctr_name: Text = models.CharField(
        max_length=50,
        help_text="강의 명",
    )
    lctr_source: Text = models.TextField(
        help_text="강의 영상 소스 코드 URL",
    )
    lctr_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="강의에 대한 정보, 없는 경우 Null",
    )

    class Meta:
        managed: bool = True
        db_table: str = "lecture"

    def __str__(self) -> Text:
        """
        강의(세부 강의) 이름 반환

        :return: 강의(세부 강의) 이름
        """
        return self.lctr_name
