from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from sensor.models import Device,Location
from .context import TestContext
from api_key.models import ApiKey


class LocationTest(TestCase):

    def setUp(self):
        self.context = TestContext()
        self.client = Client()
        self.dev_id = self.context.dev.id
        self.url = reverse("sensor.api.device_location",
                           kwargs={'pk': self.dev_id})
        self.key = str(self.context.dev.post_key.external_key)
        self.name, self.lat, self.lon, self.alt = 'Planet Hoth', 60.588, 7.48, 1222

        
    def test_get_location(self):
        device = Device.objects.get(pk=self.context.dev.id)
        # name = "Ulriken", latitude = 200, longitude = 120, altitude = 600
        self.assertEqual('Ulriken', device.location.name)
        self.assertEqual(200, device.location.latitude)
        self.assertEqual(120, device.location.longitude)
        self.assertEqual(600, device.location.altitude)

    def _assert_error_msg(self, err, msg):
        """Asserts msg in err.message"""
        self.assertIn(msg, err.message)

    def test_create_location_key_issues(self):
        
        with self.assertRaises(KeyError) as ctx:
            data = {'latitude': self.lat,
                    'longitude': self.lon,
                    'name': self.name}
            self.client.get(self.url, data = data)
        self._assert_error_msg(ctx.exception, 'Missing API-key')
        
        with self.assertRaises(KeyError) as ctx:
            data = {'latitude': self.lat,
                    'longitude': self.lon,
                    'name': self.name,
                    'key' : 'Invalid'}
            self.client.get(self.url, data=data)
        self._assert_error_msg(ctx.exception, 'Invalid')

        other_existing_key = ApiKey.objects.create(description="Newerkey")
        with self.assertRaises(KeyError) as ctx:
            data = {'latitude': self.lat,
                    'longitude': self.lon,
                    'name': self.name,
                    'key' : other_existing_key.external_key} 
            self.client.get(self.url, data=data)
        self._assert_error_msg(ctx.exception, 'Invalid')


    def test_create_location_missing_fields(self):
        with self.assertRaises(KeyError) as ctx:  # missing latitude
            data = {'key': self.key, 'longitude': self.lon, 'name': self.name}
            self.client.get(self.url, data=data)
        self._assert_error_msg(ctx.exception, 'latitude')

        with self.assertRaises(KeyError) as ctx:  # missing longitude
            data = {'key': self.key, 'latitude': self.lat, 'name': self.name}
            self.client.get(self.url, data=data)
        self._assert_error_msg(ctx.exception, 'longitude')

        with self.assertRaises(KeyError) as ctx:  # missing name
            data = {'key': self.key, 'latitude': self.lat, 'longitude': self.lon}
            self.client.get(self.url, data=data)
        self._assert_error_msg(ctx.exception, 'name')

    def test_wrong_type_lat(self):
        data = {'key': self.key,
                'latitude': 'fortysix',
                'longitude': self.lon,
                'name': self.name}
        with self.assertRaises(ValueError):
            self.client.get(self.url, data=data)

    def test_wrong_type_lon(self):
        data = {'key': self.key,
                'latitude': self.lat,
                'longitude': 'two',
                'name': self.name}
        with self.assertRaises(ValueError):
            self.client.get(self.url, data=data)

    def test_wrong_type_alt(self):
        data = {'key': self.key,
                'latitude': self.lat,
                'longitude': self.lon,
                'altitude': 'and',
                'name': self.name}
        with self.assertRaises(ValueError):
            self.client.get(self.url, data=data)


    def test_create_location_GET(self):
        data = {'key': self.key,
                'latitude': self.lat,
                'longitude': self.lon,
                'name': self.name}
        self.client.get(self.url, data=data)

        device = Device.objects.get(pk=self.context.dev.id)
        new_loc = device.location

        self.assertEqual(self.lat, new_loc.latitude)
        self.assertEqual(self.lon, new_loc.longitude)
        self.assertEqual(self.name, new_loc.name)
        self.assertEqual(0, new_loc.altitude)

    def test_create_location_POST(self):
        data = {'key': self.key,
                'latitude': self.lat,
                'longitude': self.lon,
                'name': self.name}
        self.client.post(self.url, data=data)

        device = Device.objects.get(pk=self.context.dev.id)
        new_loc = device.location

        self.assertEqual(self.lat, new_loc.latitude)
        self.assertEqual(self.lon, new_loc.longitude)
        self.assertEqual(self.name, new_loc.name)
        self.assertEqual(0, new_loc.altitude)

        
    def test_create_location_with_altitude(self):
        data = {'key': self.key,
                'latitude': self.lat,
                'longitude': self.lon,
                'altitude': self.alt,
                'name': self.name}
        self.client.get(self.url, data=data)

        device = Device.objects.get(pk=self.context.dev.id)
        new_loc = device.location

        self.assertEqual(self.lat, new_loc.latitude)
        self.assertEqual(self.lon, new_loc.longitude)
        self.assertEqual(self.name, new_loc.name)
        self.assertEqual(self.alt, new_loc.altitude)

    def test_list(self):
        client = Client( )
        response = client.get( reverse("sensor.api.location") )
        self.assertEqual( response.status_code , status.HTTP_200_OK )
        data = response.json()
        self.assertEqual( len(data) , Location.objects.all().count())

        
    def test_location(self):
        client = Client( )
        response = client.get( reverse("sensor.api.location" , kwargs = {"pk" : 1000} ))
        self.assertEqual( response.status_code , status.HTTP_404_NOT_FOUND )

        response = client.get( reverse("sensor.api.location" , kwargs = {"pk" : self.context.loc.id} ))
        self.assertEqual( response.status_code , status.HTTP_200_OK )

        data = response.json( )
        loc = self.context.loc
        self.assertEqual( data["name"] , loc.name )
        self.assertEqual( data["id"] , loc.id )
        self.assertEqual( data["latitude"] , loc.latitude )
        self.assertEqual( data["longitude"] , loc.longitude )

