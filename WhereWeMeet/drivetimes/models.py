from django.contrib.gis.db import models
from django.contrib.auth.models import User
from random_primary import RandomPrimaryIdModel

class Meeting(RandomPrimaryIdModel):
  #todo: https://djangosnippets.org/snippets/1249/
  #needs to return "visible user coordinate ids (from fk)", drivetime_geojson, and locations of interest
  name = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  geojsonResult = models.TextField(blank=True,null=True) #dump a json hash in here

  def __unicode__(self):
    return u'Meeting #%s' % self.id 

class UserCoordinate(models.Model):
  CAR = 'C'
  PUBLIC = 'P'
  WALKING = 'W'
  BICYCLE = 'B'
  TRANSPORTATION_TYPE_CHOICES = (
        (CAR, 'Car'),
        (PUBLIC, 'Public'),
        (WALKING, 'Walking'),
        (BICYCLE, 'Bicycle'),
    )
  meeting = models.ForeignKey(Meeting, related_name='userCoordinates')
  point = models.PointField(geography=True)
  name = models.CharField(max_length = 100, blank=True, null = True)
  transportationType = models.CharField(max_length = 1, choices = TRANSPORTATION_TYPE_CHOICES)
  visible = models.BooleanField()
  created = models.DateTimeField(auto_now_add=True)

class LocationType(models.Model):
  name = models.CharField(max_length = 100)

  def __unicode__(self):
    return u'LocationType: %s' % self.name

class PointLocation(models.Model):
  point = models.PointField(geography=True)
  name = models.CharField(max_length = 100)
  category = models.ForeignKey(LocationType, related_name='locationPoints')
  description = models.TextField()
  added = models.DateTimeField(auto_now_add=True)


