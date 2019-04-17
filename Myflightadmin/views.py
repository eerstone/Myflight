from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
# Create your views here.

def admin_Login(request):
    return render(request,"Myflightadmin/Database.html")

def admin_Manager(request):
    return render(request,"Myflightadmin/Manager.html")

def admin_add_manager(request):
    #print(1)
    return render(request,"Myflightadmin/add_manager.html")

def admin_add_flight(request):
    return render(request,"Myflightadmin/add_flight.html")

def admin_mod_flight(request):
    return render(request,"Myflightadmin/mod_flight.html")

def admin_add_airport(request):
    return render(request,"Myflightadmin/add_airport.html")

def admin_mod_airport(request):
    return render(request,"Myflightadmin/mod_airport.html")

def scene_update_view(request):
    if request.method == "POST":

        name = request.POST.get('newusrname')
        print(name)
        psw = request.POST.get('newusrpsw')
        print(psw)
        status = 0
        result = "Error!"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result
        }))