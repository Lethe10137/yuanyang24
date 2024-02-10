from wxcloudrun.models import Group, GroupBelong, Purchase
from django.db import transaction
import random
from datetime import datetime, timedelta

def exit_group(open_id):
    user = get_user(open_id)
    
    if (user.group_id != None):
        original_group = user.group_id
    else:
        return "当前不在任何队伍中"
    
    if(original_group.exitable):
        with transaction.atomic():
            if original_group.member1 == user:
                original_group.member1 = None
            elif original_group.member2 == user:
                original_group.member2 = None
            elif original_group.member3 == user:
                original_group.member3 = None
            elif original_group.member4 == user:
                original_group.member4 = None
            elif original_group.member5 == user:
                original_group.member5 = None
            original_group.save()
            user.group_id = None
            user.save()
    else:
        raise Exception("所在队伍{}有提交或购买记录，不能退出！".format(original_group.id))

    return "成功退出队伍{}".format(original_group.id)
    
    
def get_group_id(open_id):
    user = get_user(open_id)
    if (user.group_id):
        return user.group_id
    raise Exception("请先加入或创建队伍")

def get_group_id_lock(open_id):
    user = get_user(open_id)
    if (user.group_id):
        return Group.objects.select_for_update().get(pk = user.group_id.id)
    raise Exception("请先加入或创建队伍")



def join_group(open_id,  group_id, token):
    user : GroupBelong = get_user(open_id)

    with transaction.atomic():
        if (user.group_id != None):
            raise Exception("请先退出队伍")

        try:
            group = Group.objects.get(pk = group_id)
        except:
            raise Exception("队伍不存在")
        
            
        if datetime.now() > group.token_expire:
            return "验证码过期"
        
        if token != group.token:
            return "验证码错误"
    
        
        user.group_id = group
        if group.member1 is None:
            group.member1 = user
            group.save()
            user.save()
        elif group.member2 is None:
            group.member2 = user
            group.save()
            user.save()
        elif group.member3 is None:
            group.member3 = user
            group.save()
            user.save()
        # elif group.member4 is None:
        #     group.member4 = user
        #     group.save()
        #     user.save()
        # elif group.member5 is None:
        #     group.member5 = user
        #     group.save()
        #     user.save()
        else:
            # 如果没有空位，则撤销对group和groupbelong的任何修改
            raise Exception("队伍已满")

    
    return "成功加入队伍{}".format(group_id)

    
def get_user(openid) -> GroupBelong:
    user = GroupBelong.objects.get_or_create(openid = openid,
        defaults= {
            'group_id' : None
        }                                     
        )

    return user[0]
        
        
        

def create_group(open_id):
    user : GroupBelong = get_user(open_id)

    with transaction.atomic():
        if (user.group_id != None):
            raise Exception("请先退出队伍")
        

        new_group = Group.objects.create(
            token = None,
            token_expire = None
            ,t0=None, t1=None, t2=None, t3=None, t4=None, t5=None, t6=None, t7=None, t8=None, t9=None, t10=None, t11=None, t12=None, t13=None, t14=None, t15=None, t16=None, t17=None, t18=None, t19=None, t20=None)
        user.group_id = new_group
        user.save()
        new_group.member1 = user
        new_group.save()
        
    return "成功创建并加入队伍 {}".format(new_group.id)


def create_token(open_id):
    user : GroupBelong = get_user(open_id)
    # print(user)
    if (user.group_id != None):
        current_group = user.group_id
    else:
        return "当前不在任何队伍中"
    
    token = random.randrange(0, 99999999)
    current_group.token = token
    current_group.token_expire = datetime.now() + timedelta(minutes= 10)
    current_group.save()
    
    return "队伍{}现在的验证码是{}, 10分钟内有效".format(current_group.id,str(token).zfill(8))
