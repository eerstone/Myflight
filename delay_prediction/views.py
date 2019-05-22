from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from sklearn.externals import joblib

model_path = 'model.m'

def getPredict(request):
    ret_msg = {}
    if request.method == 'GET':
        data = request.GET.get('data')
        data = np.array(data)
        model = joblib.load(model_path)
        try:
            prob = model.predict(data)
            ret_msg['is_succeed'] = 0
            ret_msg['prob'] = str(prob)
            return JsonResponse(ret_msg, safe=False)
        except Exception e:
            ret_msg['is_succeed'] = 0
            ret_msg['prob'] = 'N/A'
            return JsonResponse(ret_msg, safe=False)
    else:
        ret_msg['is_succeed'] = 0
        ret_msg['prob'] = 'N/A'
        return JsonResponse(ret_msg, safe=False)