from django.contrib import admin
from silencio.models import Record, User, Location


class UserClass(admin.ModelAdmin):

    class Meta:
        model = User
admin.site.register(User, UserClass)


class LocationClass(admin.ModelAdmin):

    class Meta:
        model = Location
admin.site.register(Location, LocationClass)



class RecordClass(admin.ModelAdmin):
    list_display = ('user', 'location', 'db_level')

    class Meta:
        model = Record
admin.site.register(Record, RecordClass)
