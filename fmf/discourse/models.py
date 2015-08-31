from django.db import models


class User(models.Model):
    class Meta:
        managed = False

    name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    messages = models.IntegerField()
    avatar = models.CharField(max_length=256)
