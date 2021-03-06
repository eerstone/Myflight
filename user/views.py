from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
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

from airplane import models as airplanemodels
from django.template import loader ,Context

from datetime import datetime as DT
from datetime import date
from datetime import time

#index
def home(request):
    if request.method == 'GET':
        return render(request, 'user/home.html')

#login
def login(request):
    if request.method == 'GET':
        return render(request, 'user/log in.html')

#register
def register(request):
    if request.method=='GET':
        return render(request,"user/register.html")

def person(request):
    if request.method=='GET':
        return render(request,'user/person.html')

def postloginapi(request):
    json =  {
	"login_status" : 0,
	"info" : "access by psw",
	"user" :{
		"user_id": 0,
		"phone_num":"18701618598",
		"user_name":"bill",
		"gender":"male",
		"email":"kingiy12138@gmail.com",
		"birthday":"1997.6.3",
		"icon":"pic1"
	}
}
    return JsonResponse(json,safe=False)


def postlogin(request):
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
        phone_num = request.POST.get('phone_num')
        psw = request.POST.get('pwd')
        verifiedcode = request.POST.get('VerifiedCode')
        print(ltype)
        print(phone_num)
        print(psw)

        basicinfo ={'user_id':-1,'phone_num':"",'user_name':"",'gender':"",'email':"",'birthday':"",'icon':""}
        ifexist = models.User_Auth.objects.filter(identifier=phone_num).count()
        if ifexist:
            user = models.User_Auth.objects.get(identifier=phone_num)
            basicinfo = models.phone2basicinfo(phone_num)
        else:
            ret_msg = {'user':{}, 'login_status':1}
            return JsonResponse(ret_msg,safe=False)
        if ltype == "0":
            try:
                if user.credential == psw:
                    ret_msg = {'user':basicinfo, 'login_status':0}
                    response = HttpResponse('user')
                    response.set_cookie('user_id', 'ret_msg["user"]["user_id"]')
                    response.set_cookie('is_login','true')
                    print('这里')
             #       request.session['is_login'] = True
             #       request.set_cookie['user_id'] = ret_msg["user"]["user_id"]
              #      print(basicinfo)
              #      request.session['user_name'] = psw
                    return JsonResponse(ret_msg,safe=False)
                else:
                    ret_msg = {'user':{}, 'login_status':3}
                    return JsonResponse(ret_msg,safe=False)
            except:
                ret_msg = {'user':{}, 'login_status':4}
                return JsonResponse(ret_msg,safe=False)
        elif ltype == "1":
            try:
                code = VerifyCode.objects.filter(mobile=phone_num).last().code
                if verifiedcode == code:
                    print(123)
                    print(basicinfo)
                    ret_msg = {'user':basicinfo, 'login_status':0}
                    return JsonResponse(ret_msg,safe=False)
                else:
                    ret_msg = {'user':{}, 'login_status':2}
                    return JsonResponse(ret_msg,safe=False)
            except:
                ret_msg = {'user':{}, 'login_status':4}
                return JsonResponse(ret_msg,safe=False)
        return JsonResponse({'user':{}, 'login_status':4},safe=False)
    else:
        return render(request, 'user/log in.html')


def postregister(request):#调试成功
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        passwd = request.POST.get('pwd')
        verifycode = request.POST.get('VerifiedCode')
        ret_msg = {}
        ret_msg["msg"]=""
        flag = (phone_num!=None and passwd!=None and verifycode!=None)
        print(flag)
        if not flag:
            ret_msg['register_status'] = 3
            ret_msg['user_id']=None
            ret_msg["msg"]="手机号、密码与验证码中存在空值"
            return JsonResponse(ret_msg,safe=False)
        elif passwd.__len__() < 6 :
            ret_msg['register_status'] = 3
            ret_msg['user_id']=None
            ret_msg["msg"] = "请设置6位及以上的密码"
            return JsonResponse(ret_msg, safe=False)
        elif passwd.__len__() > 50:
            ret_msg['register_status'] = 3
            ret_msg['user_id']=None
            ret_msg["msg"] = "密码长度不能大于50个字符"
            return JsonResponse(ret_msg, safe=False)
        else:
            #判断手机号是否已经存在
            phone = models.User_Auth.objects.filter(identifier=phone_num)
            if phone.count()>0:
                ret_msg['register_status'] = 1
                ret_msg['user_id']=None
                ret_msg["msg"]="手机号已存在"
                return JsonResponse(ret_msg,safe=False)
            #手机号与验证码匹配验证
            vcode = VerifyCode.objects.filter(mobile=phone_num)
            if not vcode.exists():
                ret_msg['register_status'] = 2
                ret_msg['user_id']=None
                ret_msg["msg"] = "验证码不正确"
                return JsonResponse(ret_msg,safe=False)
            code = VerifyCode.objects.filter(mobile=phone_num).last().code
            if code!=verifycode:
                ret_msg['register_status'] = 2
                ret_msg['user_id']=None
                ret_msg["msg"] = "验证码不正确"
                return JsonResponse(ret_msg,safe=False)
            #验证成功，添加该字段进数据库
            one_user = models.User.objects.create()
            user_id = one_user.id
            user_auth = models.User_Auth.objects.create(user_id=one_user,identity_type="手机"
                                                        ,identifier=phone_num,credential=passwd)
            ret_msg['register_status']=0
            ret_msg['user_id']=user_id
            ret_msg["msg"] = "注册成功"
            return JsonResponse(ret_msg,safe=False)
    return render(request, 'user/log in.html')

def postUserPushStatus(request):
    user_id = request.POST.get("userid")
    user_status = request.POST.get("user_status")

    ret_msg = {}
    if user_id==None or user_status==None:
        ret_msg['issucceed'] = 0
        ret_msg["msg"] = "无效查询，存在字段为空"
        return JsonResponse(ret_msg,safe=False)
    user_id_check = models.User.objects.filter(id=user_id)
    if not user_id_check.exists():
        ret_msg['issucceed'] = 0
        ret_msg["msg"] = "该用户不存在"
        return JsonResponse(ret_msg,safe=False)
    user = user_id_check[0]
    user_status = int(user_status)
    if user_status!=0  and user_status!=1:
        ret_msg['issucceed'] = 0
        ret_msg["msg"] = "用户状态为非法输入"
        return JsonResponse(ret_msg,safe=False)
    user.user_status = user_status
    user.save()
    ret_msg['issucceed'] = 1
    ret_msg["msg"] = "用户消息推送状态变更成功"
    return JsonResponse(ret_msg, safe=False)

def getVerifiedCode(request):
    print("get")
    example =  {'String':'wejfwi'}
    example = json.dumps(example)
    return JsonResponse(example,safe=False)


class ForCodeView(View):  # 调试成功
    """获取手机验证码"""

    def post(self, request):
        mobile = request.POST.get('phone_num', '')
        print(mobile)
        ret_msg = {}
        if mobile:
            # 验证是否为有效手机号
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, mobile)
            if res:
                # 生成手机验证码
                # 通过redis存储验证码
                # redis_conn = get_redis_connection("default")
                c = random.randint(1000, 9999)
                # redis_conn.setex(mobile,60,str(c))
                # 通过自建的数据库存储验证码
                code = VerifyCode()
                code.mobile = mobile
                code.code = str(c)
                vcode = code.code
                yunpian = YunPian(APIKEY)
                sms_status = yunpian.send_sms(code=vcode, mobile=mobile)
                sms_status = sms_status.json()
                msg = sms_status["msg"]
                if sms_status["code"]==0:
                    code.save()
                    ret_msg["CodeStatus"] = 0
                else:
                    ret_msg["CodeStatus"] = 0
                ret_msg["msg"] = msg
                return JsonResponse(ret_msg, safe=False)
            else:
                msg = '请输入有效手机号码!'
                ret_msg["CodeStatus"] = 1
                ret_msg["msg"] = msg
                return JsonResponse(ret_msg, safe=False)
        else:
            msg = '手机号不能为空！'
            ret_msg["CodeStatus"] = 1
            ret_msg["msg"] = msg
            return JsonResponse(ret_msg, safe=False)


def apitest(request):
    print("get")
    example =  {'String':'wejfwi'}
    example = json.dumps(example)
    return JsonResponse(example,safe=False)

#management
def management(request):
    if request.method == 'GET':
        return render(request, 'user/management.html')

def postModifyIcon(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        newicon = request.POST.get('icon')
        
        try:
            user = models.User.objects.get(id=user_id)
            user.update(icon=newicon)
            ret_msg['issucceed'] = 1
            return JsonResponse(ret_msg,safe=False)
        except Exception as e:
            ret_msg['issucceed'] = 0
            return JsonResponse(ret_msg,safe=False)
    else:
        return render(request, 'user/log in.html')

def postBasicInfo(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        newuser_name = request.POST.get('user_name')
        newphone_num = request.POST.get('phone_num')
        newgender = request.POST.get('gender')
        newemail = request.POST.get('email')
        newbirthday = request.POST.get('birthday')

        user_id_check = models.User.objects.filter(id=user_id)
        if not user_id_check.exists():
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "该用户不存在"
            return JsonResponse(ret_msg,safe=False)
        #try:
        user = models.User.objects.get(id=user_id)
        # models.User.objects.filter(id=user_id).update()
        if len(newemail)>320:
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "邮箱长度大于320位"
            return JsonResponse(ret_msg,safe=False)
        else:
            email_pat = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}')
            res  = email_pat.match(newemail)
            # print(res)
            if not res:
                ret_msg['issucceed'] = 0
                ret_msg["msg"] = "请检查输入的邮箱格式"
                return JsonResponse(ret_msg,safe=False)

        birthdate = DT.strptime(newbirthday, '%Y-%m-%d')
        birthdate = birthdate.date()
        today =  date.today()

        if birthdate>today:
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "请输入正确的出生日期"
            return JsonResponse(ret_msg, safe=False)
        if newuser_name.__len__()> 50:
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "请输入50位及以内的用户名长度"
            return JsonResponse(ret_msg, safe=False)
        mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
        res = re.search(mobile_pat, newphone_num)
        if not res:
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "请检查手机号是否正确"
            return JsonResponse(ret_msg, safe=False)

        user_auth = models.User_Auth.objects.get(user_id_id=user_id,identity_type="手机")
        user_auth_check = models.User_Auth.objects.filter(identity_type="手机",identifier=newphone_num)
        if user_auth_check.exists():
            #此处默认手机号仅有一条记录信息
            newphone_userid = user_auth_check[0].user_id_id
            print(type(newphone_userid))
            print(type(user_id))
            print(newphone_userid,int(user_id))
            if newphone_userid != int(user_id):
                ret_msg['issucceed'] = 0
                ret_msg["msg"] = "该手机号已被其他用户注册"
                return JsonResponse(ret_msg, safe=False)
        user_auth.identifier = newphone_num
        user_auth.save()
        user.nickname=newuser_name
        user.sex=newgender
        user.email=newemail
        user.birthday=newbirthday
        user.save()
        ret_msg['issucceed'] = 1
        ret_msg["msg"] = "信息修改成功"
        return JsonResponse(ret_msg,safe=False)
        # except:
        #     ret_msg['issucceed'] = 0
        #     return JsonResponse(ret_msg,safe=False)
    else:
        return render(request, 'user/log in.html')
    
def postUpdatePassword(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        oldpsw = request.POST.get('oldpsw')
        newpsw = request.POST.get('psw')

        user_id_check = models.User.objects.filter(id = user_id)
        if not user_id_check.exists():
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "该用户不存在"
            return JsonResponse(ret_msg,safe=False)


        user_auth = models.User_Auth.objects.get(user_id=user_id)
        if newpsw == None :
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "新密码不能为空"
            return JsonResponse(ret_msg,safe=False)
        if newpsw.__len__() == 0 :
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "新密码不能为空"
            return JsonResponse(ret_msg,safe=False)
        if newpsw.__len__() < 6  :
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "请设置6位及以上的新密码"
            return JsonResponse(ret_msg,safe=False)
        if newpsw.__len__()>50:
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "密码长度不能大于50个字符"
            return JsonResponse(ret_msg,safe=False)

        if user_auth.credential == oldpsw:
            user_auth.credential=newpsw
            user_auth.save()
            ret_msg['issucceed'] = 1
            ret_msg["msg"] = "修改密码成功"
            return JsonResponse(ret_msg,safe=False)
        else:
            ret_msg['issucceed'] = 0
            ret_msg["msg"] = "旧密码错误"
            return JsonResponse(ret_msg,safe=False)
    else:
        return render(request, 'user/log in.html')

def tripsort(elem):
    # print(elem)
    return elem["flight"]["datetime"]

#mytrip
def getFavorateFlight(request):
    ret_msg = {}
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        # trip = models.mytrip.objects.get(user_ID=user_id)
        # flight = airplanemodels.Flight.objects.filter(flight_id=trip.flight_id)
        # flights =[]
        # for f in flight:
        #     flights.append(model_to_dict(f))
        # ret_msg['user_id'] = user_id
        # ret_msg['flight'] = flights
        # ret_msg['user_type'] = trip.user_trip
        ret_msg = models.search_trip(user_id)
        ret_msg.sort(key = tripsort)
        return JsonResponse({"trips":ret_msg},safe=False)
    else:
        pass

def postDelete(request):
    ret_msg = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_id = int(user_id)
        trip_id = request.POST.get('trip_id')

        isexist = models.mytrip.objects.filter(id=trip_id)
        isexist = isexist.exists()
        if (isexist==1):
            trip = models.mytrip.objects.get(id=trip_id)
            if (user_id == trip.user_ID_id):
                trip.delete()
                ret_msg['issucceed'] = 1
                return JsonResponse(ret_msg,safe=False)
            else:
                ret_msg['issucceed'] = 0
                return JsonResponse(ret_msg,safe=False)
        else:
            ret_msg['issucceed'] = 0
            return JsonResponse(ret_msg,safe=False)
    else:
        pass

