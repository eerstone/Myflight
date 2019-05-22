import os
import sys
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

def loaddicts():
    pass

def main():

    columns = []
    data_path = ''

    map_mile = []
    map_departure = []
    map_arrival = []
    map_weather = []

    dt = pd.read_csv(data_path, headers=columns)

    x_train = dt[columns[:-1]]
    y_train = dt[columns[-1]]

    regressor = RandomForestRegressor()
    regressor = AdaBoostRegressor(n_estimators=100, learning_rate=0.01)

    regressor.fit(x_train, y_train)
    joblib.dump(regressor, 'model.m')

if __name__ == '__main__':
    main()
