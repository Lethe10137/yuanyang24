
for i in range(21):
    print("""
        if question_id == {}:
            if group.t{} == None or group.t{} > int(time):
                if(group.t{} == None):
                    group.credit += credits[{}]
                group.t{} = int(time)
                group.save()
            else:
                return "已有更早的提交"
""".format(i,i,i,i,i,i))
    
    
exit(0)
for i in range(21):
    print("""
if (group.t{} and group.t{} > time_epoch):
            passes[{}] = True
""".format(i,i,i))