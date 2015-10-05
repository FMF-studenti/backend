from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Year(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=200)
    years = models.ManyToManyField(Year)

    def __str__(self):
        return self.name


class Subject(models.Model):
    department = models.ForeignKey(Department)
    level = models.ForeignKey(Level)
    year = models.ForeignKey(Year)
    name = models.CharField(max_length=200)
    others = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name + ' (' + str(self.year) + ', ' + str(self.level) + ', ' + str(self.department) + ')'


class Note(models.Model):
    file = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject)
    author = models.CharField(max_length=200)
    uploader = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
