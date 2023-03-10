import datetime
from users.models import Teacher, User
from django.db import models


class Course(models.Model):

    """Courses를 정의한 모델"""

    tcr: Teacher = models.ForeignKey(
        "users.Teacher", models.DO_NOTHING, blank=True, null=True
    )
    crs_name: str = models.CharField(max_length=50)
    crs_info: str = models.TextField(blank=True, null=True)
    thumbnail: str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "course"


class Lecture(models.Model):

    """Lectures를 정의한 모델"""

    crs: Course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    lctr_name: str = models.CharField(max_length=50)
    lctr_source: str = models.TextField()
    lctr_info: str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "lecture"


class Review(models.Model):

    """Reviews를 정의한 모델"""

    user: User = models.ForeignKey(
        "users.User", models.DO_NOTHING, blank=True, null=True
    )
    crs: Course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    star: int = models.IntegerField(blank=True, null=True)
    content: str = models.TextField()
    created_at: datetime = models.DateTimeField()
    updated_at: datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "review"


from django.db import models


class Answer(models.Model):
    profileImg = models.URLField(blank=True)  # 이미지 링크를 첨부하기 위함
    profileIntroduce = models.CharField(max_length=150, default="")
    followerNum = models.PositiveIntegerField(default=0)
