# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 05:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_auto_20170619_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 10, 54, 59, 691765), editable=False),
        ),
        migrations.AddField(
            model_name='teams',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 10, 54, 59, 691765), editable=False),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 10, 54, 59, 677727)),
        ),
        migrations.AlterField(
            model_name='ccigroups',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 10, 54, 59, 677727)),
        ),
        migrations.AlterField(
            model_name='teams',
            name='Group',
            field=models.ForeignKey(db_column='GroupId', default=1, on_delete=django.db.models.deletion.CASCADE, to='main.CciGroups'),
        ),
    ]