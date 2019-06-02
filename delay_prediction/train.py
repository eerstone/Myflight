import os
import sys
import pandas as pd
import numpy as np
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

airport_status = {'流量正常':0, '小面积延误':1, '大面积延误':2}
weather = {'晴天':0, '多云':1, '阴天':2, '小雨':3, '中雨':4, '大雨':5}

def isdigit(c):
    return c >= '0' and c <= '9'

def parse(s):
    n = len(s)
    if s.count('提前') + s.count('晚点') == 0:
        return [1, 0]
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

def transtime(s):
    l = s.split(':')
    return int(l[0]) * 60 + int(l[1])

def main():

    columns = [6, 7, 10, 11, 12, 15, 16, 17, 18, 20]
    columns_text = ['航程', '飞行时长',
                    '出发地天空状况', '出发地pm2.5', '出发地机场状态',
                    '到达地天空状况', '到达地pm2.5', '到达地机场状态', '历史准点率', '实际情况'
                   ]
    data_paths = ['./data/522_tran_data.csv', './data/523_tran_data.csv', './data/524_tran_data.csv']

    dts = []

    for i in data_paths:
        dts.append(pd.read_csv(i, usecols=columns))

    dt = pd.concat(dts, axis=0, ignore_index=True)

    '''
    dts = pd.read_csv(data_paths[0], usecols=columns)
    print(dt.head())
    for i in range(1, 3):
        cur = pd.read_csv(data_paths[i], usecols=columns)
        print(cur.head())
        dt.append(cur)
    '''

    dt['出发地机场状态'] = dt['出发地机场状态'].map(airport_status)
    dt['到达地机场状态'] = dt['到达地机场状态'].map(airport_status)
    dt['出发地天空状况'] = dt['出发地天空状况'].map(weather)
    dt['到达地天空状况'] = dt['到达地天空状况'].map(weather)

    n = len(dt)
    drops = []

    for i in range(0, n):
        dt['飞行时长'][i] = transtime(dt['飞行时长'][i])
        msg = parse(dt['实际情况'][i])
        dt['实际情况'][i] = msg[0]
        if dt['历史准点率'][i] == '-':
            drops.append(i)

    dt.drop(drops, inplace=True)
    dt.reset_index(drop=True, inplace=True)

    dt.dropna(axis=0, how='any', inplace=True)
    dt.reset_index(drop=True, inplace=True)

    print(len(dt))
    print(dt.tail())

    x_train = dt[columns_text[:-1]].values
    y_train = dt[columns_text[-1]].values

    print(type(y_train[-1]))

    regressor = AdaBoostRegressor(n_estimators=100, learning_rate=0.01)

    regressor.fit(x_train, y_train)
    joblib.dump(regressor, 'model.m')

    print('done')

if __name__ == '__main__':
    main()
