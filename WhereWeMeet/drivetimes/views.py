from django.views.generic import TemplateView
from WhereWeMeet.drivetimes import serializers
from rest_framework import generics
from WhereWeMeet.drivetimes.models import Meeting, UserCoordinate, LocationType, PointLocation

class HomeView(TemplateView):
    template_name = 'index.html'

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Meeting
    serializer_class = serializers.MeetingSerializer

'''
client has no business knowing all user input across all meetings
class UserCoordinateList(generics.ListCreateAPIView):
    model = UserCoordinate
    serializer_class = serializers.UserCoordinateSerializer

    def get_queryset(self):
        return UserCoordinate.objects.filter(visible=True)
'''

#TODO client should not be able to get and modify USerCoordinates
# if the client didn't create it.
class UserCoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    model = UserCoordinate
    serializer_class = serializers.UserCoordinateSerializer


class UserCoordinateByMeetingList(generics.ListAPIView):
    model = UserCoordinate
    serializer_class = serializers.UserCoordinateSerializer

    def get_queryset(self):
        meeting_hash = self.kwargs.get('meeting_hash', None)
        if meeting_hash is not None:
            return UserCoordinate.objects.filter(meeting__id=meeting_hash).filter(visible=True)
        return []


class LocationTypeList(generics.ListAPIView):
    model = LocationType
    serializer_class = serializers.LocationTypeSerializer


class PointLocationList(generics.ListAPIView):
    model = PointLocation
    serializer_class = serializers.PointLocationSerializer

class PointLocationByType(generics.ListAPIView):
    model = PointLocation
    serializer_class = serializers.PointLocationSerializer

    def get_queryset(self):
        locationtype_id = self.kwargs.get('locationtype_id', None)
        if locationtype_id is not None:
            return PointLocation.objects.filter(category__id=locationtype_id)
        return []


