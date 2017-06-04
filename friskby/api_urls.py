from django.conf.urls import url, include

from sensor.api.api_views import *

urlpatterns = [
    # These are implemented in the sensor application
    url(r'^location/$' , LocationView.as_view(), name = "api.location"),
    url(r'^location/(?P<pk>[0-9]+)/$' , LocationView.as_view() , name="api.location"),
]
