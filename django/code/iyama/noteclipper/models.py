from django.db import models
from django.urls import reverse

#Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30)
    passwd = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('noteclipper:main')


class Class(models.Model):
    name = models.CharField(max_length = 10)
    activate = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('noteclipper:activate_home')

class Note(models.Model):
    title = models.CharField(max_length = 100)
    done = models.BooleanField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('noteclipper:main')

class Clip(models.Model):
    file = models.CharField(max_length = 100)
    note = models.CharField(max_length = 100)
    class_type = models.CharField(max_length = 15)
    pos = models.BooleanField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('noteclipper:main')