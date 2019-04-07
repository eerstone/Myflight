
from django.conf.urls import url,include
from django.contrib import admin
from .views import ForCodeView

urlpatterns = [

    url('forcode/',ForCodeView.as_view(),name='forcode'),
]