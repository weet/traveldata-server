from rest_framework import serializers
from WhereWeMeet.drivetimes.models import Meeting, UserCoordinate, LocationType, PointLocation

class MeetingSerializer(serializers.ModelSerializer):
    userCoordinates = serializers.SerializerMethodField('get_visible_users')

    def get_visible_users(self,obj):
        #returns the whole thing, should it just return a list of id's?
	visible_users = UserCoordinate.objects.filter(meeting=obj,visible=True)
	return UserCoordinateSerializer(visible_users).data

    class Meta:
        model = Meeting
        fields = ('id', 'name', 'created', 'geojsonResult', 'userCoordinates')


class UserCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCoordinate
        fields = ('id', 'point', 'name', 'transportationType', 'created')


class LocationTypeSerializer(serializers.ModelSerializer):
    #locationPoints = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = LocationType
        detail_allowed_methods = ['get']
        list_allowed_methods = ['get']
        fields = ('id', 'name')

class PointLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointLocation
        fields = ('id', 'name', 'point','description')

