#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Myflight.settings")

import django
if django.VERSION >= (1,7):
    django.setup()

import pandas as pd
from airport.models import airport

def main():
    io = "mysql2airport.xls"
    with open("airports.txt","w") as f:
        airports = airport.objects.all()
        for a in airports:
            print(a.airport.__str__())
            f.write(a.airport.__str__()+"\n")



if __name__=="__main__":
    main()
    print("main_done")