import datetime
from django.db import models


class User(models.Model):

    """users를 정의한 모델"""

    email: str = models.CharField(unique=True, max_length=89)
    password: str = models.CharField(max_length=255)
    created_at: datetime = models.DateTimeField(blank=True, null=True)
    nickname: str = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user"


class Teacher(models.Model):

    """teachers를 정의한 모델"""

    user: User = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    tcr_name: str = models.CharField(max_length=50)
    tcr_info: str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "teacher"
