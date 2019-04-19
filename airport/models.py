from django.db import models
from django.forms.models import model_to_dict

# Create your models here.
class airport(models.Model):
    airport = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    temperature = models.IntegerField()
    weather_status = (
        ("0","晴"),
        ("1","多云"),
        ("2","少云"),
        ("3","阴"),
        ("4","雾"),
    )
    weather = models.CharField(max_length=10,choices=weather_status)

def add_airport(newairport,city,temperature,weather=None):
    if(temperature>=100 or temperature<-100):
        return None
    ap = airport.objects.get_or_create(airport=newairport,city=city,temperature=temperature,weather="晴")


def airport2info(port):
    """

    :param port:
    :return: basic info about airport
    """
    portinfo = airport.objects.filter(airport=port)
    if portinfo.count()==0:
        portinfo = portinfo[0]
        portinfo = model_to_dict(portinfo)
        del portinfo["id"]
        portinfo["temperature"] = str(portinfo["temperature"])
        return portinfo
    else:
        return None

def city2airport(city):
    """

    :param city:
    :return: list about airports
    """
    airports = airport.objects.filter(city=city)
    airport_name = []
    for port in airports:
        dict = model_to_dict(port)
        airport_name+= dict["airport"]
    return airport_name

