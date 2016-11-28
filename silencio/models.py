from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username


class Record(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    db_level = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " : " + str(self.db_level)
