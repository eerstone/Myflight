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
    check_in = models.CharField(max_length=30)
    boarding_port = models.CharField(max_length=30)
    arriving_port = models.CharField(max_length=30)
    Baggage_num = models.CharField(max_length=30)
    company = models.CharField(max_length=20)
    is_mon = models.BooleanField()
    is_tue = models.BooleanField()
    is_wed = models.BooleanField()
    is_thr = models.BooleanField()
    is_fri = models.BooleanField()
    is_sat = models.BooleanField()
    is_sun = models.BooleanField()


def add_Fligt(flight_id,mileage,aircraft_models,plan_departure_time,plan_arrival_time,
                  departure,arrival,punctuality_rate,delay_time,
                  company,is_mon,is_tue,is_wed,is_thr,is_fri,is_sat,is_sun):
    flight = Flight.objects.get_or_create(flight_id=flight_id,mileage=mileage,aircraft_models=aircraft_models,
                                     plan_departure_time=plan_departure_time,plan_arrival_time=plan_arrival_time,
                                     actual_departure_time=plan_departure_time,actual_arrival_time=plan_arrival_time,
                                     departure=departure,arrival=arrival,punctuality_rate=punctuality_rate,delay_time=delay_time,
                                     check_in="A0",boarding_port="H0",arriving_port="C13",Baggage_num="X3",company=company,
                                     is_mon=is_mon, is_tue=is_tue, is_wed=is_wed, is_thr=is_thr, is_fri=is_fri, is_sat=is_sat, is_sun=is_sun
                                     )
    return 1



