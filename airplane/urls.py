from django.conf.urls import url,include
from django.contrib import admin
from airplane import  views
urlpatterns = [
    url(r'^getSearchFlightByCity/', views.getSearchFlightByCity),
    # url(r'^getSearchFlightByCity/', views.gS_FC),
    url(r'^getSearchFlightById/', views.getSearchFlightById),
    url(r'^postFavoriteFlight/', views.postFavoriteFlight),
]