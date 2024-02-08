from .titles import unlock_token, titles_to_num, titles, record, credits
    
from wxcloudrun.models import Group, GroupBelong, Purchase
from .purchase import get_balance, get_credit

time_epoch = 17_0000_0000_000_000
     
def get_next(i):
    if(i == 0):
        return[1,2,11]
    if(i == 1):
        return[3,4,12]
    if(i == 2):
        return[3,4,13]
    if(i == 3):
        return[5,6,7,14]
    if(i == 4):
        return[5,6,7,15]
    if(i == 5):
        return[16]
    if(i == 6):
        return[17]
    if(i == 7):
        return[18]
    if(i == 8):
        return[19]
    if(i == 10):
        return[11,12,1]
    if(i == 11):
        return[13,14,2]
    if(i == 12):
        return[13,14,3]
    if(i == 13):
        return[15,16,17,4]
    if(i == 14):
        return[15,16,17,5]
    if(i == 15):
        return[6]
    if(i == 16):
        return[7]
    if(i == 17):
        return[8]
    if(i == 18):
        return[9]
    return []


def get_progress(group):

    try:
        passes = [False] * 21
        
        if group.t0 and group.t0 > time_epoch:
            passes[0] = True

        if group.t1 and group.t1 > time_epoch:
            passes[1] = True

        if group.t2 and group.t2 > time_epoch:
            passes[2] = True

        if group.t3 and group.t3 > time_epoch:
            passes[3] = True

        if group.t4 and group.t4 > time_epoch:
            passes[4] = True

        if group.t5 and group.t5 > time_epoch:
            passes[5] = True

        if group.t6 and group.t6 > time_epoch:
            passes[6] = True

        if group.t7 and group.t7 > time_epoch:
            passes[7] = True

        if group.t8 and group.t8 > time_epoch:
            passes[8] = True

        if group.t9 and group.t9 > time_epoch:
            passes[9] = True

        if group.t10 and group.t10 > time_epoch:
            passes[10] = True

        if group.t11 and group.t11 > time_epoch:
            passes[11] = True

        if group.t12 and group.t12 > time_epoch:
            passes[12] = True

        if group.t13 and group.t13 > time_epoch:
            passes[13] = True

        if group.t14 and group.t14 > time_epoch:
            passes[14] = True

        if group.t15 and group.t15 > time_epoch:
            passes[15] = True

        if group.t16 and group.t16 > time_epoch:
            passes[16] = True

        if group.t17 and group.t17 > time_epoch:
            passes[17] = True

        if group.t18 and group.t18 > time_epoch:
            passes[18] = True

        if group.t19 and group.t19 > time_epoch:
            passes[19] = True

        if group.t20 and group.t20 > time_epoch:
            passes[20] = True
            
        unlocks = passes.copy()
        
        unlocks[0] = True
        unlocks[10] = True
        
        for i in range(20):
            if (passes[i]):
                for j in get_next(i):
                    unlocks[j] = True

        part1_pass = 0
        part2_pass = 0
        
        for i in range(9):
            if(passes[i]):
                part1_pass += 1
            if(passes[i + 10]):
                part2_pass += 1
            
        if(part1_pass >= 5):
            unlocks[9] = True
        
        if(part2_pass >= 5):
            unlocks[19] = True
            
        if(passes[9] and passes[19]):
            unlocks[20] = True
            
        part1_unlock = 0
        part2_unlock = 0
        
        for i in range(8):
            if(unlocks[i]):
                part1_unlock += 1
            if(unlocks[i + 10]):
                part2_unlock += 1
        
        if(part1_unlock >= 5):
            unlocks[8] = True
        
        if(part2_unlock >= 5):
            unlocks[18] = True
            
            
        return {
            "ok" : True,
            "content" : [
                (unlock_token[i] if unlocks[i] else "") for i in range(21)
            ],
            "msg": "success"
        }
        
    except Exception as e:
        return {"ok": False, "content": [], "msg": e.__repr__()}



def handle_submit(group, time, question):
    # print(group, time, question)
    try:

        try:
            question_id = record[str(question)]
        except:
            raise Exception("id为{}的题目不存在".format(question_id))

        group.exitable = False
        
        old_credit = group.credit
        
        if question_id == 0:
            if group.t0 == None or group.t0 > int(time):
                if(group.t0 == None):
                    group.credit += get_credit(0)
                group.t0 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 1:
            if group.t1 == None or group.t1 > int(time):
                if(group.t1 == None):
                    group.credit += get_credit(1)
                group.t1 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 2:
            if group.t2 == None or group.t2 > int(time):
                if(group.t2 == None):
                    group.credit += get_credit(2)
                group.t2 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 3:
            if group.t3 == None or group.t3 > int(time):
                if(group.t3 == None):
                    group.credit += get_credit(3)
                group.t3 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 4:
            if group.t4 == None or group.t4 > int(time):
                if(group.t4 == None):
                    group.credit += get_credit(4)
                group.t4 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 5:
            if group.t5 == None or group.t5 > int(time):
                if(group.t5 == None):
                    group.credit += get_credit(5)
                group.t5 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 6:
            if group.t6 == None or group.t6 > int(time):
                if(group.t6 == None):
                    group.credit += get_credit(6)
                group.t6 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 7:
            if group.t7 == None or group.t7 > int(time):
                if(group.t7 == None):
                    group.credit += get_credit(7)
                group.t7 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 8:
            if group.t8 == None or group.t8 > int(time):
                if(group.t8 == None):
                    group.credit += get_credit(8)
                group.t8 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 9:
            if group.t9 == None or group.t9 > int(time):
                if(group.t9 == None):
                    group.credit += get_credit(9)
                group.t9 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 10:
            if group.t10 == None or group.t10 > int(time):
                if(group.t10 == None):
                    group.credit += get_credit(10)
                group.t10 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 11:
            if group.t11 == None or group.t11 > int(time):
                if(group.t11 == None):
                    group.credit += get_credit(11)
                group.t11 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 12:
            if group.t12 == None or group.t12 > int(time):
                if(group.t12 == None):
                    group.credit += get_credit(12)
                group.t12 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 13:
            if group.t13 == None or group.t13 > int(time):
                if(group.t13 == None):
                    group.credit += get_credit(13)
                group.t13 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 14:
            if group.t14 == None or group.t14 > int(time):
                if(group.t14 == None):
                    group.credit += get_credit(14)
                group.t14 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 15:
            if group.t15 == None or group.t15 > int(time):
                if(group.t15 == None):
                    group.credit += get_credit(15)
                group.t15 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 16:
            if group.t16 == None or group.t16 > int(time):
                if(group.t16 == None):
                    group.credit += get_credit(16)
                group.t16 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 17:
            if group.t17 == None or group.t17 > int(time):
                if(group.t17 == None):
                    group.credit += get_credit(17)
                group.t17 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 18:
            if group.t18 == None or group.t18 > int(time):
                if(group.t18 == None):
                    group.credit += get_credit(18)
                group.t18 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 19:
            if group.t19 == None or group.t19 > int(time):
                if(group.t19 == None):
                    group.credit += get_credit(19)
                group.t19 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 20:
            if group.t20 == None or group.t20 > int(time):
                if(group.t20 == None):
                    group.credit += get_credit(20)
                group.t20 = int(time)
                group.save()
            else:
                return "已有更早的提交"

            
        return "成功提交unix时间戳为{}的题目 {} 本次获得龙币{}, 余额{}".format(int(time) / 1000000, titles[question_id], group.credit - old_credit,get_balance(group)  )

    except Exception as e:
        return "提交失败， {}".format(e.__repr__())
