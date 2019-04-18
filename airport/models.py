from django.db import models

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



