# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 07:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_auto_20170620_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccigroups',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 12, 49, 24, 75200), editable=False),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 12, 49, 24, 75200), editable=False),
        ),
        migrations.AlterField(
            model_name='teams',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 12, 49, 24, 75200), editable=False),
        ),
        migrations.AlterField(
            model_name='teams',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 12, 49, 24, 75200), editable=False),
        ),
        migrations.AlterModelTable(
            name='ccigroups',
            table='CciGroup',
        ),
    ]
