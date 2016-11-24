from django.contrib import admin
from silencio.models import Record

class RecordClass(admin.ModelAdmin):
    class Meta:
        model = Record

admin.site.register(Record, RecordClass)
# Register your models here.
