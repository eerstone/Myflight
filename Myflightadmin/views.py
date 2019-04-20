from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
#from Myflightadmin import administerMagemnet
#from Myflightadmin import flightManagement
#from Myadmin import airportManagement
import json
# Create your views here.
from user import models as usermodels
from airplane import views as av
from airplane import models as am

def goto_admin_Login(request):
    return render(request,"Myflightadmin/Database.html")

def goto_admin_Manager(request):
    return render(request,"Myflightadmin/Manager.html")

def goto_admin_add_manager(request):
    #print(1)
    return render(request,"Myflightadmin/add_manager.html")

def goto_admin_add_flight(request):
    return render(request,"Myflightadmin/add_flight.html")

def goto_admin_mod_flight(request):
    return render(request,"Myflightadmin/mod_flight.html")

def goto_admin_add_airport(request):
    return render(request,"Myflightadmin/add_airport.html")

def goto_admin_mod_airport(request):
    return render(request,"Myflightadmin/mod_airport.html")
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
def admin_add_manager(request):
    """
        input: json{
                    'newusrname':newusrname,
                    'newusrpsw':newusrpsw}
        output:json{
                    'status':issucceeded  1：添加成功 2：已存在添加失败 3：未知原因，添加失败 0：添加失败}
    """
    postaddadmin(request)
    return None

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
    #postaddfl(request)  conflict

def admin_search_flight_by_Id(request):
    """
            input: json{
                        'flightname':flightname,//航班号
                        'date':date//日期
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        flight{}}
    """
    getsearchbyId(request)

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
    getSearchFlightByCity(request)

def admin_mod_flight(request):
    """
            input: json{
                        flight{}}
            output:json{
                        'status':issucceeded  1：修改成功 0：修改失败}
    """
    if request.method == "POST":
        issuccessed = mod_flight(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)
    #postupdatefl(request) TBD

def admin_del_flight(request):
    """
            input: json{
                        'flightname':filghtname//航班号
                        'date':date//日期}
            output:json{
                        'status':issucceeded  1：删除成功 0：删除失败}
    """
    postdeletefl(request)

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
    #TBD

def admin_search_airport_by_Id(request):
    """
            input: json{
                        'airport_name':airport_name,//机场名
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        airport{}}
    """
    #TBD

def admin_search_airport_by_City(request):
    """
            input: json{
                        'airport_city':airport_city,//机场所在城市
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        airport{}}
    """
    #TBD

def admin_mod_airport(request):
    """
            input: json{
                        airport{}}
            output:json{
                        'status':issucceeded  1：修改成功 0：修改失败}
    """
    #TBD

def admin_del_airport(request):
    """
            input: json{
                        airport{}}
            output:json{
                        'status':issucceeded  1：删除成功 0：删除失败}
    """
    #TBD

#administerMagemnet
def postaddadmin(request):
    ret_msg = {}
    if requeset.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = usermodels.User_Auth.objects.filter(identifier=uesrname)
    if user.count() > 0:
        ret_msg['issucceed'] = 2
        return JsonResponse(ret_msg, safe=False)
   
    user_new = usermodels.User.objects.create()
    user_au_new = usermodels.User_Auth.objects.create(user_id=user_new,identity_type="用户名"
                                                        ,identifier=username,credential=password)
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)
    
def getsearch(request):
    ret_msg = {}
    if requeset.method != 'GET':
        ret_msg['issucceed'] = 0
        ret_msg['username'] = ''
        ret_msg['password'] = ''
        return JsonResponse(ret_msg, safe=False)
    
    username = request.POST.get('username')
    users = usermodels.User_Auth.objects.filter(identifier=uesrname)
    if users.count() == 0:
        ret_msg['issucceed'] = 0
        ret_msg['username'] = ''
        ret_msg['password'] = ''
        return JsonResponse(ret_msg, safe=False)
    
    ret_msg['issucceed'] = 1
    ret_msg['username'] = users[0].identifier
    ret_msg['password'] = users[0].credential
    return JsonResponse(ret_msg, safe=False)

def postdelete(requset):
    ret_msg = {}
    if requeset.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    users = usermodels.User_Auth.objects.filter(identifier=uesrname, credential=password)
    
    if users.exists():
        users.delete()
    
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)

def postupdate(request):
    ret_msg = {}
    if requeset.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = usermodels.User_Auth.objects.filter(identifier=uesrname)
    
    if not user.exists:
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    
    user[0].update(credential=password)
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)

#flightManagement
def postaddfl(request):
    ret_msg = {}
    if requeset.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    
    flight = request.POST.get('flight')
    flight_dict = json.loads(flight)
    
    am.add_Fligt(flight_dict['flight_id'], flight_dict['mileage'], flight_dict['aircraft_models'], flight_dict['plan_departure_time'],
                 flight_dict['plan_arrival_time'], flight_dict['departure'], flight_dict['arrival'], flight_dict['punctuality_rate'],
                 flight_dict['delay_time'], flight_dict['company'], flight_dict['is_mon'], flight_dict['is_tue'],
                 flight_dict['is_wed'], flight_dict['is_thr'], flight_dict['is_fri'], flight_dict['is_sat'], flight_dict['is_sun'])
    
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)

def getsearchbyId(request):
    av.getSearchFlightById(request)
    
def getSearchFlightByCity(request):
    av.getSearchFlightByCity(request)
    
def postdeletefl(request):
    ret_msg = {}
    if requeset.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    
    dflight_id = request.POST.get('flight_id')
    datetime = request.POST.get('datetime')
    flights = usermodels.User_Auth.objects.filter(flight_id=dflight_id)
    
    if flights.exists():
        flights.delete()
    
    ret_msg['issucceed'] = 1
    return JsonResponse(ret_msg, safe=False)

def postupdatefl(request):
    ret_msg = {}
    if requeset.method != 'POST':
        ret_msg['issucceed'] = 0
        return JsonResponse(ret_msg, safe=False)
    pass