# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-22 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airplane', '0003_auto_20190522_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
    ]
