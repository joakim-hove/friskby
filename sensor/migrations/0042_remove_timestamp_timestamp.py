# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-02 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0041_device_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timestamp',
            name='timestamp',
        ),
    ]
