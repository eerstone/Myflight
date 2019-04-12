import requests
from Myflight.settings import APIKEY
class YunPian(object):
    def __init__(self,api_key):
        self.api_key=api_key
        self.single_send_url='https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self,code,mobile):
        parmas={
            'apikey':self.api_key,
            'mobile':mobile,
            'text':'【潘冠东】感谢您注册航班出行小助手，您的验证码是{code}'.format(code=code)
        }

        print(parmas['text'])
        #text必须要跟云片后台的模板内容 保持一致，不然发送不出去！
        r=requests.post(self.single_send_url,data=parmas
        print(r.json())
        return r


if __name__=='__main__':
    yun_pian=YunPian(APIKEY)
    yun_pian.send_sms(1234,18811650310)