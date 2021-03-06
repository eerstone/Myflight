# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-02 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190420_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytrip',
            name='Baggage_num',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='a_pm',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='a_state',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='a_weather',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='actual_arrival_time',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='actual_departure_time',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='age',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='arrival',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='arriving_port',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='boarding_port',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='check_in',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='company',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='d_pm',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='d_state',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='d_weather',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='delay_time',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='departure',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='detail_url',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='flight_status',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='forecast',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='length',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='old_state',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='plan_arrival_time',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='plan_departure_time',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='plane',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='proc',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='punctuality_rate',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='real_flight_id',
            field=models.CharField(default='--', max_length=100),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='time',
            field=models.CharField(default='--', max_length=100),
        ),
    ]
