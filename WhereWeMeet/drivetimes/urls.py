from WhereWeMeet.drivetimes import views
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

    url(r'^/locationtypes/$', views.LocationTypeList.as_view()),
    url(r'^/pointlocations/$', views.PointLocationList.as_view()),
    url(r'^/pointlocations/(?P<locationtype_id>\d+)/$', views.PointLocationByType.as_view()),
    url(r'^/meetings/(?P<pk>[a-zA-Z0-9]+)/$', views.MeetingDetail.as_view()),
    url(r'^/meetings/$', views.MeetingCreate.as_view()),
    url(r'^/usercoordinates/(?P<meeting_hash>[a-zA-Z0-9]+)/$', views.UserCoordinateByMeetingList.as_view()),
    url(r'^/usercoordinates/(?P<pk>\d+)/$',views.UserCoordinateDetail.as_view()),
 )
