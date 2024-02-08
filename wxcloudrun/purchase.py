from .models import Purchase, Group, Hint, Skip

from .titles import  titles, purchaseable_titles, titles_to_num, credits, answers

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

import math

import time
import datetime

def get_time():
    return (time.time() - datetime.datetime(2024, 2, 8, 11, 0, 0, 0).timestamp())

def get_mercy():
    return int((get_time())/60) * 3

def get_normal_inflation():
    now = get_time()
    if(now >= 86400):
        return 1

    # print(6 ** ((86400 - now) / 86400))
    
    return 6 ** ((86400 - now) / 86400)
    
def get_additional_inflation():
    now = get_time()
    period0 = 86400
    period1 = 5 * 3600 + 4 * 86400
    
    if(now < period0):
        this_period = (period0 - now) / period0 
        return 18 * (3 ** this_period)
    
    if(now < period1):
        this_period = (period1 - now) / (period1 - period0) 
        return 3 * (6 ** this_period)
    
    return 3
    
    

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
    return int(hint.price * get_normal_inflation())

def get_credit(id: int):
    return int(credits[id] * get_normal_inflation())


@check_group
def check_credits(group: Group):
    # print(group)
    earn = group.credit
    consume = group.consumed
    mercy = get_mercy()
    
    return "队伍{} 累计获得{}龙币，消耗{}龙币，系统赠送{}龙币 余额{}龙币".format(group.id, earn, consume, mercy,earn - consume + mercy)
    
@check_group  
@use_hint
def look_up_hint(group, hintid):
    try:
        hintid = int(hintid)
    except:
        return "提示编号应该是数字"
    
    hint = Hint.objects.get(pk = hintid)
    
    if Purchase.objects.filter(group_id = group, hint_id = hint).exists():
        return hint.question+"\n"+hint.content
    else:
        return "尚未购买该提示。输入「购买提示 {}」后尝试".format(hintid)
    
def get_answer_price(title):
    if title not in purchaseable_titles :
        return "题目不存在或不支持购买答案"
    
    question_id = titles_to_num[title]
    price = int(get_additional_inflation() * credits[question_id])
    return "{}龙币".format(price)


@check_group
def purchase_answer(group: Group, title):
    if title not in purchaseable_titles :
        return "题目不存在或不支持购买答案"
    
    question_id = titles_to_num[title]
    price = int(get_additional_inflation() * credits[question_id])
    
    answer = answers[question_id][0]
    
    
    if Skip.objects.filter(group_id = group, question_id = question_id).exists():
        return "你或你的队友已购买该答案\n" + answer
    
    
    balance = get_balance(group)

    if (balance < price):
        return "龙币余额不足，需要{}龙币, 当前余额是{}龙币".format(price, balance)
    
    group.consumed += price
    group.exitable = False
    
    order = Skip(group_id=group, question_id = question_id, cost=price)
    
    order.save()
    group.save()
    
    return "购买{}的答案成功，当前余额{}\n{}".format(title, balance - price, answer)
    

@check_group
@use_hint
def purchase_hint(group: Group, hintid):
    try:
        hintid = int(hintid)
    except:
        return "提示编号应该是数字"
    hint = Hint.objects.get(pk = hintid)
    
    if Purchase.objects.filter(group_id = group, hint_id = hint).exists():
        return "你或你的队友已购买该提示\n" + hint.question+"\n"+hint.content
    
    balance = get_balance(group)
    price = get_price(hint)
    if (balance < price):
        return "龙币余额不足，需要{}龙币, 当前余额是{}龙币".format(price, balance)
    
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
            result+= "    {} {}龙币 编号{}\n".format(
                  hint.question,get_price(hint),hint.id
            )
            hint_id += 1
        except:
            break
        
    return result
    
