from django.db import models


class User(models.Model):
    email = models.CharField(unique=True, max_length=89)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user"
