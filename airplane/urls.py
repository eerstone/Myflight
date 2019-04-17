from django.conf.urls import url,include
from django.contrib import admin
from airplane import  views
urlpatterns = [
    url(r'^getSearchFlightByCity/', views.gS_FC),
]