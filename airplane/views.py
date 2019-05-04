from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from . import models
from user import models as um
from airport import  models as airportmodels
import requests
import hashlib
import json
import operator
from utils.data_get import variflight
import re
import random
from utils.yunpian import YunPian
from Myflight.settings import APIKEY
from django.views import View
from django_redis import get_redis_connection


from rest_framework.views import APIView
from rest_framework.response import Response
import random

#detail
def detail(request):
    if request.method == 'GET':
        return render(request, 'user/detail.html')

#index
def index(request):
    if request.method=='GET':
        return render(request,'user/index.html')

#trip
def trip(request):
    if request.method=='GET':
        return render(request,'user/trip.html')

#search
def getSearchFlightById(request):
    ret_msg = {}
    if request.method == 'GET':
        askflight_id = request.GET.get('flight_id')
        datetime = request.GET.get('datetime')

        vf = variflight()
        ret_msg = vf.search_num(askflight_id)
        return JsonResponse(ret_msg,safe=False)
        # flights = models.Flight.objects.filter(flight_id=askflight_id)
        # if not flights.exists():
        #     ret_msg['is_exist'] = 0
        #     ret_flight = []
        #     ret_msg['flight'] = ret_flight
        #     return JsonResponse(ret_msg,safe=False)
        # else:
        #     ret_flight=[]
        #     for i in range(flights.count()):
        #         ret_flight.append(model_to_dict(flights[i]))
        #         ret_flight[i]['plan_departure_time'] = str(ret_flight[i]['plan_departure_time'])
        #         ret_flight[i]["plan_arrival_time"] = str(ret_flight[i]["plan_arrival_time"])
        #         ret_flight[i]["actual_departure_time"] = str(ret_flight[i]["plan_departure_time"])
        #         ret_flight[i]["actual_arrival_time"] = str(ret_flight[i]["actual_arrival_time"])
        #     ret_msg['is_exist'] = 1
        #     ret_msg['flight'] = sorted(ret_flight, key=operator.itemgetter('plan_departure_time'))
        #     return JsonResponse(ret_msg,safe=False)
    else:
        ret_msg['is_exist'] = 0
        ret_flight = []
        ret_msg['flight'] = ret_flight
        return JsonResponse(ret_msg, safe=False)

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
    return  json
def getSearchFlightByCity(request):
    ret_msg = {}
    if request.method == 'GET':
        city_from = request.GET.get('city_from')
        city_to = request.GET.get('city_to')
        datetime = request.GET.get('datetime')

        vf = variflight()
        ret_msg = vf.search_seg(city_from,city_to)
        return JsonResponse(ret_msg,safe=False)
        # d_airport = airportmodels.city2airport(city_from)
        # a_airport = airportmodels.city2airport(city_to)
        # flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport)
        #
        # if not flights.exists():
        #     ret_msg['is_exist'] = 0
        #     ret_flights = []
        #     ret_msg['flight'] = ret_flights
        #
        #     return JsonResponse(ret_msg,safe=False)
        # else:
        #     ret_flights = []
        #     for item in flights:
        #         ret_flights.append(model_to_dict(item))
        #     ret_msg['is_exist'] = 1
        #     ret_msg['flight'] = sorted(ret_flights, key=operator.itemgetter('plan_departure_time'))
        #     return JsonResponse(ret_msg,safe=False)
    else:
        ret_msg['is_exist'] = 0
        ret_msg['flight'] = []
        return JsonResponse(ret_msg, safe=False)
    
def postFavoriteFlight(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_type = request.POST.get('user_type')
        flight_id = request.POST.get('flight_id')
        datetime = request.POST.get('datetime')
        um.mytrip.objects.create(user_ID_id=user_id, flight_id=flight_id, datetime=datetime, user_trip=user_type)
        ret_msg['issucceed'] = 1
        return JsonResponse(ret_msg, safe=False)
    else:
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)