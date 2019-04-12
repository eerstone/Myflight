from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from . import models
import requests
import hashlib
import json


import re
import random
from utils.yunpian import YunPian
from Myflight.settings import APIKEY
from django.views import View
from .models import VerifyCode
from django_redis import get_redis_connection


from rest_framework.views import APIView
from rest_framework.response import Response
import random

def login(request):
    # TBD:already login
    #if request.session.get('is_login', None):
    #    return redirect('/')
    if request.method == 'POST':
        # json_data = request.json()
        # data = json.loads(json_data)
        # ltype = data['type']
        # phone_num = data['phone_num']
        # # VerifiedCode TBD
        # psw = data['psw']
        ltype = request.POST.get('type')
        print(ltype)
        phone_num = request.POST.get('phone_num')
        psw = request.POST.get('psw')
        if ltype == 0:
            try:
                user = models.User_Auth.objects.get(identifier=phone_num)
                if user.credential == psw:
                    ret_msg = {'user_id':user.user_id, 'login_status':0}
                    return render(request, '/', json.dumps(ret_msg))
                    # return JsonResponse(json.dumps(ret_msg),safe=False)
                else:
                    ret_msg = {'user_id':user.user_id, 'login_status':1}
                    return render(request, 'user/login.html', json.dumps(ret_msg))
                    # return JsonResponse(json.dumps(ret_msg),safe=False)
            except:
                ret_msg = {'user_id':-1, 'login_status':2}
                return render(request, 'user/login.html', json.dumps(ret_msg))
                # return JsonResponse(json.dumps(ret_msg),safe=False)
        # return JsonResponse(json.dumps({'user_id':-1, 'login_status':2}),safe=False)
    else:
        ret_msg = {'user_id':-1, 'login_status':2}
        return render(request, 'user/login.html',{})
def register(request):
    pass
    return render(request, 'user/index.html')

def getVerifiedCodeapi(request):
    print("get")
    example =  {'String':'wejfwi'}
    example = json.dumps(example)
    return JsonResponse(example,safe=False)

class ForCodeView(View):
    """获取手机验证码"""
    def post(self,request):
        mobile=request.POST.get('mobile','')
        print(mobile)
        if mobile:
            #验证是否为有效手机号
            mobile_pat=re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res=re.search(mobile_pat,mobile)
            if res:
                #生成手机验证码
                #通过redis存储验证码
                redis_conn = get_redis_connection("default")
                c=random.randint(1000,9999)
                redis_conn.setex(mobile,60,str(c))
                #通过自建的数据库存储验证码
                code=VerifyCode()
                code.mobile=mobile
                code.code=str(c)
                code.save()
                code=VerifyCode.objects.filter(mobile=mobile).first().code
                yunpian=YunPian(APIKEY)
                sms_status=yunpian.send_sms(code=code,mobile=mobile)
                sms_status = sms_status.json()
                msg=sms_status["msg"]
                return HttpResponse(msg)
            else:
                msg='请输入有效手机号码!'
                return HttpResponse(msg)
        else:
            msg='手机号不能为空！'
            return HttpResponse(msg)