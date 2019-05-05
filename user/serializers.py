from rest_framework import serializers
from django_redis import get_redis_connection
#图片验证码的编写方式 目前用不到
class MsgCodeSerializer(serializers.Serializer):
    '''
    定义需要校验的数据类型
    '''

    imagecode_id = serializers.UUIDField()
    image_string = serializers.CharField(max_length=3,min_length=3)

    def validate(self, attrs):
        print('传递过来的数据',attrs)
        imagecode_id = str(attrs['imagecode_id']) # 从网页中传过来的值为byte类型需要转为字符串类型
        image_string = attrs['image_string'].encode('utf-8')
        print(type(imagecode_id))
        conn = get_redis_connection('default')# 连接redis数据库
        true_string = conn.get(imagecode_id)# 从redis数据库中取值
        print(true_string)
        if not true_string or image_string != true_string:
            raise serializers.ValidationError('验证码错误')

        if image_string == true_string:
            print('验证通过')
        return attrs