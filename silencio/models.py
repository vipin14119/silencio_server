from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    mac = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Record(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    db_level = models.FloatField(null=False, blank=False)
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location.name + " : " + str(self.db_level)
