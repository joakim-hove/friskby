from django.urls import reverse
from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from rest_framework import status

from .context import TestContext
from sensor.models import *
from sensor.sample import downsample
from datetime import datetime as dt


class ApiTest(TestCase):

    def test_urls(self):
        client = Client()
        url = reverse( "api.location" )
        response = client.get( url )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
