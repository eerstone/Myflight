# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-10 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190502_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrip',
            name='datetime',
            field=models.DateField(default='2000-01-01'),
        ),
    ]