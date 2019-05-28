import os
import sys
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

airport_status = {'流量正常':0, '小面积延误':1, '大面积延误':2}
weather = {'晴天':0, '多云':1, '阴天':2, '小雨':3, '中雨':4, '大雨':5}

def main():

    columns = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    data_path = './data/524_tran_data(1).csv'

    dt = pd.read_csv(data_path, usecols=columns)
    dt['出发地机场状态'] = dt['出发地机场状态'].map(airport_status)
    dt['到达地机场状态'] = dt['到达地机场状态'].map(airport_status)

    print(dt.head())
    '''
    x_train = dt[columns[:-1]]
    y_train = dt[columns[-1]]

    regressor = AdaBoostRegressor(n_estimators=100, learning_rate=0.01)

    regressor.fit(x_train, y_train)
    joblib.dump(regressor, 'model.m')
    '''
if __name__ == '__main__':
    main()
