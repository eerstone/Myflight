from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from . import models
import requests
import hashlib
import json

def login(request):
    # TBD:already login
    #if request.session.get('is_login', None):
    #    return redirect('/')
    if request.method == 'POST':
        json_data = request.json()
        data = json.loads(json_data)
        ltype = data['type']
        phone_num = data['phone_num']
        # VerifiedCode TBD
        psw = data['psw']
        
        if ltype == 0:
            try:
                user = models.User_Auth.objects.get(identifier=phone_num)
                if user.credential == psw:
                    ret_msg = {'user_id':user.user_id, 'login_status':0}
                    return render(request, '/', json.dumps(ret_msg))
                else:
                    ret_msg = {'user_id':user.user_id, 'login_status':1}
                    return render(request, '/user/login.html', json.dumps(ret_msg))
            except:
                ret_msg = {'user_id':-1, 'login_status':2}
                return render(request, '/user/login.html', json.dumps(ret_msg))

def register(request):
    pass
    return render(request, 'user/index.html')

def getVerifiedCodeapi(request):
    
    return JsonResponse()





import re
import random
from xyw.settings import APIKEY
from .models import VerifyCode


class ForCodeView(View):
    """获取手机验证码"""
    def post(self,request):
        mobile=request.POST.get('mobile','')
        if mobile:
            #验证是否为有效手机号
            mobile_pat=re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res=re.search(mobile_pat,mobile)
            if res:
                #生成手机验证码
                code=VerifyCode()
                code.mobile=mobile
                c=random.randint(1000,9999)
                code.code=str(c)
                code.save()
                code=VerifyCode.objects.filter(mobile=mobile).first().code
                yunpian=YunPian(APIKEY)
                sms_status=yunpian.send_sms(code=code,mobile=mobile)
                msg=sms_status.msg
                return HttpResponse(msg)
            else:
                msg='请输入有效手机号码!'
                return HttpResponse(msg)
        else:
            msg='手机号不能为空！'
            return HttpResponse(msg)