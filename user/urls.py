
from django.conf.urls import url,include
from django.contrib import admin
from .views import ForCodeView
from user import  views
app_name = 'user'
urlpatterns = [

    url(r'^login/', views.login),
    url(r'^postlogin/', views.postlogin),
    url(r'^postLoginapi/', views.postloginapi),
    url(r'^register/', views.register),
    url(r'^postRegister/', views.postregister),
    url(r'^postVerifiedCode/',ForCodeView.as_view(),name='forcode'),
    url(r'^getVerifiedCode/', views.getVerifiedCode),
    url(r'^apitest/', views.apitest),
]