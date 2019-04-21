from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.contrib import auth
from user import models as usermodels
from airplane import views as av
from airplane import models as am
from airport import models as apm
from airport import views as apv
# from Myflightadmin import administerMagemnet
# from Myflightadmin import flightManagement
# from Myadmin import airportManagement
import json
from django.contrib.auth.decorators import login_required
from Myflight import settings
# Create your views here.
from user import models as usermodels
from django.forms.models import model_to_dict



def my_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = usermodels.User_Auth.objects.filter(identifier=username)
    if not user:
        return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def goto_admin_Login(request):
    return render(request, "Myflightadmin/Database.html")


def goto_admin_search_flight(request):
    return render(request, "Myflightadmin/search.html")


def goto_admin_search_airport(request):
    return render(request, "Myflightadmin/search_airport.html")


def check_admin(request):
    # input:username, password
    # issucceed:int 1：成功 2：用户名不存在 3：密码错误 4:不是admin
    ret_msg = {}
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method != 'POST':
        ret_msg['issucceed'] = 2
        return JsonResponse(ret_msg, safe=False)

    user = usermodels.User_Auth.objects.filter(identifier=username)

    if not user.exists():
        ret_msg['issucceed'] = 2
        return JsonResponse(ret_msg, safe=False)

    u = user[0]
    if password != u.credential:
        ret_msg['issucceed'] = 3
        return JsonResponse(ret_msg, safe=False)

    if u.identity_type == '手机':
        ret_msg['issucceed'] = 4
        return JsonResponse(ret_msg, safe=False)

    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


def goto_admin_Manager(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = usermodels.User_Auth.objects.filter(identifier=username)
    request.session["login_user"] = username
    request.session["login_pwd"] = password
    #if request.user.is_authenticated():
    #    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "Myflightadmin/Manager.html")


def goto_admin_add_manager(request):
    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "Myflightadmin/add_manager.html")


def goto_admin_add_flight(request):
    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "Myflightadmin/add_flight.html")


def goto_admin_mod_flight(request):
    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "Myflightadmin/mod_flight.html")


def goto_admin_add_airport(request):
    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "Myflightadmin/add_airport.html")


def goto_admin_mod_airport(request):
    #if not request.user.is_authenticated():
    #    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "Myflightadmin/mod_airport.html")


"""
def admin_add_admin(username,pwd):
    admin_exist = usermodels.User_Auth.objects.filter(identifier=username)
    if admin_exist != None:
        newadmin = usermodels.User(access=0)
        newadminiden = usermodels.User_Auth(user_id=newadmin.id, identity_type="username",
                                            identifier=username, credential=pwd)
        newadmin.save()
        newadminiden.save()

        return 1
    else:
    return 2

"""


def admin_add_flight(request):
    """
        input: json{
                    'takeoff':takeoff,//起飞地
                    'landing':landing,//降落地
                    'filghtname':flightname//航班号
                    'PDtime':PDtime//计划起飞时间
                    'PLtime':PLtime//计划降落时间
                    'airlinename':airlinename//航空公司
                    'date':date//日期}
        output:json{
                    'status':issucceeded  1：添加成功 2：已存在添加失败 3：未知原因，添加失败 0：添加失败}
    """
    flight = {}
    if request.method == 'POST':
        #flight = {}
        flight['departure'] = request.POST['departure']
        flight['arrival'] = request.POST['arrival']
        flight['flight_id'] = request.POST['flight_id']
        flight['plan_departure_time'] = request.POST['plan_departure_time']
        flight['plan_arrival_time'] = request.POST['plan_arrival_time']
        flight['company'] = request.POST['company']
        flight['datetime'] = request.POST['datetime']
        flight['flight_status'] = "计划"
        flight['mileage'] = 0
        flight['aircraft_models'] = ""
        flight['actual_departure_time'] = request.POST['plan_departure_time']
        flight['actual_arrival_time'] = request.POST['plan_arrival_time']
        flight['punctuality_rate'] = "90%"
        flight['delay_time'] = "",
        flight['check_in'] = "A0"
        flight['boarding_port'] = "H0"
        flight['arriving_port'] = "C13"
        flight['Baggage_num'] = "X3"
        flight['is_mon'] = False
        flight['is_tue'] = False
        flight['is_wed'] = False
        flight['is_thr'] = False
        flight['is_fri'] = False
        flight['is_sat'] = False
        flight['is_sun'] = False
        name = request.POST['flight_id']
        origin = am.Flight.objects.filter(flight_id=name)
        if origin.exists():
            ret_msg = {}
            ret_msg['issucceed'] = 2
            return JsonResponse(ret_msg, safe=False)
        return postaddfl(flight)
    else:
        ret_msg = {}
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)


def admin_search_flight_by_Id(request):
    """
            input: json{
                        'flightname':flightname,//航班号
                        'date':date//日期
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        flight{}}
    """
    #flight = av.gS_FC(request)
    #return JsonResponse(flight, safe=False)
    return getsearchbyId(request)#TBD


def admin_search_flight_by_City(request):
    """
            input: json{
                        'takeoff':takeoff,//起飞地
                        'landing':landing,//降落地
                        'date':date//日期}
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        flight{}}
    """
    #flight = av.gS_FC(request)
    #return JsonResponse(flight, safe=False)
    return getSearchFlightByCity(request)#TBD


def admin_mod_flight(request):  # ok
    """
            input: json{
                        flight{}}
            output:json{
                        'status':issucceeded  1：修改成功 0：修改失败}
    """
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    flight = {}
    id = request.POST['flight_id']
    origin = am.searchbyid(id)
    #print(request.POST)
    if origin.exists():
        ofl = model_to_dict(origin[0])
        flight['company'] = str(request.POST['company'])
        flight['flight_id'] = request.POST['flight_id']
        flight['flight_status'] = request.POST['flight_status']
        flight['plan_departure_time'] = request.POST['plan_departure_time']
        flight['actual_departure_time'] = request.POST['actual_departure_time']
        flight['departure'] = request.POST['departure']
        flight['plan_arrival_time'] = request.POST['plan_arrival_time']
        flight['actual_arrival_time'] = request.POST['actual_arrival_time']
        flight['arrival'] = request.POST['arrival']
        flight['punctuality_rate'] = request.POST['punctuality_rate']
        flight['flight_status'] = request.POST['flight_status']
        flight['mileage'] = ofl['mileage']
        flight['aircraft_models'] = ofl['aircraft_models']
        flight['delay_time'] = ofl['delay_time']
        flight['check_in'] = ofl['check_in']
        flight['boarding_port'] = ofl['boarding_port']
        flight['arriving_port'] = ofl['arriving_port']
        flight['Baggage_num'] = ofl['Baggage_num']
        flight['is_mon'] = ofl['is_mon']
        flight['is_tue'] = ofl['is_tue']
        flight['is_wed'] = ofl['is_wed']
        flight['is_thr'] = ofl['is_thr']
        flight['is_fri'] = ofl['is_fri']
        flight['is_sat'] = ofl['is_sat']
        flight['is_sun'] = ofl['is_sun']
        origin.delete()

    return postaddfl(flight)


def admin_del_flight(request):
    """
            input: json{
                        'flightname':filghtname//航班号
                        'date':date//日期}
            output:json{
                        'status':issucceeded  1：删除成功 0：删除失败}
    """
    return postdeletefl(request)


def admin_add_airport(request):
    """
            input: json{
                        'airport_name':airport_name,//机场名
                        'airport_city':airport_city,//机场所在城市
                        'airport_tem':airport_tem//机场温度
                        'airport_wea':airport_wea//机场天气
            output:json{
                        'status':issucceeded  1：添加成功 2：已存在添加失败 3：未知原因，添加失败 0：添加失败}
    """
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    name = request.POST.get('airport')
    city = request.POST.get('city')
    tem = request.POST.get('temperature')
    wea = request.POST.get('weather')

    origin = apm.airport.objects.filter(airport=name)
    if origin.exists():
        ret_msg['issucceed'] = 2
        return JsonResponse(ret_msg, safe=False)

    apm.add_airport(name, city, tem, wea)
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


def admin_search_airport_by_Id(request):
    """
            input: json{
                        'airport_name':airport_name,//机场名
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        airport{}}
    """
    """
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    airport_name = request.POST.get('airport')
    ps = apm.airport.objects.filter(airport=airport_name)

    if not ps.exists():
        ret_msg['issucceed'] = 0
        ret_msg['airport'] = []
        return JsonResponse(ret_msg, safe=False)

    ret_msg['issucceed'] = 1
    ret_msg['airport'] = [ps[0]]
    return JsonResponse(ret_msg, safe=False)
    """
    return apv.getAirport(request)

    #return JsonResponse(apv.gS_FC(request),safe=False)


def admin_search_airport_by_City(request):
    """
            input: json{
                        'airport_city':airport_city,//机场所在城市
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        airport{}}
    """
    ret_msg = {}
    if request.method != 'GET':
        ret_msg['is_exist'] = 0
        return JsonResponse(ret_msg, safe=False)
    city = request.GET.get('city')
    airports = apm.city2airport(city)
    #print(airports)
    if len(airports):
        ret_msg['is_exist'] = 1
    else:
        ret_msg['is_exist'] = 0

    ret_msg['airport'] = apv.getAirportlistByName(airports)
    return JsonResponse(ret_msg, safe=False)
    #return JsonResponse(apv.gS_FC(request), safe=False)


def admin_mod_airport(request):
    """
            input: json{
                        airport{}}
            output:json{
                        'status':issucceeded  1：修改成功 0：修改失败}
    """
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    airport = request.POST

    id = airport['airport']
    origin = apm.searchbyid(id)
    if not origin.exists():
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    origin[0].delete()
    return admin_add_airport(request)


def admin_del_airport(request):
    """
            input: json{
                        airport{}}
            output:json{
                        'status':issucceeded  1：删除成功 0：删除失败}
    """
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    airport = request.POST
    id = airport['airport']
    origin = apm.searchbyid(id)
    origin.delete()

    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


# administerMagemnet
def postaddadmin(request):
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = usermodels.User_Auth.objects.filter(identifier=username)
    if user.count() > 0:
        ret_msg['issucceed'] = 2
        return JsonResponse(ret_msg, safe=False)

    user_new = usermodels.User.objects.create()
    user_au_new = usermodels.User_Auth.objects.create(user_id=user_new, identity_type="用户名"
                                                      , identifier=username, credential=password)
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


def getsearch(request):
    ret_msg = {}
    if request.method != 'GET':
        ret_msg['issucceed'] = 0
        ret_msg['username'] = ''
        ret_msg['password'] = ''
        return JsonResponse(ret_msg, safe=False)

    username = request.POST.get('username')
    users = usermodels.User_Auth.objects.filter(identifier=username)
    if users.count() == 0:
        ret_msg['issucceed'] = 0
        ret_msg['username'] = ''
        ret_msg['password'] = ''
        return JsonResponse(ret_msg, safe=False)

    ret_msg['issucceed'] = 1
    ret_msg['username'] = users[0].identifier
    ret_msg['password'] = users[0].credential
    return JsonResponse(ret_msg, safe=False)


def postdelete(request):
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    username = request.POST.get('username')
    password = request.POST.get('password')
    users = usermodels.User_Auth.objects.filter(identifier=username, credential=password)

    if users.exists():
        users.delete()

    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


def postupdate(request):
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = usermodels.User_Auth.objects.filter(identifier=username)

    if not user.exists:
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    user[0].update(credential=password)
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


# flightManagement
def postaddfl(flight):  # ok
    ret_msg = {}

    # flight = request.POST.get('flight')
    flight_dict = flight
    am.add_Flight(flight_dict['flight_id'], flight_dict['mileage'], flight_dict['flight_status'], flight_dict['aircraft_models'], flight_dict['plan_departure_time'],
                    flight_dict['plan_arrival_time'], flight_dict['departure'], flight_dict['arrival'],
                    flight_dict['punctuality_rate'], flight_dict['delay_time'], flight_dict['company'],
                    flight_dict['is_mon'], flight_dict['is_tue'],
                    flight_dict['is_wed'], flight_dict['is_thr'], flight_dict['is_fri'], flight_dict['is_sat'],
                    flight_dict['is_sun'])
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)


def getsearchbyId(request):
    return av.getSearchFlightById(request)


def getSearchFlightByCity(request):
    return av.getSearchFlightByCity(request)


def postdeletefl(request):
    ret_msg = {}
    if request.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)

    dflight_id = request.POST.get('flight_id')
    datetime = request.POST.get('datetime')
    flights = am.Flight.objects.filter(flight_id=dflight_id)

    if flights.exists():
        flights.delete()

    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)
