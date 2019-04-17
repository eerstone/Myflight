from django.conf.urls import url,include
from django.contrib import admin
from Myflightadmin import  views
urlpatterns = [
    url(r'^login/', views.goto_admin_Login),

    url(r'^Manager/add_manager/', views.goto_admin_add_manager),
    url(r'^Manager/add_flight/', views.goto_admin_add_flight),
    url(r'^Manager/mod_flight/', views.goto_admin_mod_flight),
    url(r'^Manager/add_airport/', views.goto_admin_add_airport),
    url(r'^Manager/mod_airport/', views.goto_admin_mod_airport),
    url(r'^Manager/', views.goto_admin_Manager),
    url(r'^add_manager/', views.admin_add_manager),
    url(r'^add_flight/', views.admin_add_flight),
    url(r'^search_flight_by_Id/', views.admin_search_flight_by_Id),
    url(r'^search_flight_by_City/', views.admin_search_flight_by_City),
    url(r'^del_flight/', views.admin_del_flight),
    url(r'^add_airport/', views.admin_add_airport),
    url(r'^search_airport_by_Id/', views.admin_search_airport_by_Id),
    url(r'^search_airport_by_City/', views.admin_search_airport_by_City),
    url(r'^mod_airport/', views.admin_mod_airport),
    url(r'^search_flight_by_City/', views.admin_search_flight_by_City),
]