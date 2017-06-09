# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20170608_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billable_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillableStatus', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='teammembers',
            name='Billable_Status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Billable_Status'),
        ),
        migrations.AddField(
            model_name='teammembers',
            name='Employee_Status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Employee_Status'),
        ),
    ]
