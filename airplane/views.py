from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from . import models
from user import models as um
from airport import models as airportmodels
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
from utils import data_get
from utils import jiguang
import time
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from datetime import datetime as DT
from datetime import date
from datetime import time
from Myflight import settings
from django.http import HttpResponseRedirect, HttpResponse
from delay_prediction import views as dv


# detail
def detail(request):
    if request.method == 'GET':
        return render(request, 'user/detail.html')


# index
def index(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')


# trip
def trip(request):
    if request.method == 'GET':
        return render(request, 'user/trip.html')

#printflight
def printflight(request):
    if request.method == 'GET':
        return render(request, 'user/printflight.html')


def week2flightid(askflight_id, weekday):
    if weekday > 6 or weekday < 0:
        return None
    if weekday == 0:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_mon=1)
    elif weekday == 1:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_tue=1)
    elif weekday == 2:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_wed=1)
    elif weekday == 3:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_thr=1)
    elif weekday == 4:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_fri=1)
    elif weekday == 5:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_sat=1)
    elif weekday == 6:
        flights = models.Flight.objects.filter(flight_id=askflight_id, is_sun=1)
    return flights


def week2flightcity(d_airport, a_airport, weekday):
    if weekday > 6 or weekday < 0:
        return None
    if weekday == 0:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_mon=1)
    elif weekday == 1:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_tue=1)
    elif weekday == 2:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_wed=1)
    elif weekday == 3:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_thr=1)
    elif weekday == 4:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_fri=1)
    elif weekday == 5:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_sat=1)
    elif weekday == 6:
        flights = models.Flight.objects.filter(departure__in=d_airport, arrival__in=a_airport, is_sun=1)
    return flights

pre_columns = ['length', 'time', 'd_weather', 'd_pm', 'd_state', 'a_weather', 'a_pm', 'a_state', 'punctuality_rate']
def getpredata(ret_flight):
    n = len(ret_flight)
    datas = []
    for i in range(0, n):
        data = []
        for item in pre_columns:
            data.append(ret_flight[i][item])
        datas.append(data)
    return datas

# search
def getSearchFlightById(request):
    ret_msg = {}
    if request.method == 'GET':
        askflight_id = request.GET.get('flight_id')
        dtime = request.GET.get('datetime')
        datetime = dtime#String
        is_detail = int(request.GET.get('is_detail'))
        detail_url = request.GET.get('detail_url')

        askflight_id_exist = models.Flight.objects.filter(flight_id=askflight_id)
        if not askflight_id_exist:
            ret_msg['is_exist'] = 0
            ret_flight = []
            ret_msg['flight'] = ret_flight
            return JsonResponse(ret_msg, safe=False)


        today = date.today()
        print(dtime)
        askdate = DT.strptime(dtime, '%Y-%m-%d')
        askdate = askdate.date()
        # askdate = date(askdate.year,askdate.month,askdate.day)
        # dtime.strptime('%Y-%m-%d')
        #print(askdate)
        if askdate > today:
            print("future")
            weekday = askdate.weekday()
            print(weekday)
            flights = week2flightid(askflight_id, weekday)
            if not flights.exists():
                print("future not exists")
                ret_msg['is_exist'] = 0
                ret_flight = []
                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)
            else:
                ret_flights = []
                for flight in flights:
                    flight = model_to_dict(flight)
                    flight = future2normalization(flight)
                    flight["datetime"] = datetime
                    ret_flights.append(flight)

                ret_msg['is_exist'] = 1
                ret_msg['flight'] = sorted(ret_flights, key=operator.itemgetter('plan_departure_time'))
                return JsonResponse(ret_msg, safe=False)
        else:
            if is_detail == 1 and detail_url == '--':
                ret_msg['is_exist'] = 0
                ret_flight = []
                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)

            vf = data_get.variflight()
            ret_msg['is_exist'] = 1
            ret_msg['issucceed'] = 1
            if is_detail:
                ret_flight = vf.get_detail_mes(detail_url, datetime)

                if ret_flight.__len__() == 0:
                    ret_msg['is_exist'] = 0
                    ret_msg['issucceed'] = 0	
                    return JsonResponse(ret_msg, safe=False)
        #        ret_flight["datetime"] = datetime
                datas = getpredata(ret_flight)
                msgs = dv.predict(datas)
                rn = len(ret_flight)

                for ci in range(0, rn):
                    ret_flight[ci]['punctuality_rate'] = msgs[rn]

                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)
            else:
                ret_flight = vf.search_num(askflight_id, datetime)
                if ret_flight.__len__() == 0:
                    ret_msg['is_exist'] = 0
                    ret_msg['issucceed'] = 0	
                    return JsonResponse(ret_msg, safe=False)
                ret_msg['is_exist'] = 1
                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)

        # vf = variflight()
        # ret_msg = vf.search_num(askflight_id)
        # return JsonResponse(ret_msg,safe=False)
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


def getSearchFlightByCity(request):
    ret_msg = {}
    if request.method == 'GET':
        city_from = request.GET.get('city_from')
        city_to = request.GET.get('city_to')
        dtime = request.GET.get('datetime')
        datetime = dtime #String
        is_detail = int(request.GET.get('is_detail'))
        detail_url = request.GET.get('detail_url')

        city_from_exist = airportmodels.airport.objects.filter(city=city_from)
        city_to_exist = airportmodels.airport.objects.filter(city=city_to)
        if  (not city_from_exist.exists() ) or ( not city_to_exist.exists()):
            ret_msg["is_exist"] = 0
            ret_flights = []
            ret_msg['flight'] = ret_flights

            return JsonResponse(ret_msg, safe=False)

        today = date.today()
        askdate = DT.strptime(dtime, '%Y-%m-%d')
        askdate = askdate.date()

        if askdate > today:
            d_airport = airportmodels.city2airport(city_from)
            a_airport = airportmodels.city2airport(city_to)
            print(d_airport)
            print(a_airport)
            weekday = askdate.weekday()
            flights = week2flightcity(d_airport, a_airport, weekday)

            if not flights.exists():
                ret_msg['is_exist'] = 0
                ret_flights = []
                ret_msg['flight'] = ret_flights

                return JsonResponse(ret_msg, safe=False)
            else:
                ret_flights = []
                for flight in flights:
                    flight = model_to_dict(flight)
                    flight = future2normalization(flight)
                    flight["datetime"] = datetime
                    ret_flights.append(flight)
                ret_msg['is_exist'] = 1
                ret_msg['flight'] = sorted(ret_flights, key=operator.itemgetter('plan_departure_time'))
                return JsonResponse(ret_msg, safe=False)
        else:
            if is_detail == 1 and detail_url == '--':
                ret_msg['is_exist'] = 0
                ret_flight = []
                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)

            vf = data_get.variflight()
            ret_msg['is_exist'] = 1
            ret_msg['issucceed'] = 1
            if is_detail:
                print("come here if is_detail")
                ret_flight = vf.get_detail_mes(detail_url, datetime)

                if ret_flight.__len__() == 0:
                    ret_msg['is_exist'] = 0
                    ret_msg['issucceed'] = 0	
                    return JsonResponse(ret_msg, safe=False)
            #    ret_flight["datetime"] = datetime
                datas = getpredata(ret_flight)
                msgs = dv.predict(datas)
                rn = len(ret_flight)

                for ci in range(0, rn):
                    ret_flight[ci]['punctuality_rate'] = msgs[rn]

                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)
            else:
                print("come here else is_detail")
                ret_flight = vf.search_seg(city_from, city_to, datetime)
                if ret_flight.__len__() == 0:
                    ret_msg['is_exist'] = 0
                    ret_msg['issucceed'] = 0	
                    return JsonResponse(ret_msg, safe=False)
                ret_msg['is_exist'] = 1
                ret_msg['flight'] = ret_flight
                return JsonResponse(ret_msg, safe=False)
        # vf = variflight()
        # ret_msg = vf.search_seg(city_from,city_to)
        # return JsonResponse(ret_msg,safe=False)
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

def future2normalization(flight):
    d_terminal = flight["departure_terminal"]
    if d_terminal != "--":
        flight["departure"] = flight["departure"]+d_terminal
    l_terminal = flight["arrival_terminal"]
    if l_terminal != "--":
        flight["arrival"] = flight["arrival"]+l_terminal
    flight["plan_departure_time"] = time.strftime(flight["plan_departure_time"], "%H:%M")
    flight["plan_arrival_time"] = time.strftime(flight["plan_arrival_time"], "%H:%M")
    # flight["actual_departure_time"] = time.strftime(flight["actual_departure_time"],"%H:%M")
    # flight["actual_arrival_time"] = time.strftime(flight["actual_arrival_time"],"%H:%M")
    flight["actual_departure_time"] = "--"
    flight["actual_arrival_time"] = "--"
    flight["real_flight_id"] = flight["flight_id"]
    flight["check_in"] = "--"
    flight["boarding_port"] = "--"
    flight["arriving_port"] = "--"
    flight["Baggage_num"] = "--"
    flight["length"] = flight["mileage"]
    flight["time"] = "--"
    flight["proc"] = "--"
    flight["plane"] = flight["aircraft_models"]
    flight["age"] = "--"
    flight["forecast"] = "--"
    flight["old_state"] = "--"
    flight["d_weather"] = "--"
    flight["d_pm"] = "--"
    flight["d_state"] = "--"
    flight["a_weather"] = "--"
    flight["a_pm"] = "--"
    flight["a_state"] = "--"
    # flight["detail_url"] = "--"
    del flight["id"]
    del flight["is_mon"]
    del flight["is_tue"]
    del flight["is_wed"]
    del flight["is_thr"]
    del flight["is_fri"]
    del flight["is_sat"]
    del flight["is_sun"]
    del flight["mileage"]
    del flight["aircraft_models"]
    return flight


def postFavoriteFlight(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_type = request.POST.get('user_type')
        flight_id = request.POST.get('flight_id')
        datetime = request.POST.get('datetime')
        detail_url = request.POST.get('detail_url')
        #数据库日期更新后，以下两条语句应该无用
        if "T16:00:00Z" in datetime:
            datetime = datetime[0:10]
        #行程是否存在判断
        istrip = um.mytrip.objects.filter(user_ID_id=user_id, user_trip=user_type, flight_id=flight_id,
                                          datetime=datetime, detail_url=detail_url)
        if istrip.exists():
            ret_msg['issucceed'] = 0
            return JsonResponse(ret_msg, safe=False)

        askdate = DT.strptime(datetime, '%Y-%m-%d')
        askdate = askdate.date()
        today = date.today()
        #如果关注行程为未来，则存储未来航班状态至库
        if askdate > today:
            weekday = askdate.weekday()
            flights = week2flightid(flight_id, weekday)
            if not flights.exists():
                ret_msg['issucceed'] = 0
                return JsonResponse(ret_msg, safe=False)
            flight_msg = model_to_dict(flights[0])
            flight_msg = future2normalization(flight_msg)
        #否则为过去和现在，调用爬虫获取状态进行存储，（目前过去实际存储同为现在）
        else:
            vf = data_get.variflight()
            print(detail_url)
            flight_msg = vf.get_detail_mes(detail_url, datetime)
            flight_msg = flight_msg[0]
            flight_msg["delay_time"] = flight_msg["forecast"]
        flight_msg["user_id"] = user_id
        flight_msg["user_type"] = user_type
        flight_msg["datetime"] = datetime
        flight_msg["detail_url"] = detail_url
        um.add_trip(flight_msg)
        # um.mytrip.objects.create(user_ID_id=user_id, flight_id=flight_id, datetime=datetime, user_trip=user_type)
        ret_msg['issucceed'] = 1
        return JsonResponse(ret_msg, safe=False)
    else:
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)


def scan_trip():
    trips = um.mytrip.objects.filter()
    i = 0
    for trip in trips:
        trip_id = trip.id
        user_id = trip.user_ID_id
        datetime = trip.datetime
        flight_id = trip.flight_id
        status = trip.flight_status
        today = date.today()
        print("trip%d" % i)
        i = i + 1
        if datetime > today:
            weekday = datetime.weekday()
            new_flight = week2flightid(flight_id, weekday)
            # print(flight_id,user_id,datetime)
            new_flight = new_flight.first()
            # print(new_flight)
            # print(new_flight)
            if new_flight is None:
                continue
            if new_flight.flight_status != status:
                jiguang.push_msg("尊敬的乘客，您关注的航班%s状态变更为%s，请您及时关注状态变化"%flight_id%new_flight.flight_status,user_id,trip_id)
                trip.flight_status = new_flight.flight_status
                trip.save()
        else:
            if trip.detail_url == "--":
                pass
            else:
                # datetimee = datetime.strftime("%Y-%M-%D")
                # print(datetime.__str__())
                vf = data_get.variflight()
                new_flight = vf.search_num(flight_id, datetime.__str__())
                # print(new_flight)
                # print(flight_id,datetime.__str__())
                new_flight = new_flight[0]
                if new_flight["flight_status"] != status:
                    jiguang.push_msg("尊敬的乘客，您关注的航班%s状态变更为%s，请您及时关注状态变化" % (flight_id, new_flight["flight_status"]),
                                     user_id, trip_id)
                    trip.flight_status = new_flight["flight_status"]
                    trip.save()


def gS_FC(request):
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
    return json
