from django.contrib.auth.models import User

from rest_framework import serializers
from api_key.models import *
from sensor.models import *


class ApiKeySerializer(serializers.ModelSerializer):
    post_key = serializers.CharField( source='getPostKey', read_only=True)

    class Meta:
        model = ApiKey
        fields = ('post_key',)


# This module only contains 'pure' serializers; in particular that
# implies that foreign keys are just represented with their ID. In the
# module info_serializers are several serializers which collect
# information from related classes to present a more convenient view
# for consumers.

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name' , 'latitude', 'longitude', 'altitude')


class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = ('id', 'name')


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField( source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('email','name')


class SensorIDSerializer(serializers.Serializer):
    sensor_list = serializers.CharField( read_only = True )
    

class ClientConfigSerializer(serializers.Serializer):
    sensor_list = SensorIDSerializer( many = True )
    post_path = serializers.CharField( )
    config_path = serializers.CharField( )
    device_id = serializers.CharField( )
    channel = serializers.CharField( )
    post_key = serializers.CharField( required = False )
    
    
    
class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('id',)
        
        

class DeviceSerializer(serializers.ModelSerializer):
    owner = UserSerializer( read_only = True )
    location = LocationSerializer( read_only = True )
    client_config = ClientConfigSerializer( source = 'clientConfig', read_only = True )
    post_key = ApiKeySerializer( read_only = True )
    sensor_types = SensorTypeSerializer( source = 'sensorTypes', many = True )
    
    class Meta:
        model = Device
        fields = ('id', 'location', 'owner', 'client_config','post_key', 'sensor_types')


    def to_representation(self, instance):
        data = super(DeviceSerializer, self).to_representation(instance)
        if "key" in self.context:
            if instance.valid_post_key( self.context["key"] ):
                data["post_key"] = instance.post_key.getPostKey( )
                data["client_config"]["post_key"] = instance.post_key.getPostKey( )
        return data
    
    #def __init__(self, data = None, context = None):
    #    if data is None:
    #        self._data = {}
    #        return
    #
    #    key = None
    #    if context:
    #        if "key" in context:
    #            key = context["key"]
    #    
    #        
    #    device = data
    #    data = {"id" : device.id,
    #            "owner" : { "name" : device.owner.get_full_name( ),
    #                        "email" : device.owner.email }}
    #
    #    if device.location:
    #        loc = device.location
    #        data["location"] = {"name" : loc.name,
    #                            "latitude" : loc.latitude,
    #                            "longitude" : loc.longitude }
    #
    #
    #    data["client_config"] = device.clientConfig( )
    #    
    #    data["post_key"] = "----------"
    #    if device.locked:
    #        if device.valid_post_key( key ):
    #            data["post_key"] = str(device.post_key.external_key)
    #            data["client_config"]["post_key"] = str(device.post_key.external_key)
    #    else:
    #        data["post_key"] = str(device.post_key.external_key)
    #        data["client_config"]["post_key"] = str(device.post_key.external_key)
    #
    #    sensor_types = [sensor.sensor_type.id for sensor in device.sensorList()]
    #    data["sensor_types"] = sensor_types
    #    self._data = data
    #
    #def get_data(self):
    #    return self._data

    

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('id',)


class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        fields = ('timestamp',)




class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('id', 'product_name','short_description','measurement_type','description','unit','min_value','max_value')





class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('sensor_id', 'sensor_type','parent_device','description')






