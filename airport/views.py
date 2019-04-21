from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from . import models
import requests
import hashlib
import json
from airplane import models as airplanemodels

import re
import random
from utils.yunpian import YunPian
from Myflight.settings import APIKEY
from django.views import View
from django_redis import get_redis_connection


from rest_framework.views import APIView
from rest_framework.response import Response
import random

#airport

def getAirport(request):
    ret_msg = {}
    ret_msg["is_exist"]=0
    ret_msg["airport"]=""
    if request.method=='GET':
        airport = request.GET.get('airport')
        one_airport = models.airport.objects.filter(airport=airport)
        if one_airport.count()==0:
            return JsonResponse(ret_msg,safe=False)
        else:
            ret_msg["airport"] = model_to_dict(one_airport[0])
            ret_msg["is_exist"] = 1
            return JsonResponse(ret_msg,safe=False)
    return JsonResponse(ret_msg, safe=False)


def getAirportInfo(request):
    ret_msg = {}
    if request.method == 'GET':
        airport = request.GET.get('airport')
        try:
            # 目前默认获取到的机场名称是一定存在的
            one_airport = models.airport.objects.get(airport=airport)
            weather = one_airport.weather
            temperature = one_airport.temperature
            departure_flights = airplanemodels.Flight.objects.filter(departure=airport)
            arrival_flights = airplanemodels.Flight.objects.filter(arrival=airport)
            departure_flights_dicts = []
            arrival_flights_dicts = []

            if departure_flights.exists():
                for item in departure_flights:
                    departure_flights_dicts.append(model_to_dict(item))

            if arrival_flights.exists():
                for item in arrival_flights:
                    arrival_flights_dicts.append(model_to_dict(item))

            ret_msg['weather'] = weather
            ret_msg['temperature'] = temperature
            ret_msg['departure_flights'] = departure_flights_dicts
            ret_msg['arrival_flights'] = arrival_flights_dicts

            return JsonResponse(ret_msg, safe=False)
        except Exception as e:
            ret_msg= {}
            ret_msg['weather'] = ""
            ret_msg['temperature'] = ""
            ret_msg['departure_flights'] = ""
            ret_msg['arrival_flights'] = ""
            return JsonResponse(ret_msg,safe=False)

    else:
        ret_msg= {}
        ret_msg['weather'] = ""
        ret_msg['temperature'] = ""
        ret_msg['departure_flights'] = ""
        ret_msg['arrival_flights'] = ""
        return JsonResponse(ret_msg,safe=False)

def  gS_FC(request):
    json = {
        "is_exist": 1,
        "airport":
        [
        {
            "airport": "北京首都",
            "city": "北京",
            "temperature": "50",
            "weather": "晴朗"
        },
        {
            "airport": "北京首都",
            "city": "北京",
            "temperature": "50",
            "weather": "晴朗"
        },
        {
            "airport": "北京首都",
            "city": "北京",
            "temperature": "50",
            "weather": "晴朗"
        },
        {
            "airport": "北京首都",
            "city": "北京",
            "temperature": "50",
            "weather": "晴朗"
        }
        ]
    }
    return  json