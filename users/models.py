from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Optional, Text


class User(AbstractUser):

    """users를 정의한 모델"""

    first_name: Text = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    nickname: Optional[Text] = models.CharField(
        unique=True,
        max_length=50,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "user"

    def __str__(self) -> Text:
        return f"{str(self.id)} {self.nickname}"


class Teacher(models.Model):

    """teachers를 정의한 모델"""

    user: User = models.OneToOneField(  # 유저와 선생님 계정은 1대1
        User,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="teachers",
    )
    tcr_name: Text = models.CharField(
        max_length=50,
    )
    tcr_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
    )
    tcr_img: Optional[Text] = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        managed = True
        db_table = "teacher"

    def __str__(self) -> Text:
        return self.tcr_name


class UserCourse(models.Model):
    user: User = models.ForeignKey(
        User,
        models.DO_NOTHING,
        related_name="userCourses",
    )
    course = models.ForeignKey(
        "courses.Course",
        models.DO_NOTHING,
        related_name="userCourses",
    )

    class Meta:
        managed = True
        db_table = "user_course"


class VideoWatches(models.Model):
    user: Optional[User] = models.ForeignKey(
        User,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="videoWatches",
    )
    lecture = models.ForeignKey(
        "courses.Lecture",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="videoWatches",
    )
    isfullywatched: Optional[bool] = models.BooleanField(
        db_column="isFullyWatched",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = "video_watches"
        verbose_name_plural = "Video Watches"
