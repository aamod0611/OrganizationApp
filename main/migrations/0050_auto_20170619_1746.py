# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 12:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_auto_20170619_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccigroups',
            name='GroupNamee',
        ),
        migrations.AddField(
            model_name='ccigroups',
            name='GroupName',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 17, 46, 37, 801611)),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 17, 46, 37, 801611)),
        ),
    ]
