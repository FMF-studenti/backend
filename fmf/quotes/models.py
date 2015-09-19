from django.db import models


class Quote(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return sself.author + ': ' + self.content
