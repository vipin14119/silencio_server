from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username


class Record(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    db_level = models.FloatField()

    def __str__(self):
        return self.name + " : " + str(self.db_level)
