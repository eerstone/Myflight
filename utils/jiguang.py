import jpush as jpush
from jpush import common
#此处换成各自的app_key和master_secret
app_key= '19f11eaac0f8577c1a17f3ca'
master_secret = '08822d65b8709a917f765a7c'

_jpush = jpush.JPush(app_key, master_secret)
# _jpush.set_logging("DEBUG")

def all():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="眼泪不是答案")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

def push_msg(message,user_id,trip_id):
    push = _jpush.create_push()
    # push.audience = jpush.all_
    push.audience = {"alias":[user_id]}
    push.notification = jpush.notification(alert=message)
    push.message = jpush.message(message,{"trip_id":[trip_id]})
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

if __name__ == '__main__':
    push_msg("越越nb",1,19)