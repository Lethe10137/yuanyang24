record = {
    "1388807464596341962": 0,
    "11686835270657773399": 1,
    "17742894046869862114": 2,
    "13315301355602027825": 3,
    "4004308219571680113": 4,
    "1438134505462242192": 5,
    "7062578419350324245": 6,
    "16558917729305874029": 7,
    "2407402883759763646": 8,
    "12663528655678229537": 9,
    "1168440978755831426": 10,
    "9142045337100104095": 11,
    "16708055074147356504": 12,
    "11688901659336124162": 13,
    "2567163264753946024": 14,
    "15562051808872901398": 15,
    "12235079986515827170": 16,
    "4230642811140312531": 17,
    "10249401992574644714": 18,
    "4634412375863893641": 19,
    "117029381625775928": 20,
}

titles = [
    "第二道题（上）",
    "格线之间",
    "深入龙穴",
    "出题事故",
    "双盲实验",
    "命名有道",
    "大调钢琴",
    "作文考试",
    "奇怪的问卷",
    "Meta: 龙说",
    "第二道题（下）",
    "国画",
    "仓颉造字",
    "迷宫? 迷宫！",
    "八法恒久远",
    "笨龙笨事",
    "//只有.三个.词语",
    "龙的笔记本",
    "六十律",
    "Meta: 龙绘",
    "Final Meta:笑",
]

from wxcloudrun.models import Group, GroupBelong, Purchase

time_epoch = 17_0000_0000_000_000

unlock_token = ['5ace_5671_8799_47b7_ce9e_fe662b1f', '4891_c0b5_beb2_3697_b959_1480a23c', '7511_910b_87b1_f284_1c2b_1e005879', '8cb2_efe8_7983_8253_3275_1315cc21', 'f96f_38b0_cec1_1941_45ed_db4008c6', '3b2c_7fed_eead_05a0_549a_d3560ade', 'acc6_c4c2_f285_943b_1864_30ff9195', '6e8d_11cd_d618_7757_9239_f8fd1410', '04eb_e582_d3d8_8565_9c94_00000000', '33ce_f38d_4b05_2803_adda_00000000', '9398_2f87_f199_ce70_2006_2482caa5', '6a23_bf14_0510_f496_b7f5_ceca85bd', 'b645_ede3_d80b_fe09_d989_266febde', '42af_a7b5_23a8_6c9c_e91b_f5ddaf52', '66c1_d34b_9d86_7361_e46e_1942a7e4', '05c3_9123_e839_d489_8ede_f89fb128', 'ff6d_089b_968a_4879_da7c_30574808', 'cb01_5d31_9ec4_6f25_7c17_5cfb34ca', 'a00b_d875_9662_30ee_35f4_00000000', '5656_a54b_fc87_c8c1_e4a3_00000000', '90a79407ebf022a3092f1c27f3b56d79']
       
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

credits = [
    300,200,300,400,500,600,600,600,800,300,300,200,300,400,600,700,800,1200,300,10000
]

def handle_submit(group, time, question):
    print(group, time, question)
    try:

        try:
            question_id = record[str(question)]
        except:
            raise Exception("id为{}的题目不存在".format(question_id))

        group.exitable = False
        
        if question_id == 0:
            if group.t0 == None or group.t0 > int(time):
                if(group.t0 == None):
                    group.credit += credits[0]
                group.t0 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 1:
            if group.t1 == None or group.t1 > int(time):
                if(group.t1 == None):
                    group.credit += credits[1]
                group.t1 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 2:
            if group.t2 == None or group.t2 > int(time):
                if(group.t2 == None):
                    group.credit += credits[2]
                group.t2 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 3:
            if group.t3 == None or group.t3 > int(time):
                if(group.t3 == None):
                    group.credit += credits[3]
                group.t3 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 4:
            if group.t4 == None or group.t4 > int(time):
                if(group.t4 == None):
                    group.credit += credits[4]
                group.t4 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 5:
            if group.t5 == None or group.t5 > int(time):
                if(group.t5 == None):
                    group.credit += credits[5]
                group.t5 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 6:
            if group.t6 == None or group.t6 > int(time):
                if(group.t6 == None):
                    group.credit += credits[6]
                group.t6 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 7:
            if group.t7 == None or group.t7 > int(time):
                if(group.t7 == None):
                    group.credit += credits[7]
                group.t7 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 8:
            if group.t8 == None or group.t8 > int(time):
                if(group.t8 == None):
                    group.credit += credits[8]
                group.t8 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 9:
            if group.t9 == None or group.t9 > int(time):
                if(group.t9 == None):
                    group.credit += credits[9]
                group.t9 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 10:
            if group.t10 == None or group.t10 > int(time):
                if(group.t10 == None):
                    group.credit += credits[10]
                group.t10 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 11:
            if group.t11 == None or group.t11 > int(time):
                if(group.t11 == None):
                    group.credit += credits[11]
                group.t11 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 12:
            if group.t12 == None or group.t12 > int(time):
                if(group.t12 == None):
                    group.credit += credits[12]
                group.t12 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 13:
            if group.t13 == None or group.t13 > int(time):
                if(group.t13 == None):
                    group.credit += credits[13]
                group.t13 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 14:
            if group.t14 == None or group.t14 > int(time):
                if(group.t14 == None):
                    group.credit += credits[14]
                group.t14 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 15:
            if group.t15 == None or group.t15 > int(time):
                if(group.t15 == None):
                    group.credit += credits[15]
                group.t15 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 16:
            if group.t16 == None or group.t16 > int(time):
                if(group.t16 == None):
                    group.credit += credits[16]
                group.t16 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 17:
            if group.t17 == None or group.t17 > int(time):
                if(group.t17 == None):
                    group.credit += credits[17]
                group.t17 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 18:
            if group.t18 == None or group.t18 > int(time):
                if(group.t18 == None):
                    group.credit += credits[18]
                group.t18 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 19:
            if group.t19 == None or group.t19 > int(time):
                if(group.t19 == None):
                    group.credit += credits[19]
                group.t19 = int(time)
                group.save()
            else:
                return "已有更早的提交"


        if question_id == 20:
            if group.t20 == None or group.t20 > int(time):
                if(group.t20 == None):
                    group.credit += credits[20]
                group.t20 = int(time)
                group.save()
            else:
                return "已有更早的提交"

            
        return "成功提交unix时间戳为{}的题目 {} 目前积分{}".format(int(time) / 1000000, titles[question_id], group.credit)

    except Exception as e:
        return "提交失败， {}".format(e.__repr__())
