from django.conf.urls import url,include
from django.contrib import admin
from airplane import views as av
from Myflightadmin import  views
urlpatterns = [
    url(r'^login/', views.goto_admin_login),
    url(r'^Adminlogin/', views.check_admin),
    url(r'^logout/', views.logout),
    url(r'^Manager/add_manager/', views.goto_admin_add_manager),
    url(r'^Manager/add_flight/', views.goto_admin_add_flight),
    url(r'^Manager/mod_flight/', views.goto_admin_mod_flight),
    url(r'^Manager/add_airport/', views.goto_admin_add_airport),
    url(r'^Manager/mod_airport/', views.goto_admin_mod_airport),
    #url(r'^Manager/init_search_flight/', views.init_admin_search_flight),
    url(r'^Manager/search_flight/', views.goto_admin_search_flight),
    #url(r'^Manager/init_search_airport/', views.init_admin_search_airport),
    url(r'^Manager/search_airport/', views.goto_admin_search_airport),
    url(r'^Manager/uploadfile/', views.goto_admin_upload_file),
    url(r'^Manager/submit_file/', views.get_submit_file),
    url(r'^Manager/', views.goto_admin_manager),
    url(r'^add_manager/', views.postaddadmin),
    url(r'^add_flight/', views.admin_add_flight),
    #url(r'^search_flight_by_Id/', av.getSearchFlightById),
    #url(r'^search_flight_by_City/', av.getSearchFlightByCity),
    url(r'^search_flight_by_Id/', views.admin_search_flight_by_Id),
    url(r'^search_flight_by_City/', views.admin_search_flight_by_City),
    url(r'^mod_flight/', views.admin_mod_flight),
    url(r'^del_flight/', views.admin_del_flight),
    url(r'^add_airport/', views.admin_add_airport),
    url(r'^search_airport_by_Id/', views.admin_search_airport_by_Id),
    url(r'^search_airport_by_City/', views.admin_search_airport_by_City),
    url(r'^mod_airport/', views.admin_mod_airport),
    url(r'^del_airport/', views.admin_del_airport),
]