from   django.conf.urls import  url, include
from   rest_framework.urlpatterns import format_suffix_patterns
import sensor.models as models

from api_views import *

urlpatterns = [
    url(r'^device/$' , DeviceView.as_view() , name = "api.device.info"),
    url(r'^device/(?P<pk>%s)/$' % models.Device.IDPattern, DeviceView.as_view() , name = "api.device.info"),
    #
    #
    url(r'^client_log/$' , ClientLogView.as_view(), name = "sensor.api.client_log"),
    #
    url(r'^measurement_type/$' , MeasurementTypeListView.as_view()),
    url(r'^measurement_type/(?P<pk>[0-9]+)/$' , MeasurementTypeView.as_view()),
    #
    url(r'^device_type/$' , DeviceTypeListView.as_view()),
    url(r'^device_type/(?P<pk>[0-9]+)/$' , DeviceTypeView.as_view()),
    #
    url(r'^location/$' , LocationListView.as_view()),
    url(r'^location/(?P<pk>[0-9]+)/$' , LocationView.as_view()),
    #
    url(r'^data_type/$' , DataTypeListView.as_view()),
    url(r'^data_type/(?P<pk>[0-9]+)/$' , DataTypeView.as_view()),
    #
    url(r'^timestamp/$' , TimeStampListView.as_view()),
    url(r'^timestamp/(?P<pk>[0-9]+)/$' , TimeStampView.as_view()),
    #
    url(r'^sensortype/$' , SensorTypeListView.as_view()),
    url(r'^sensortype/(?P<pk>[0-9]+)/$' , SensorTypeView.as_view()),
    #
    url(r'^sensor/$' , SensorListView.as_view()),
    url(r'^sensor/(?P<pk>%s)/$' % models.Sensor.IDPattern , SensorView.as_view()),
    #
    url(r'^sensorinfo/$' , SensorInfoView.as_view(), name = "sensor.api.list_info"),
    url(r'^sensorinfo/(?P<sensor_id>%s)/$' % models.Sensor.IDPattern , SensorInfoView.as_view(), name = "sensor.api.info"),
    #
    url(r'^reading/$'            , ReadingView.as_view(), name = "sensor.api.post"),
    url(r'^reading/(?P<sensor_id>%s)/$' % models.Sensor.IDPattern , ReadingView.as_view(), name = "sensor.api.get"),
    #
    url(r'^rawdata/(?P<sensor_id>%s)/$' % models.Sensor.IDPattern , RawDataView.as_view(), name = "sensor.api.rawdata"),
    #
    url(r'^current/$'   , CurrentValueView.as_view()),
    url(r'^current/(?P<sensor_id>%s)/$' % models.Sensor.IDPattern , CurrentValueView.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
