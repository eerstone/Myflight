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
from .models import VerifyCode
from django_redis import get_redis_connection


from rest_framework.views import APIView
from rest_framework.response import Response
import random

#airport
def getAirportInfo(request):#TBD:model2dict
    ret_msg = {}
    if request.method == 'POST':
        airport = request.POST.get('airport')
        
        weather = airport.weather
        temperature = airport.temperature
        departure_flights = airplanemodels.objects.filter(boarding_port=airport)
        arrival_flights = airplanemodels.objects.filter(arriving_port=airport)
        
        ret_msg['weather'] = weather
        ret_msg['temperature'] = temperature
        ret_msg['departure_flights'] = departure_flights
        ret_msg['arrival_flights'] = arrival_flights
        
        return JsonResponse(json.dumps(ret_msg),safe=False)
    else:
        pass
    