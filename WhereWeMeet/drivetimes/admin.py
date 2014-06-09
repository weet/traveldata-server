from django.contrib.gis import admin
from WhereWeMeet.drivetimes.models import Meeting, UserCoordinate, LocationType, PointLocation

admin.site.register(Meeting)
admin.site.register(UserCoordinate, admin.GeoModelAdmin)
admin.site.register(LocationType)
admin.site.register(PointLocation,admin.GeoModelAdmin)

