from django.db import models


class Review(models.Model):
    user = models.ForeignKey("user.User", models.DO_NOTHING)
    crs = models.ForeignKey("course.Course", models.DO_NOTHING)
    star = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "review"
