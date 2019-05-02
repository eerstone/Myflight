from django.db import models
from airplane import models as airplanemodels
from django.forms.models import model_to_dict
# Create your models here.
class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
        ('secret',"保密")
    )
    # id = models.AutoField(primary_key=True) #Django 默认创建自增主键
    nickname = models.CharField(max_length=32)
    email = models.EmailField(default="username@email.com")
    sex = models.CharField(max_length=32,choices=gender,default="保密")
    birthday = models.DateField(default="2000-01-01")
    access = models.IntegerField(default=1)
    icon = models.ImageField(null=True)
    def __str__(self):
        return self.id
    def create_newuser(self,i_type,identifier,pwd):
        try:
            self.user_auth_set.create(identity_type=i_type,identifier=identifier,credential=pwd)
        except:
            pass
class User_Auth(models.Model):
    # id = models.AutoField(primary_key=True) #Django 默认创建自增主键
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Identity_type = (
        ('phone',"手机"),
        ('username',"用户名"),
        #添加其他类型的登录方式
    )
    identity_type = models.CharField(max_length=32,choices=Identity_type,default="手机")
    identifier = models.CharField(max_length=254,unique=True)
    credential = models.CharField(max_length=254)#password or token

class VerifyCode(models.Model):
    # id = models.AutoField(primary_key=True) #Django 默认创建自增主键
    mobile = models.CharField(max_length=32)
    code = models.CharField(max_length=8)

class mytrip(models.Model):
    # id = models.AutoField(primary_key=True) #Django 默认创建自增主键
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    user_trip = models.IntegerField(default=1)
    ##FLIGHT
    flight_id = models.CharField(max_length=100,default="CA1113")
    company = models.CharField(max_length=100,default="--")
    real_flight_id = models.CharField(max_length=100,default="--")
    datetime = models.DateTimeField(default="2000-01-01")

    plan_departure_time = models.CharField(max_length=100,default="--")
    plan_arrival_time = models.CharField(max_length=100,default="--")
    actual_departure_time =  models.CharField(max_length=100,default="--")
    actual_arrival_time = models.CharField(max_length=100,default="--")

    flight_status = models.CharField(max_length=100,default="--")
    departure = models.CharField(max_length=100,default="--")
    arrival = models.CharField(max_length=100,default="--")

    punctuality_rate = models.CharField(max_length=100,default="--")
    delay_time = models.CharField(max_length=100,default="--")
    check_in = models.CharField(max_length=100,default="--")
    boarding_port = models.CharField(max_length=100,default="--")
    arriving_port = models.CharField(max_length=100,default="--")

    Baggage_num = models.CharField(max_length=100,default="--")
    length = models.CharField(max_length=100,default="--")
    time = models.CharField(max_length=100,default="--")

    proc = models.CharField(max_length=100,default="--")
    plane = models.CharField(max_length=100,default="--")
    age = models.CharField(max_length=100,default="--")
    forecast = models.CharField(max_length=100,default="--")
    old_state = models.CharField(max_length=100,default="--")

    d_weather = models.CharField(max_length=100,default="--")
    d_pm = models.CharField(max_length=100,default="--")
    d_state = models.CharField(max_length=100,default="--")

    a_weather = models.CharField(max_length=100,default="--")
    a_pm = models.CharField(max_length=100,default="--")
    a_state = models.CharField(max_length=100,default="--")
    detail_url = models.CharField(max_length=100,default="--")
    ##FLIGHT

def add_trip(one_trip):
    trip = mytrip()
    trip.user_ID = one_trip["user_id"]
    trip.user_trip = one_trip["user_type"]
    trip.flight_id = one_trip["flight_id"]
    trip.company = one_trip["company"]
    trip.real_flight_id = one_trip["real_flight_id"]
    trip.datetime = one_trip["datetime"]
    trip.plan_departure_time = one_trip["plan_departure_time"]
    trip.plan_arrival_time = one_trip["plan_arrival_time"]
    trip.actual_departure_time = one_trip["actual_departure_time"]
    trip.actual_arrival_time = one_trip["actual_arrival_time"]
    trip.flight_status = one_trip["flight_status"]
    trip.departure = one_trip["departure"]
    trip.arrival = one_trip["arrival"]
    trip.punctuality_rate = one_trip["punctuality_rate"]
    trip.delay_time = one_trip["delay_time"]
    trip.check_in = one_trip["check_in"]
    trip.boarding_port = one_trip["boarding_port"]
    trip.arriving_port = one_trip["arriving_port"]
    trip.Baggage_num = one_trip["Baggage_num"]
    trip.length = one_trip["length"]
    trip.time = one_trip["time"]
    trip.proc = one_trip["proc"]
    trip.plane = one_trip["plane"]
    trip.age = one_trip["age"]
    trip.forecast = one_trip["forecast"]
    trip.old_state = one_trip["old_state"]
    trip.d_weather = one_trip["d_weather"]
    trip.d_pm = one_trip["d_pm"]
    trip.d_state = one_trip["d_state"]
    trip.a_weather = one_trip["a_weather"]
    trip.a_pm = one_trip["a_pm"]
    trip.a_state = one_trip["a_state"]
    trip.detail_url = one_trip["detail_url"]
    trip.save()

def del_trip(trip_id):
    trip = mytrip.objects.get(trip_id)
    trip.delete()

def search_trip(user_id):
    trips = mytrip.objects.filter(user_ID_id=user_id)
    re_trips = []
    for t in trips:
        one_trip = model_to_dict(t)
        one_t = {}
        one_t["trip_id"] = one_trip["id"]
        one_t["user_type"] = one_trip["user_trip"]
        del one_trip["id"]
        del one_trip["user_trip"]
        del one_trip["user_ID"]
        one_t["flight"] = one_trip
        re_trips.append(one_t)
    return re_trips

def phone2basicinfo(phone_num):
    user_auth = User_Auth.objects.filter(identifier=phone_num)
    #默认user_auth只有一个
    if user_auth.count()==1:
        user_auth = user_auth[0]
        user = User.objects.filter(id=user_auth.user_id_id)
        user = model_to_dict(user[0])
        #修改字典
        del user["access"]
        print(user)
        user["gender"] = user.pop('sex')
        user["user_id"] = user.pop('id')
        user["user_name"] = user.pop('nickname')
        user["birthday"] = str(user["birthday"])
        user["icon"] = str(user["icon"])
        user["phone_num"] = phone_num
        return user
    else:
        return None

