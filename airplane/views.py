from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from . import models
import requests
import hashlib
import json

import re
import random
from utils.yunpian import YunPian
from Myflight.settings import APIKEY
from django.views import View
from django_redis import get_redis_connection


from rest_framework.views import APIView
from rest_framework.response import Response
import random

#search
def getSearchFlightById(request):
    ret_msg = {}
    if request.method == 'GET':
        askflight_id = request.GET.get('flight_id')
        datetime = request.GET.get('datetime')
        print(askflight_id)
        flights = models.Flight.objects.filter(flight_id=askflight_id)
        
        if  not flights.exists():
            ret_msg['is_exist'] = 0
            ret_flight = {}
            ret_msg['flight'] = json.dumps(ret_flight)
            None
            return JsonResponse(json.dumps(ret_msg),safe=False)
        else:
            print(flights)
            ret_flight = model_to_dict(flights[0])
            ret_flight["plan_departure_time"] = str(ret_flight["plan_departure_time"])
            ret_flight["plan_arrival_time"] = str(ret_flight["plan_arrival_time"])
            ret_flight["actual_departure_time"] = str(ret_flight["plan_departure_time"])
            ret_flight["actual_arrival_time"] = str(ret_flight["actual_arrival_time"])
            ret_msg['is_exist'] = 1
            ret_msg['flight'] = json.dumps(ret_flight,ensure_ascii=False)
            return JsonResponse(json.dumps(ret_msg,ensure_ascii=False),safe=False)
    else:
        pass

def  gS_FC(request):
    json = {
    "is_exist": 1,
    "flight":
    [
    {
        "flight_id": "CA1835",
        "company": "中国航空",
        "plan_departure_time": "08:05",
        "plan_arrival_time": "10:15",
        "actual_departure_time": "",
        "actual_arrival_time": "",
        "flight_status": "计划",
        "departure": "北京首都",
        "arrival": "上海浦东",
        "punctuality_rate": "0.87",
        "delay_time": "",
        "check_in": "B,F,J,K,L",
        "boarding_port": "",
        "arriving_port": "",
        "Baggage_num": "36"
    },
    {
        "flight_id": "CA1835",
        "company": "中国航空",
        "plan_departure_time": "08:05",
        "plan_arrival_time": "10:15",
        "actual_departure_time": "",
        "actual_arrival_time": "",
        "flight_status": "计划",
        "departure": "北京首都",
        "arrival": "上海浦东",
        "punctuality_rate": "0.87",
        "delay_time": "",
        "check_in": "B,F,J,K,L",
        "boarding_port": "",
        "arriving_port": "",
        "Baggage_num": "36"
    },
    {
        "flight_id": "CA1835",
        "company": "中国航空",
        "plan_departure_time": "08:05",
        "plan_arrival_time": "10:15",
        "actual_departure_time": "",
        "actual_arrival_time": "",
        "flight_status": "计划",
        "departure": "北京首都",
        "arrival": "上海浦东",
        "punctuality_rate": "0.87",
        "delay_time": "",
        "check_in": "B,F,J,K,L",
        "boarding_port": "",
        "arriving_port": "",
        "Baggage_num": "36"
    },
    {
        "flight_id": "CA1835",
        "company": "中国航空",
        "plan_departure_time": "08:05",
        "plan_arrival_time": "10:15",
        "actual_departure_time": "",
        "actual_arrival_time": "",
        "flight_status": "计划",
        "departure": "北京首都",
        "arrival": "上海浦东",
        "punctuality_rate": "0.88",
        "delay_time": "",
        "check_in": "B,F,J,K,L",
        "boarding_port": "",
        "arriving_port": "",
        "Baggage_num": "36"
    }
    ]
}
    return JsonResponse(json,safe=False)

def getSearchFlightByCity(request):
    ret_msg = {}
    if request.method == 'POST':
        city_from = request.POST.get('city_from')
        city_to = request.POST.get('city_to')
        datetime = request.POST.get('datetime')
        
        flights = models.Flight.objects.filter(departure=city_from, arrival=city_to)
        
        if flights == []:
            ret_msg['is_exist'] = 0
            ret_flights = []
            ret_msg['flight'] = ret_flights
            
            return JsonResponse(json.dumps(ret_msg),safe=False)
        else:
            ret_flights = []
            for item in flights:
                ret_flights.append(json.dumps(model_to_dict(item)))
            ret_msg['is_exist'] = 1
            ret_msg['flight'] = ret_flight
            return JsonResponse(json.dumps(ret_msg),safe=False)
    else:
        pass
    
def postFavoriteFlight(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_type = request.POST.get('user_type')
        flight_id = request.POST.get('flight_id')
        datetime = request.POST.get('datetime')
        pass
    else:
        pass