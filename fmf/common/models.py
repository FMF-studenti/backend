from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contribution = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
