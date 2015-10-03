from django.db import models
from adminsortable.models import SortableMixin


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contribution = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def name(self):
        return self.__str__()


class BlogArticle(models.Model):
    class Meta:
        managed = False

    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    published = models.DateTimeField()


class ExternalLink(SortableMixin):
    class Meta:
        ordering = ['order']

    title = models.CharField(max_length=50)
    url = models.URLField()

    # define the field the model should be ordered by
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    order_field_name = 'order'

    def __str__(self):
        return self.title
