from django.db import models


class User(models.Model):

    """users를 정의한 모델"""

    email = models.CharField(unique=True, max_length=89)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user"


class Teacher(models.Model):

    """teachers를 정의한 모델"""

    user = models.ForeignKey("User", models.DO_NOTHING, blank=True, null=True)
    tcr_name = models.CharField(max_length=50)
    tcr_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "teacher"
