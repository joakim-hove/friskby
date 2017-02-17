import datetime
import pytz

from django.test import TestCase
from sensor.models import *
from .context import TestContext

class SensorTest(TestCase):
    def setUp(self):
        self.context = TestContext( )


    def test_validate(self):
        obj = Sensor.objects.get( sensor_id = "TEMP:XX" )
        self.assertFalse( obj.valid_input(  -100  ))
        self.assertFalse( obj.valid_input(   200 ))
        self.assertFalse( obj.valid_input(   "XYZ"  ))

        self.assertTrue( obj.valid_input(  "50"  ))
        self.assertTrue( obj.valid_input(  50  ))
        
    

