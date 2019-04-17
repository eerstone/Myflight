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
from .models import VerifyCode
from django_redis import get_redis_connection


from rest_framework.views import APIView
from rest_framework.response import Response
import random

#search
def getSearchFlightById(request):
    ret_msg = {}
    if request.method == 'POST':
        askflight_id = request.POST.get('flight_id')
        datetime = request.POST.get('datetime')
        
        flights = models.Flight.objects.filter(flight_id=askflight_id)
        
        if flights == []:
            ret_msg['is_exist'] = 0
            ret_flight = {}
            ret_msg['flight'] = json.dumps(ret_flight)
            
            return JsonResponse(json.dumps(ret_msg),safe=False)
        else:
            ret_flight = model_to_dict(flights[0])
            ret_msg['is_exist'] = 1
            ret_msg['flight'] = json.dumps(ret_flight)
            return JsonResponse(json.dumps(ret_msg),safe=False)
    else:
        pass

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