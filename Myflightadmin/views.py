from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
# Create your views here.

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

def admin_add_manager(request):
    if request.method == "POST":
        issucceeded = admin_add_admin(request.POST)
        return JsonResponse(json.dumps({
            "status": issucceeded
        }),safe=False)

def admin_add_flight(request):
    if request.method == "POST":
        issuccessed = add_flight(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }),safe=False)

def admin_search_flight_by_Id(request):
    if request.method == "POST":
        flight = getflightbyid(request.POST)
        return JsonResponse(json.dumps(flight), safe=False)

def admin_search_flight_by_City(request):
    if request.method == "POST":
        flight = getflightbyCity(request.POST)
        return JsonResponse(json.dump(flight),safe=False)

def admin_mod_flight(request):
    if request.method == "POST":
        issuccessed = mod_flight(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

def admin_del_flight(request):
    if request.method == "POST":
        issuccessed = del_flight(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

def admin_add_airport(request):
    if request.method == "POST":
        issuccessed = add_airport(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }),safe=False)

def admin_search_airport_by_Id(request):
    if request.method == "POST":
        airport = getairportbyId(request.POST)
        return JsonResponse(json.dump(airport),safe=False)

def admin_search_airport_by_City(request):
    if request.method == "POST":
        airport = getairportbyCity(request.POST)
        return JsonResponse(json.dump(airport),safe=False)

def admin_mod_airport(request):
    if request.method == "POST":
        issuccessed = mod_airport(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

def admin_del_airport(request):
    if request.method == "POST":
        issuccessed = del_airport(request.POST)
        return JsonResponse(json.dumps({
            "status": issuccessed
        }), safe=False)

