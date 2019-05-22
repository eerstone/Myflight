from django.db import models
from django.forms.models import model_to_dict


# Create your models here.
class airport(models.Model):
    airport = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    temperature = models.IntegerField(default=23)
    weather_status = (
        ("0", "晴"),
        ("1", "多云"),
        ("2", "少云"),
        ("3", "阴"),
        ("4", "雾"),
    )
    weather = models.CharField(max_length=10, choices=weather_status, default="晴")
    airport_3_letter = models.CharField(max_length=10, default="--")
    city_3_letter = models.CharField(max_length=10, default="--")


def add_airport(new_airport, city, city_3_letter, airport_3_letter, temperature, weather):
    ap = airport.objects.get_or_create(airport=new_airport, city=city,
                                       airport_3_letter=airport_3_letter, city_3_letter=city_3_letter,
                                       temperature=temperature, weather=weather)


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
        one_ap = str(dict["airport"])
        airport_name.append(one_ap)
    return airport_name


def searchbyid(id):
    return airport.objects.filter(airport=id)