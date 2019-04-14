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
    if request.method == 'GET':
        return render(request, 'user/login.html')

def postloginapi(request):
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
                    # return render(request, '/', json.dumps(ret_msg))
                    return JsonResponse(json.dumps(ret_msg),safe=False)
                else:
                    ret_msg = {'user_id':user.user_id, 'login_status':1}
                    # return render(request, 'user/login.html', json.dumps(ret_msg))
                    return JsonResponse(json.dumps(ret_msg),safe=False)
            except:
                ret_msg = {'user_id':-1, 'login_status':2}
                # return render(request, 'user/login.html', json.dumps(ret_msg))
                return JsonResponse(json.dumps(ret_msg),safe=False)
        # return JsonResponse(json.dumps({'user_id':-1, 'login_status':2}),safe=False)
    else:
        render(request, 'user/login.html')

def register(request):
    print(1)
    if request.method == 'POST':
        print(2)
        phone_num = request.POST.get('phone_num')
        passwd = request.POST.get('passwd')
        verifycode = request.POST.get('VerifyCode')
        ret_msg = {}
        flag = (phone_num!=None and passwd!=None and verifycode!=None)
        print(flag)
        if not flag:
            ret_msg['register_status'] = 3
            ret_msg['user_id']=None
            return JsonResponse(ret_msg,safe=False)
        else:
            #手机号与验证码匹配验证
            #验证成功，添加该字段进数据库
            one_user = models.User.objects.create()
            user_id = one_user.id
            user_auth = models.User_Auth.objects.create(user_id=one_user,identity_type="手机"
                                                        ,identifier=phone_num,credential=passwd)
            one_user.save()
            user_auth.save()
            ret_msg['register_status']=0
            ret_msg['user_id']=user_id
            return JsonResponse(ret_msg,safe=False)
    return render(request, 'user/login.html')

def getVerifiedCodeapi(request):
    print("get")
    example =  {'String':'wejfwi'}
    example = json.dumps(example)
    return JsonResponse(example,safe=False)

def postModifyIcon(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        newicon = request.POST.get('icon')
        
        try:
            user = models.User.objects.get(id=user_id)
            user.update(icon=newicon)
            ret_msg['issucceed'] = 0
            return JsonResponse(json.dumps(ret_msg),safe=False)
        except:
            ret_msg['issucceed'] = 1
            return JsonResponse(json.dumps(ret_msg),safe=False)
    else:
        return render(request, 'user/login.html')

def postBasicInfo(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        newuser_name = request.POST.get('user_name')
        newphone_num = request.POST.get('phone_num')
        newgender = request.POST.get('gender')
        newemail = request.POST.get('email')
        newbirthday = request.POST.get('birthday')
        
        try:
            user = models.User.objects.get(id=user_id)
            user.update(nickname=newuser_name)
            user_auth = models.User_Auth.objects.get(user_id=user_id)
            user_auth.update(identifier=newphone_num)
            user.update(sex=newgender)
            user.update(email=newemail)
            user.update(birthday=newbirthday)
            ret_msg['issucceed'] = 0
            return JsonResponse(json.dumps(ret_msg),safe=False)
        except:
            ret_msg['issucceed'] = 1
            return JsonResponse(json.dumps(ret_msg),safe=False)
    else:
        return render(request, 'user/login.html')
    
def postUpdatePassword(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        oldpsw = request.POST.get('oldpsw')
        newpsw = request.POST.get('psw')
        
        user_auth = models.User_Auth.objects.get(user_id=user_id)
        
        if user_auth.credential == oldpsw:
            user_auth.update(credential=newpsw)
            ret_msg['issucceed'] = 0
            return JsonResponse(json.dumps(ret_msg),safe=False)
        else:
            ret_msg['issucceed'] = 1
            return JsonResponse(json.dumps(ret_msg),safe=False)
    else:
        return render(request, 'user/login.html')
    
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