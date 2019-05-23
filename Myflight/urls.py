"""Myflight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from login import views
from user import  views as userviews



urlpatterns = [
    url(r'^$', userviews.home),
    url(r'^user/', include('user.urls')),
    url(r'^Myflightadmin/', include('Myflightadmin.urls')),
    url(r'^airplane/', include('airplane.urls')),
    url(r'^airport/', include('airport.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),

    # url(r'^static/(?P<path>.*)$', static.serve,
    #     {'document_root': settings.STATIC_ROOT}, name='static')  # 解决静态文件加载失败问题

]


from apscheduler.scheduler import Scheduler
from airplane.views import scan_trip
sched = Scheduler()


# @sched.interval_schedule(seconds=10)
# def my_task1():
#     print(1)

@sched.interval_schedule(seconds=600)
def my_task2():
    scan_trip()


sched.start()