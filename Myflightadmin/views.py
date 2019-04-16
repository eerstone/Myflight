from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def admin_Manager(request):
    return render(request,"Myflightadmin/Manager.html")

def admin_add_manager(request):
    print(1)
    return render(request,"Myflightadmin/add_manager.html")

def admin_add(request):
    return render(request,"Myflightadmin/add_flight.html")