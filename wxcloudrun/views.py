import json
import logging

from django.http import JsonResponse
from django.shortcuts import render
from wxcloudrun.models import Counters
from django.http import HttpRequest

import base64
import binascii

from .utils import trunc_open_id, decode_token

logger = logging.getLogger('log')



def reply(request : HttpRequest, _):
    
#     {
#   "ToUserName": "gh_919b00572d95", // 小程序/公众号的原始ID，资源复用配置多个时可以区别消息是给谁的
#   "FromUserName": "oVneZ57wJnV-ObtCiGv26PRrOz2g", // 该小程序/公众号的用户身份openid
#   "CreateTime": 1651049934, // 消息时间
#   "MsgType": "text", // 消息类型
#   "Content": "回复文本", // 消息内容
#   "MsgId": 23637352235060880 // 唯一消息ID，可能发送多个重复消息，需要注意用此ID去重
# }

    try:
        request = json.loads(request.body.decode())
        # print(request)
        openid = request["FromUserName"]
        openid = trunc_open_id(openid) # 保证长度是28字符， 即168位
        
        byte_id = base64.urlsafe_b64decode(openid)
        openid = binascii.hexlify(byte_id).decode('utf-8')
        
        
        KEY_PHASE  = b"oikjhfe3ewdsxcvjp8765r4edf"
        SALT_PHASE = b"234578okhfdwe57iknbvcde5678"
        
        content = request["Content"]
        
        
        if(content == "商务合作"):  
            result = "商务合作信息"
        if(content == "id"):
            result = "查询id" + openid
        elif len(content) == 128:
            try:
                id, time, question = decode_token(request["FromUserName"])
                if(id == openid):
                    result = "{} {} {}".format(id, time, question)
                else:
                    result = "获取这个token时的身份信息和当前微信账号不符" + "{} {} {}".format(id, time, question)
            except Exception as e:
                result = "不合法的token {}".format(e)
        else:
            result = "默认回复"
        
        return JsonResponse({
                "ToUserName": request["FromUserName"],
                "FromUserName": request["ToUserName"],
                "CreateTime":  request["CreateTime"], 
                "MsgType": "text", 
                "Content": result
        })
    except Exception as e:
        return JsonResponse({
            'msg' : e.__repr__()
        })


def index(request, _):
    """
    获取主页

     `` request `` 请求对象
    """

    return render(request, 'index.html')


def counter(request, _):
    """
    获取当前计数

     `` request `` 请求对象
    """

    rsp = JsonResponse({'code': 0, 'errorMsg': ''}, json_dumps_params={'ensure_ascii': False})
    if request.method == 'GET' or request.method == 'get':
        rsp = get_count()
    elif request.method == 'POST' or request.method == 'post':
        rsp = update_count(request)
    else:
        rsp = JsonResponse({'code': -1, 'errorMsg': '请求方式错误'},
                            json_dumps_params={'ensure_ascii': False})
    logger.info('response result: {}'.format(rsp.content.decode('utf-8')))
    return rsp


def get_count():
    """
    获取当前计数
    """

    try:
        data = Counters.objects.get(id=1)
    except Counters.DoesNotExist:
        return JsonResponse({'code': 0, 'data': 0},
                    json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'code': 0, 'data': data.count},
                        json_dumps_params={'ensure_ascii': False})


def update_count(request):
    """
    更新计数，自增或者清零

    `` request `` 请求对象
    """

    logger.info('update_count req: {}'.format(request.body))

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if 'action' not in body:
        return JsonResponse({'code': -1, 'errorMsg': '缺少action参数'},
                            json_dumps_params={'ensure_ascii': False})

    if body['action'] == 'inc':
        try:
            data = Counters.objects.get(id=1)
        except Counters.DoesNotExist:
            data = Counters()
        data.id = 1
        data.count += 1
        data.save()
        return JsonResponse({'code': 0, "data": data.count},
                    json_dumps_params={'ensure_ascii': False})
    elif body['action'] == 'clear':
        try:
            data = Counters.objects.get(id=1)
            data.delete()
        except Counters.DoesNotExist:
            logger.info('record not exist')
        return JsonResponse({'code': 0, 'data': 0},
                    json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'code': -1, 'errorMsg': 'action参数错误'},
                    json_dumps_params={'ensure_ascii': False})
