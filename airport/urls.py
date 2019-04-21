from django.conf.urls import url,include
from django.contrib import admin
from airport import  views

urlpatterns = [

    url(r'^getAirportInfo/', views.getAirportInfo),
]