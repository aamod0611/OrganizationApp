# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 11:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0069_auto_20170620_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccigroups',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 16, 39, 8, 312383), editable=False),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 16, 39, 8, 312383), editable=False),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='BillStatus',
            field=models.IntegerField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 16, 39, 8, 328007), editable=False),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 16, 39, 8, 328007), editable=False),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='MemStatus',
            field=models.IntegerField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 16, 39, 8, 312383), editable=False),
        ),
        migrations.AlterField(
            model_name='teams',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 16, 39, 8, 312383), editable=False),
        ),
    ]
