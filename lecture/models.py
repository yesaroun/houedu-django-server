from django.db import models


class Lecture(models.Model):
    crs = models.ForeignKey("course.Course", models.DO_NOTHING)
    lctr_name = models.CharField(max_length=50)
    lctr_source = models.TextField()
    lctr_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "lecture"
