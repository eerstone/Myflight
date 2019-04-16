from django.conf.urls import url,include
from django.contrib import admin
from Myflightadmin import  views
urlpatterns = [
    # url(r'^login/', views.admin_Manager),
    url(r'^login/Manager.html', views.admin_Manager),
    url(r'^add_manager/', views.admin_add_manager),
    url(r'^add/', views.admin_add),
]