from django.db import models


class Teacher(models.Model):
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    tcr_name = models.CharField(max_length=50)
    tcr_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "teacher"
