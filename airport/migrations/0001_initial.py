# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-14 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.IntegerField()),
                ('weather', models.CharField(choices=[('0', '晴'), ('1', '多云'), ('2', '少云'), ('3', '阴'), ('4', '雾')], max_length=10)),
            ],
        ),
    ]