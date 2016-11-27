from __future__ import unicode_literals
from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    db_level = models.FloatField()

    def __str__(self):
        return self.name + " : "+ str(self.db_level)
