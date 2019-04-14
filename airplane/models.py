from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_id = models.CharField(max_length=100)
    mileage = models.IntegerField()
    aircraft_models = models.CharField(max_length=30)
    Status = (
        ("1","计划"),
        ("2","起飞"),
        ("3","到达"),
        ("4","延误"),
        ("5","取消"),
    )
    flight_status = models.CharField(max_length=30,choices=Status,default="计划")
    plan_departure_time = models.TimeField()
    plan_arrival_time = models.TimeField()
    actual_departure_time = models.TimeField()
    actual_arrival_time = models.TimeField()
    departure = models.CharField(max_length=30)
    arrival = models.CharField(max_length=30)
    punctuality_rate = models.CharField(max_length=30)
    delay_time = models.CharField(max_length=30)

