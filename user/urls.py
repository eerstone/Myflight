
from django.conf.urls import url,include
from django.contrib import admin
from .views import ForCodeView
from user import  views
app_name = 'user'
urlpatterns = [

    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^getVerifiedCodeapi/', views.getVerifiedCodeapi),
    url(r'^forcode/',ForCodeView.as_view(),name='forcode'),
]