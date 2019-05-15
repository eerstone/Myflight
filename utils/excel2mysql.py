#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Myflight.settings")

import django
if django.VERSION >= (1,7):
    django.setup()

import pandas as pd
from airport.models import add_airport
from airplane.models import add_Flight
def main():
    io = "airplane.xls"
    df = pd.read_excel(io,sheet_name="hangban",header=0)
    # print(df.ix[1]["departure_city"])
    print(df.__len__())
    for i in range(df.__len__()):
        data = df.ix[i]
        add_airport(newairport=data["departure_airport"],city=data["departure_city"],temperature=23)
        add_airport(newairport=data["landing_airport"],city=data["landing_city"],temperature=23)
        add_Flight(flight_id=data["flight_schedules"],mileage=data["mileage"],aircraft_models=data["aircraft_models"],
                         plan_departure_time=data["departure_time"],plan_arrival_time=data["landing_time"],
                         departure=data["departure_airport"],arrival=data["landing_airport"],
                         punctuality_rate=data["punctuality_rate"],delay_time=data["average_delayed"],company=data["airlines"],
                         is_mon=data["is_mon"],is_tue=data["is_tue"],is_wed=data["is_wed"],is_thr=data["is_thr"],
                         is_fri=data["is_fri"],is_sat=data["is_sat"],is_sun=data["is_sun"])
        print(i)


if __name__=="__main__":
    main()
    print("main_done")
