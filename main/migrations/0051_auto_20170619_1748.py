# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 12:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20170619_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccigroups',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 17, 48, 47, 306478)),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 17, 48, 47, 306478)),
        ),
    ]