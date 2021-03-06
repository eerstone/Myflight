from django.conf.urls import url, include
from django.contrib import admin
from .views import ForCodeView
from user import views

app_name = 'user'
urlpatterns = [

    url(r'^register/', views.register),
    url(r'^person/', views.person),
    url(r'^postLogin/', views.postlogin),
    url(r'^login/', views.login),
    url(r'^postLoginapi/', views.postloginapi),
    url(r'^postRegister/', views.postregister),
    url(r'^postVerifiedCode/', ForCodeView.as_view(), name='forcode'),
    url(r'^getVerifiedCode/', views.getVerifiedCode),
    url(r'^apitest/', views.apitest),
    url(r'^getFavorateFlight/', views.getFavorateFlight),
    url(r'^postBasicInfo/', views.postBasicInfo),
    url(r'^postUpdatePassword/', views.postUpdatePassword),
    url(r'^postDelete/', views.postDelete),
    url(r'^postUserPushStatus/', views.postUserPushStatus),
    #url(r'^getSearchFlightById/', views.search_by_id),
]
