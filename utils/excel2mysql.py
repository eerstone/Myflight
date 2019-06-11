#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Myflight.settings")

import django
if django.VERSION >= (1,7):
    django.setup()

import pandas as pd
from airport.models import add_airport
from airport.models import update_airport
from airplane.models import add_Flight
import numpy as np
def airport_split(airport):
    airport = str(airport)
    list = airport.split("T")
    airport = list[0]
    if list.__len__() == 1:
        terminal = "--"
    else:
        terminal = "T"+list[1]
    return airport,terminal

def isNan(day):
    # print(day)
    # if day is np.nan:
    #     return  0
    # else:
    #     return int(day)
    return day

def main():
    io = "airport2.xls"
    df = pd.read_excel(io,sheet_name="Sheet1",header=0)
    # print(df.ix[1]["departure_city"])
    # df[['mileage']].astype(int)
    print(df.__len__())
    for i in range(df.__len__()):
        data = df.ix[i]
        update_airport(new_airport= data["airport"],temperature=data["temperature"],weather=data["weather"])
        # mileage  = 0
        # aircraft_models =  "--"
        # average_delayed  = "--"
        #
        # is_mon = isNan(data["is_mon"])
        # is_tue = isNan(data["is_tue"])
        # is_wed = isNan(data["is_wed"])
        # is_thr = isNan(data["is_thr"])
        # is_fri = isNan(data["is_fri"])
        # is_sat = isNan(data["is_sat"])
        # is_sun = isNan(data["is_sun"])
        # print(i)
        # dairport,dterminal = airport_split(data["departure_airport"])
        # lairport,lterminal = airport_split(data["landing_airport"])
        # print(dairport,dterminal)
        # print(lairport,lterminal)
        # add_airport(new_airport=dairport,city=data["departure_city"],temperature=23,weather="晴",
        #             airport_3_letter=data['d_airport_3_letter'],city_3_letter=data['d_city_3_letter'])
        # add_airport(new_airport=lairport,city=data["landing_city"],temperature=23,weather="晴",
        #             airport_3_letter=data['l_airport_3_letter'],city_3_letter=data['l_city_3_letter'])

        # add_Flight(flight_id=data["flight_schedules"],flight_status="计划",
        #            mileage=mileage,aircraft_models=aircraft_models,
        #                  plan_departure_time=data["departure_time"],plan_arrival_time=data["landing_time"],
        #                  departure=dairport,arrival=lairport,departure_terminal=dterminal,arrival_terminal=lterminal,
        #                  punctuality_rate=data["punctuality_rate"],delay_time=average_delayed,company=data["airlines"],
        #                  is_mon=is_mon,is_tue=is_tue,is_wed=is_wed,is_thr=is_thr,
        #                  is_fri=is_fri,is_sat=is_sat,is_sun=is_sun,detail_url=data["detail_url"]
        #
        #            )


if __name__=="__main__":
    main()
    print("main_done")
