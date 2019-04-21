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
    flight_id = models.CharField(max_length=100,default="CA1113")
    # flight_ID = models.ForeignKey(airplanemodels.Flight,on_delete=models.CASCADE)
    #user_trip = models.Integerfield(default=1)
    user_trip = models.IntegerField(default=1)
    datetime = models.DateTimeField(default="2000-01-01")


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

