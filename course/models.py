from django.db import models


class Course(models.Model):
    tcr = models.ForeignKey("teacher.Teacher", models.DO_NOTHING, blank=True, null=True)
    crs_name = models.CharField(max_length=50)
    crs_info = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "course"
