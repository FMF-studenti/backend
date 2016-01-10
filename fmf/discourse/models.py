from django.db import models


class Topic(models.Model):

    class Meta:
        managed = False

    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    updated = models.DateTimeField()
    last_poster = models.CharField(max_length=256)
    last_poster_avatar = models.CharField(max_length=256)


class User(models.Model):

    class Meta:
        managed = False

    name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    messages = models.IntegerField()
    avatar = models.CharField(max_length=256)
    administrator = models.BooleanField()
    error = models.BooleanField()
