from django.db import models


class Course(models.Model):

    """Courses를 정의한 모델"""

    tcr = models.ForeignKey("user.Teacher", models.DO_NOTHING, blank=True, null=True)
    crs_name = models.CharField(max_length=50)
    crs_info = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    lctr = models.ForeignKey("Lecture", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "course"


class Lecture(models.Model):

    """Lectures를 정의한 모델"""

    crs = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    lctr_name = models.CharField(max_length=50)
    lctr_source = models.TextField()
    lctr_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "lecture"


class Review(models.Model):

    """Reviews를 정의한 모델"""

    user = models.ForeignKey("user.User", models.DO_NOTHING, blank=True, null=True)
    crs = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "review"
