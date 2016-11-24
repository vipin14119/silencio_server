from __future__ import unicode_literals
from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    db_level = models.FloatField()
