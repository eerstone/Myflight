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
    if request.method == "POST":
        issucceeded = administerMagemnet.postadd(request.POST.get("newusrname"),request.POST.get("newusrpsw"))
        return JsonResponse(json.dumps({
            "status": issucceeded
        }),safe=False)

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
    if request.method == "POST":
        issuccessed = flightManagement.postadd(request.POST)
        print(issuccessed)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }),safe=False)

def admin_search_flight_by_Id(request):
    """
            input: json{
                        'flightname':flightname,//航班号
                        'date':date//日期
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        flight{}}
    """
    if request.method == "POST":
        is_exist,flight = flightManagement.getsearchbyId(request.POST.get("flightname"),request.POST.get("date"))
        return JsonResponse(json.dumps({flight,is_exist}), safe=False)

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
    if request.method == "POST":
        flight = flightManagement.getSearchFlightByCity(request.POST.get("takeoff"),request.POST.get("landing"),request.POST.get("date"))
        return JsonResponse(json.dump(flight),safe=False)

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

def admin_del_flight(request):
    """
            input: json{
                        'flightname':filghtname//航班号
                        'date':date//日期}
            output:json{
                        'status':issucceeded  1：删除成功 0：删除失败}
    """
    if request.method == "POST":
        issuccessed = del_flight(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

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
    if request.method == "POST":
        issuccessed = add_airport(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }),safe=False)

def admin_search_airport_by_Id(request):
    """
            input: json{
                        'airport_name':airport_name,//机场名
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        airport{}}
    """
    if request.method == "POST":
        airport = getairportbyId(request.POST)
        return JsonResponse(json.dump(airport),safe=False)

def admin_search_airport_by_City(request):
    """
            input: json{
                        'airport_city':airport_city,//机场所在城市
            output:json{
                        isexist:isexist //1:存在 0:不存在
                        airport{}}
    """
    if request.method == "POST":
        airport = getairportbyCity(request.POST)
        return JsonResponse(json.dump(airport),safe=False)

def admin_mod_airport(request):
    """
            input: json{
                        airport{}}
            output:json{
                        'status':issucceeded  1：修改成功 0：修改失败}
    """
    if request.method == "POST":
        issuccessed = mod_airport(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

def admin_del_airport(request):
    """
            input: json{
                        airport{}}
            output:json{
                        'status':issucceeded  1：删除成功 0：删除失败}
    """
    if request.method == "POST":
        issuccessed = del_airport(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

