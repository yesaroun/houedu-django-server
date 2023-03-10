from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """users를 정의한 모델"""

    # email: str = models.CharField(unique=True, max_length=89)
    # password: str = models.CharField(max_length=255)
    # created_at: datetime = models.DateTimeField(blank=True, null=True)
    # nickname: str = models.CharField(unique=True, max_length=50, blank=True, null=True)
    nickname: str = models.CharField(unique=True, max_length=50, blank=True, null=True)
    # email: str = models.CharField(unique=True, max_length=89)

    # USERNAME_FIELD = "id"
    # objects = UserManager()
    #
    # def __str__(self):
    #     return self.user_id
    #
    # @property
    # def is_staff(self):
    #     return self.is_admin

    def save(self, *args, **kwargs):
        self.set_password(self.password)  # 비밀번호를 해시하여 저장
        super().save(*args, **kwargs)

    class Meta:
        db_table = "user"


class Teacher(models.Model):

    """teachers를 정의한 모델"""

    user: User = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    tcr_name: str = models.CharField(max_length=50)
    tcr_info: str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "teacher"


class UserCourse(models.Model):
    user: User = models.ForeignKey(User, models.DO_NOTHING)
    course = models.ForeignKey("courses.Course", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "user_course"


class VideoWatches(models.Model):
    user: User = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    lecture = models.ForeignKey(
        "courses.Lecture", models.DO_NOTHING, blank=True, null=True
    )
    isfullywatched: int = models.IntegerField(
        db_column="isFullyWatched", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "video_watches"