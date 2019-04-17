from django.conf.urls import url,include
from django.contrib import admin
from Myflightadmin import  views
urlpatterns = [
    url(r'^login/', views.admin_Login),

    url(r'^Manager/add_manager/', views.admin_add_manager),
    url(r'^Manager/add_flight/', views.admin_add_flight),
    url(r'^Manager/mod_flight/', views.admin_mod_flight),
    url(r'^Manager/add_airport/', views.admin_add_airport),
    url(r'^Manager/mod_airport/', views.admin_mod_airport),
    url(r'^Manager/', views.admin_Manager),
    url(r'^add_manager/', views.scene_update_view),
]