# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-25 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190510_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.BooleanField(default=True),
        ),
    ]