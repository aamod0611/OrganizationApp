# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 10:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0075_auto_20170620_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammembers',
            name='Billablestatus',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='Employeestatus',
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 15, 44, 4, 234064), editable=False),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 15, 44, 4, 234064), editable=False),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 15, 44, 4, 249691), editable=False),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 15, 44, 4, 249691), editable=False),
        ),
        migrations.AlterField(
            model_name='teams',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 15, 44, 4, 249691), editable=False),
        ),
        migrations.AlterField(
            model_name='teams',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 15, 44, 4, 249691), editable=False),
        ),
    ]
