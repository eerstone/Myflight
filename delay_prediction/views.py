from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from sklearn.externals import joblib

model_path = 'model.m'

airport_status = {'流量正常':0, '小面积延误':1, '大面积延误':2}
weather = {'晴天':0, '多云':1, '阴天':2, '小雨':3, '中雨':4, '大雨':5}

at = [6, 11]
wt = [4, 9]

def isdigit(c):
    return c >= '0' and c <= '9'

def parse(s):
    n = len(s)
    if s.count('提前') + s.count('晚点') == 0:
        return [0, 0]
    p = 1
    if s.count('提前'):
        p = -1

    i = 0
    num = []
    while i < n:
        if isdigit(s[i]):
            cur = 0
            while isdigit(s[i]):
                cur = cur * 10 + int(s[i]) - int('0')
                i += 1
            num.append(cur)
        i += 1

    ti = 0
    if len(num) == 2:
        ti = num[0] * 60 + num[1]
    else:
        ti = num[0]

    return [p * ti, 1]

def getPredict(request):
    ret_msg = {}
    if request.method == 'GET':
        data = request.GET.get('data')
        model = joblib.load(model_path)
        try:
            ti = model.predict(data)
            ti = int(ti)
            ret_msg['is_succeed'] = 0
            if ti < -30:
                msg = '提前半小时以上到达'
            elif ti > 120:
                msg = '晚点2小时以上'
            elif ti > 5:
                msg = '晚点' + str(ti) + '分钟到达'
            elif ti < -5:
                msg = '提前' + str(ti) + '分钟到达'
            else:
                msg = '准点到达'
            ret_msg['msg'] = msg
            return JsonResponse(ret_msg, safe=False)
        except:
            ret_msg['is_succeed'] = 0
            ret_msg['msg'] = 'N/A'
            return JsonResponse(ret_msg, safe=False)
    else:
        ret_msg['is_succeed'] = 0
        ret_msg['msg'] = 'N/A'
        return JsonResponse(ret_msg, safe=False)

def test_predict(data):
    n = len(data)
    d2 = []
    for i in range(0, n):
        if i == 1:
            d2.append(parse(data[i])[0])
        elif i in at:
            d2.append(airport_status[data[i]])
        elif i in wt:
            d2.append(weather[data[i]])
        else:
            d2.append(float(data[i]))

    model = joblib.load(model_path)
    return int(model.predict([d2]))

def main():
    print(test_predict([1795, '1:57', 14, 30, '多云', 29, '小面积延误', 15, 31, '阴天', 12, '小面积延误', 100]))

if __name__ == '__main__':
    main()