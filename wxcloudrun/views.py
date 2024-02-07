import json
import logging

from django.http import JsonResponse
from django.shortcuts import render
from wxcloudrun.models import Counters, Group, GroupBelong
from django.http import HttpRequest, Http404

import base64
import binascii
from . import puzzle_record, purchase
import datetime

from .utils import trunc_open_id, decode_token

from . import user

logger = logging.getLogger("log")


from .strings import simple_reply, 默认回复


KEY_PHASE = b"oikjhfe3ewdsxcvjp8765r4edf"
SALT_PHASE = b"234578okhfdwe57iknbvcde5678"


def public(request: HttpRequest, _):
    try:
        request = json.loads(request.body.decode())

        if request["a"] != "h9uasd87ft8hje2f81829e98asdif8wudhjha":
            return Http404()

        try:
            open_id = request["openid"]
            assert len(open_id) == 42
            binascii.unhexlify(open_id)
        except:
            raise (Exception("openid 不合法"))

        # print(request)

        if request["action"] == "submit":
            token = request["token"]
            result = submit(open_id, token)
        elif request["action"] == "load":
            token = request["token"]
            result = get_load(False, token, open_id)
        else:
            result = "未知action".format(request["action"])

    except Exception as e:
        result = "失败原因" + e.__repr__()
    return JsonResponse({"msg": result})


def submit(openid, token):
    try:
        id, time, question = decode_token(token, KEY_PHASE, SALT_PHASE)
        if id == openid:
            group_id = user.get_group_id(openid)
            if group_id:
                return puzzle_record.handle_submit(group_id, time, question)
            else:
                return "token合法，但是由于不在队伍中，无法提交"
        else:
            return "获取这个token时的身份信息和当前微信账号不符" + "{} {} {}".format(
                id, time, question
            )
    except Exception as e:
        result = "不合法的token {}".format(e)
    return result


def get_load(trusted, token, openid):
    try:
        group = user.get_group_id(openid)
    except:
        return {"ok": False, "content": [], "msg": "查询不到队伍"}

    if trusted:
        return puzzle_record.get_progress(group)

    if int(token) != group.token:
        return {"ok": False, "content": [], "msg": "验证码错误"}

    if datetime.datetime.now() > group.token_expire:
        return {"ok": False, "content": [], "msg": "验证码过期"}

    return puzzle_record.get_progress(group)


def reply(request: HttpRequest, _):

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
        openid = trunc_open_id(openid)  # 保证长度是28字符， 即168位

        byte_id = base64.urlsafe_b64decode(openid)
        openid = binascii.hexlify(byte_id).decode("utf-8")

        content: str = request["Content"]

        msgtype = "text"

        if content.startswith("查询id"):
            result = "你的id是: " + openid

        elif content.startswith("创建队伍"):
            try:
                result = user.create_group(openid)
            except Exception as e:
                result = "创建队伍失败！ {}".format(e)

        elif content.startswith("加入队伍"):
            try:
                try:
                    group_id = int(content.split(" ")[1])
                    token = int(content.split(" ")[2])
                except:
                    raise Exception("格式有误。示例 \n加入队伍 123 352532")
                result = user.join_group(openid, group_id, token)
            except Exception as e:
                result = "加入队伍失败！ {}".format(e)

        elif content.startswith("退出队伍"):
            try:
                result = user.exit_group(openid)
            except Exception as e:
                result = "退出队伍失败！ {}".format(e)

        elif content.startswith("验证码"):
            try:
                result = user.create_token(openid)
            except Exception as e:
                result = "获取验证码失败！ {}".format(e)

        elif content.startswith("同步进度"):
            progress = get_load(True, "", openid)
            print(progress)
            if not progress["ok"]:
                result = progress["msg"]
            else:
                result = json.dumps(progress["content"])

        elif len(content) == 128:
            result = submit(openid, content)

        # elif(content.startswith("豹死空留皮一裘")):
        #     result = json.dumps(puzzle_record.unlock_token)

        elif content.startswith("查询提示列表"):
            query = content.strip().split(" ")
            if len(query) == 2:
                result = purchase.get_puzzle_list(query[1])
            else:
                result = "格式错误。示例：\n查询提示列表 第二道题（上）"

        elif content.startswith("查看提示"):
            query = content.strip().split(" ")
            if len(query) == 2:
                result = purchase.look_up_hint(openid, query[1])
            else:
                result = "格式错误。示例：\n查看提示 1"

        elif content.startswith("购买提示"):
            query = content.strip().split(" ")
            if len(query) == 2:
                result = purchase.purchase_hint(openid, query[1])
            else:
                result = "格式错误。示例：\n购买提示 1"

        elif content.startswith("查询积分"):
            result = purchase.check_credits(openid)

        # elif content == "图片测试":
        #     return JsonResponse(
        #         {
        #             "ToUserName": request["FromUserName"],
        #             "FromUserName": request["ToUserName"],
        #             "CreateTime": request["CreateTime"],
        #             "MsgType": "image",
        #             "Image":{
        #                 "MediaId" : 
        #             }
        #         },
        #         safe=False,
        #         json_dumps_params={"ensure_ascii": False},
        #     )
        elif content == "推送测试1":
            return JsonResponse(
                {
                    "ToUserName": request["FromUserName"],
                    "FromUserName": request["ToUserName"],
                    "CreateTime": request["CreateTime"],
                    "MsgType": "news",
                    "ArticleCount": 1,
                    "Articles": [
                        {
                            "Title": "Relax｜今日推荐音乐",
                            "Description": "每日推荐一个好听的音乐，感谢收听～",
                            "PicUrl": "https://y.qq.com/music/photo_new/T002R300x300M000004NEn9X0y2W3u_1.jpg?max_age=2592000",
                            "Url": "https://mellow-conkies-f83e36.netlify.app/",
                        }
                    ],
                },
                safe=False,
                json_dumps_params={"ensure_ascii": False},
            )
        elif content == "推送测试2":
            return JsonResponse(
                {
                    "ToUserName": request["FromUserName"],
                    "FromUserName": request["ToUserName"],
                    "CreateTime": request["CreateTime"],
                    "MsgType": "news",
                    "ArticleCount": 1,
                    "Articles": [
                        {
                            "Title": "test",
                            "Description": "每日推荐一个好听的音乐，感谢收听～",
                            "PicUrl": "http://mmbiz.qpic.cn/mmbiz_jpg/yvMGNJZUwCcOrBzr6W35cqodTQZRKpdnZh8Ej9nKlo9wXyTwG0nswuR8zWbTOe5mBfvIIcvNEIoO1po50ZUKWg/0?wx_fmt=jpeg",
                            "Url": "http://mp.weixin.qq.com/s?__biz=MzU0OTA4NTk1Mw==&mid=100000380&idx=1&sn=e7c7814aca5a59e83cb80a96534816bc&chksm=7bb474124cc3fd04c8bfb027c1926dda8311c1a5f2273e8f052fdcc8ca301e57f12945be1488#rd",
                        }
                    ],
                },
                safe=False,
                json_dumps_params={"ensure_ascii": False},
            )
            
        elif content == "推送测试3":
            return JsonResponse(
                {
                    "ToUserName": request["FromUserName"],
                    "FromUserName": request["ToUserName"],
                    "CreateTime": request["CreateTime"],
                    "MsgType": "news",
                    "ArticleCount": 1,
                    "Articles": [
                        {
                            "Title": "test",
                            "Description": "每日推荐一个好听的音乐，感谢收听～",
                            "PicUrl": "http://mmbiz.qpic.cn/mmbiz_jpg/yvMGNJZUwCcOrBzr6W35cqodTQZRKpdnZh8Ej9nKlo9wXyTwG0nswuR8zWbTOe5mBfvIIcvNEIoO1po50ZUKWg/0?wx_fmt=jpeg",
                            "Url": "https://www.zhihu.com",
                        }
                    ],
                },
                safe=False,
                json_dumps_params={"ensure_ascii": False},
            )

        else:
            result = simple_reply(content)

        if msgtype == "text":
            return JsonResponse(
                {
                    "ToUserName": request["FromUserName"],
                    "FromUserName": request["ToUserName"],
                    "CreateTime": request["CreateTime"],
                    "MsgType": "text",
                    "Content": result,
                },
                safe=False,
                json_dumps_params={"ensure_ascii": False},
            )
    except Exception as e:
        return JsonResponse({"msg": e.__repr__()})


def index(request, _):
    """
    获取主页

     `` request `` 请求对象
    """

    return JsonResponse({"hello": "world"})


def counter(request, _):
    """
    获取当前计数

     `` request `` 请求对象
    """

    rsp = JsonResponse(
        {"code": 0, "errorMsg": ""}, json_dumps_params={"ensure_ascii": False}
    )
    if request.method == "GET" or request.method == "get":
        rsp = get_count()
    elif request.method == "POST" or request.method == "post":
        rsp = update_count(request)
    else:
        rsp = JsonResponse(
            {"code": -1, "errorMsg": "请求方式错误"},
            json_dumps_params={"ensure_ascii": False},
        )
    logger.info("response result: {}".format(rsp.content.decode("utf-8")))
    return rsp


def get_count():
    """
    获取当前计数
    """

    try:
        data = Counters.objects.get(id=1)
    except Counters.DoesNotExist:
        return JsonResponse(
            {"code": 0, "data": 0}, json_dumps_params={"ensure_ascii": False}
        )
    return JsonResponse(
        {"code": 0, "data": data.count}, json_dumps_params={"ensure_ascii": False}
    )


def update_count(request):
    """
    更新计数，自增或者清零

    `` request `` 请求对象
    """

    logger.info("update_count req: {}".format(request.body))

    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    if "action" not in body:
        return JsonResponse(
            {"code": -1, "errorMsg": "缺少action参数"},
            json_dumps_params={"ensure_ascii": False},
        )

    if body["action"] == "inc":
        try:
            data = Counters.objects.get(id=1)
        except Counters.DoesNotExist:
            data = Counters()
        data.id = 1
        data.count += 1
        data.save()
        return JsonResponse(
            {"code": 0, "data": data.count}, json_dumps_params={"ensure_ascii": False}
        )
    elif body["action"] == "clear":
        try:
            data = Counters.objects.get(id=1)
            data.delete()
        except Counters.DoesNotExist:
            logger.info("record not exist")
        return JsonResponse(
            {"code": 0, "data": 0}, json_dumps_params={"ensure_ascii": False}
        )
    else:
        return JsonResponse(
            {"code": -1, "errorMsg": "action参数错误"},
            json_dumps_params={"ensure_ascii": False},
        )
