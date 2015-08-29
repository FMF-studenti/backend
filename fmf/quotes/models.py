from django.db import models


class Quote(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()
    ip = models.GenericIPAddressField(protocol='IPv4')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + ': ' + self.author
