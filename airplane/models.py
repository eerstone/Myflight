from django.db import models
from django.forms.models import model_to_dict
# Create your models here.


class Flight(models.Model):
    flight_id = models.CharField(max_length=100)
    mileage = models.IntegerField(default=0)
    aircraft_models = models.CharField(max_length=30)
    Status = (
        ("1", "计划"),
        ("2", "起飞"),
        ("3", "到达"),
        ("4", "延误"),
        ("5", "取消"),
    )
    flight_status = models.CharField(max_length=30,choices=Status,default="计划")
    plan_departure_time = models.TimeField()
    plan_arrival_time = models.TimeField()
    actual_departure_time = models.TimeField()
    actual_arrival_time = models.TimeField()

    departure = models.CharField(max_length=30)
    arrival = models.CharField(max_length=30)
    departure_terminal = models.CharField(max_length=10, default="--")
    arrival_terminal = models.CharField(max_length=10, default="--")

    punctuality_rate = models.CharField(max_length=30, default="--")
    delay_time = models.CharField(max_length=30, default="--")
    check_in = models.CharField(max_length=30, default="--")
    boarding_port = models.CharField(max_length=30, default="--")
    arriving_port = models.CharField(max_length=30, default="--")
    Baggage_num = models.CharField(max_length=30, default="--")
    company = models.CharField(max_length=20)

    detail_url = models.CharField(max_length=200,default="--")
    is_mon = models.BooleanField()
    is_tue = models.BooleanField()
    is_wed = models.BooleanField()
    is_thr = models.BooleanField()
    is_fri = models.BooleanField()
    is_sat = models.BooleanField()
    is_sun = models.BooleanField()



def add_Flight(flight_id, mileage, aircraft_models, plan_departure_time,
               plan_arrival_time, departure, arrival,
               departure_terminal, arrival_terminal,
               punctuality_rate, delay_time, company,
               is_mon, is_tue, is_wed, is_thr, is_fri, is_sat, is_sun
               , flight_status):
    # print(delay_time)
    flight = Flight.objects.get_or_create(flight_id=flight_id, mileage=mileage, flight_status=flight_status,
                                          aircraft_models=aircraft_models,
                                          plan_departure_time=plan_departure_time, plan_arrival_time=plan_arrival_time,
                                          actual_departure_time=plan_departure_time,
                                          actual_arrival_time=plan_arrival_time,
                                          departure=departure, arrival=arrival, departure_terminal=departure_terminal,
                                          arrival_terminal=arrival_terminal,
                                          punctuality_rate=punctuality_rate,
                                          delay_time=delay_time, check_in="--", boarding_port="--", arriving_port="--",
                                          Baggage_num="--", company=company,
                                          is_mon=is_mon, is_tue=is_tue, is_wed=is_wed, is_thr=is_thr, is_fri=is_fri,
                                          is_sat=is_sat, is_sun=is_sun,
                                          )
    return 1


def airport2flight(airport, isfrom):
    """
    输入机场，为出发机场 或到达机场，返回对应航班的列表，
    :param airport:
    :param isfrom:
    :return:
    """
    if isfrom:
        flightset = Flight.objects.filter(departure=airport)
        flights = []
        if flightset.exists():
            for flight in flightset:
                flights += model_to_dict(flight)
            return flights
        else:
            return None
    else:
        flightset = Flight.objects.filter(arrival=airport)
        flights = []
        if flightset.exists():
            for flight in flightset:
                flights += model_to_dict(flight)
            return flights
        else:
            return None
from airplane.views import future2normalization


def searchbyid(flightid):
    flight = Flight.objects.filter(flight_id=flightid)
    # flight = model_to_dict(flight[0])
    # flight = future2normalization(flight)
    return flight
