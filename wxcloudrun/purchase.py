from .models import Purchase, Group, Hint

from .puzzle_record import  titles

import re


def get_chinese_only(a):
    return re.sub(r'[^\u4e00-\u9fa5]', '', a)

i = 0
chinese_only_to_id = {}
chinese_only_to_original = {}

for item in titles:
    chinese_only_to_id[get_chinese_only(item)] = i
    chinese_only_to_original[get_chinese_only(item)] = item
    i += 1
    
from .user import get_group_id_lock
from functools import wraps


from django.db import transaction



import time
import datetime
def get_mercy():
    return int((time.time() - datetime.datetime(2024, 2, 3, 10, 0, 0, 0).timestamp())/60)
    

def check_group(func):
    @wraps(func)
    @transaction.atomic
    def wrapper(openid, *args, **kwargs):
        try:
            group = get_group_id_lock(openid)
            result = func(group, *args, **kwargs)
            return result
        except Group.DoesNotExist:
            return "请先加入或创建队伍"
        except Exception as e:
            return str(e)
    return wrapper

def use_hint(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Hint.DoesNotExist:
            return "该提示不存在"
    return wrapper
    
def get_balance(group: Group):
    return group.credit - group.consumed + get_mercy()

def get_price(hint: Hint):
    return hint.price

@check_group
def check_credits(group: Group):
    print(group)
    earn = group.credit
    consume = group.consumed
    mercy = get_mercy()
    
    return "队伍{} 累计获得{}分，消耗{}分，系统赠送{}分 余额{}分".format(group.id, earn, consume, mercy,earn - consume + mercy)
    
@check_group  
@use_hint
def look_up_hint(group, hintid):
    hintid = int(hintid)
    hint = Hint.objects.get(pk = hintid)
    
    if Purchase.objects.filter(group_id = group, hint_id = hint).exists():
        return hint.question+"\n"+hint.content
    else:
        return "尚未购买该提示。输入「购买提示 {}」后尝试".format(hintid)
    
    

@check_group
@use_hint
def purchase_hint(group: Group, hintid):
    hintid = int(hintid)
    hint = Hint.objects.get(pk = hintid)
    
    if Purchase.objects.filter(group_id = group, hint_id = hint).exists():
        return "业已购买该提示\n" + hint.question+"\n"+hint.content
    
    balance = get_balance(group)
    price = get_price(hint)
    if (balance < price):
        return "积分余额不足，需要{}积分, 当前余额是{}积分".format(price, balance)
    
    group.consumed += price
    group.exitable = False
    
    order = Purchase(group_id=group, hint_id=hint, cost=price)
    
    order.save()
    group.save()
    
    return "购买提示{}成功，当前余额{}\n{}\n{}".format(hintid, balance - price, hint.question, hint.content)
    
    

def get_puzzle_list(name):
    puzzle_id = chinese_only_to_id[get_chinese_only(name)]
    result = chinese_only_to_original[get_chinese_only(name)] + ":\n"
    
    hint_id = puzzle_id * 100 + 1
    
    while(True):
        try:
            hint = Hint.objects.get(pk = hint_id)
            result+= "    {} {}积分 编号{}\n".format(
                  hint.question,get_price(hint),hint.id
            )
            hint_id += 1
        except:
            break
        
    return result
    