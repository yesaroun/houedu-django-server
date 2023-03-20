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
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="courses",
        help_text="The category of the course.",
    )

    class Meta:
        managed: bool = True
        db_table: str = "course"

    def __str__(self) -> Text:
        """
        Return the name of the course.

        :return: A string represeting the name of the course.
        """
        return self.crs_name

    def rating(self) -> float:
        """
        Calculate and return the average rating for the course.

        :return: A float representing the average rating for the course.
        """
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
    """
    Model representing a Lecture.
    """

    crs: Optional[Course] = models.ForeignKey(
        Course,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="lectures",
        help_text="The course associated with the lecture.",
    )
    lctr_name: Text = models.CharField(
        max_length=50,
        help_text="The name of the lecture.",
    )
    lctr_source: Text = models.TextField(
        help_text="the source code for the lecture.",
    )
    lctr_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information about the lecture, if any.",
    )

    class Meta:
        managed: bool = True
        db_table: str = "lecture"

    def __str__(self) -> Text:
        """
        Return the name of the lecture.

        :return: A string representing the name of the lecture.
        """
        return self.lctr_name
