# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0043_remove_rawdata_apikey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdata',
            name='status',
            field=models.IntegerField(choices=[(0, b'Valid'), (2, b'Format error in value'), (3, b'Value out of range'), (4, b'Invalid sensor ID'), (5, b'Sensor offline')], default=0),
        ),
    ]
