# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20170609_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='Billablestatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Billable_Status'),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='Employeestatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Employee_Status'),
        ),
    ]
