# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-02 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0058_auto_20170402_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawdata',
            old_name='s_id',
            new_name='sensor',
        ),
    ]
