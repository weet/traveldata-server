from django.conf.urls import patterns, include, url
from WhereWeMeet.drivetimes.views import HomeView
from django.contrib.gis import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api', include('WhereWeMeet.drivetimes.urls', namespace='WhereWeMeet')),
    url(r'^$', HomeView.as_view()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
