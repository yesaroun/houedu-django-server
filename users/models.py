from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Optional, Text


class User(AbstractUser):
    """
    사용자를 나타내는 모델
    """

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
    email = models.EmailField(blank=False, unique=True, help_text="이메일 필드")
    user_img: Optional[Text] = models.TextField(
        blank=True, null=True, help_text="사용자 이미지 URL 필드"
    )

    class Meta:
        db_table = "user"

    def __str__(self) -> Text:
        """
        사용자의 문자열 표현 반환

        :return: 사용자 문자열
        """
        return f"{str(self.id)} {self.nickname}"


class Teacher(models.Model):
    """
    강사를 나타내는 모델
    """

    user: User = models.OneToOneField(
        User,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="teachers",
        help_text="강사인 유저, 1대1관계",
    )
    tcr_name: Text = models.CharField(
        max_length=50,
        help_text="강사 이름 필드",
    )
    tcr_info: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="강사 정보 필드",
    )
    tcr_img: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="강사 이미지 URL 필드",
    )
    tcr_career: Optional[Text] = models.TextField(
        blank=True,
        null=True,
        help_text="강사 경력 필드",
    )

    class Meta:
        managed = True
        db_table = "teacher"

    def __str__(self) -> Text:
        """
        강사 이름 반환

        :return: 강사 이름
        """
        return self.tcr_name


class UserCourse(models.Model):
    """
    사용자가 수강한 강의들을 나타내는 모델
    """

    user: User = models.ForeignKey(
        User,
        models.DO_NOTHING,
        related_name="userCourses",
        help_text="강의를 수강한 사용자 필드",
    )
    course = models.ForeignKey(
        "courses.Course",
        models.DO_NOTHING,
        related_name="userCourses",
        help_text="수강한 강의 필드",
    )

    class Meta:
        managed = True
        db_table = "user_course"


class VideoWatches(models.Model):
    """
    사용자가 시청한 동영상들을 나타내는 모델
    """

    user: Optional[User] = models.ForeignKey(
        User,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="videoWatches",
        help_text="시청한 유저 필드",
    )
    lecture = models.ForeignKey(
        "courses.Lecture",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="videoWatches",
        help_text="시청한 강좌 필드",
    )
    isfullywatched: Optional[bool] = models.BooleanField(
        db_column="isFullyWatched",
        blank=True,
        null=True,
        help_text="시청 여부 필드",
    )

    class Meta:
        managed = True
        db_table = "video_watches"
        verbose_name_plural = "Video Watches"
