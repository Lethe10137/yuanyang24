from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名

class Group(models.Model):
    
    class Meta:
        db_table = 'Group'  # 数据库表名
    # 自增主键
    id = models.AutoField(primary_key=True)
    
    token = models.IntegerField(null = True)
    token_expire = models.DateTimeField(null = True)
    
    credit = models.IntegerField(default = 0)
    exitable = models.BooleanField(default = True)
    
    # T0到T20的21个字段，类型是bigint，初始值为null
    t0 = models.BigIntegerField(null=True)
    t1 = models.BigIntegerField(null=True)
    t2 = models.BigIntegerField(null=True)
    t3 = models.BigIntegerField(null=True)
    t4 = models.BigIntegerField(null=True)
    t5 = models.BigIntegerField(null=True)
    t6 = models.BigIntegerField(null=True)
    t7 = models.BigIntegerField(null=True)
    t8 = models.BigIntegerField(null=True)
    t9 = models.BigIntegerField(null=True)
    t10 = models.BigIntegerField(null=True)
    t11 = models.BigIntegerField(null=True)
    t12 = models.BigIntegerField(null=True)
    t13 = models.BigIntegerField(null=True)
    t14 = models.BigIntegerField(null=True)
    t15 = models.BigIntegerField(null=True)
    t16 = models.BigIntegerField(null=True)
    t17 = models.BigIntegerField(null=True)
    t18 = models.BigIntegerField(null=True)
    t19 = models.BigIntegerField(null=True)
    t20 = models.BigIntegerField(null=True)
    
    # 名叫member1, member2, member3, member4, member5的五个字段，内容应该是groupbelong中的自增主键，初始值为null
    member1 = models.ForeignKey('GroupBelong', related_name='member1', on_delete=models.SET_NULL, null=True)
    member2 = models.ForeignKey('GroupBelong', related_name='member2', on_delete=models.SET_NULL, null=True)
    member3 = models.ForeignKey('GroupBelong', related_name='member3', on_delete=models.SET_NULL, null=True)
    member4 = models.ForeignKey('GroupBelong', related_name='member4', on_delete=models.SET_NULL, null=True)
    member5 = models.ForeignKey('GroupBelong', related_name='member5', on_delete=models.SET_NULL, null=True)

class GroupBelong(models.Model):
    
    class Meta:
        db_table = 'GroupBelong'  # 数据库表名
    # 自增主键
    id = models.AutoField(primary_key=True)
    
    # OPENID, 是一个长度不超过64的字符串
    openid = models.CharField(max_length=64, unique=True)
    
    # GROUP_ID, 是第二张表中的自增主键
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE, null = True)
    

class Purchase(models.Model):
    
    class Meta:
        db_table = 'Purchase'  # 数据库表名
        
    id = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(default=datetime.now(),)
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE)
    hint_id = models.IntegerField()
    cost = models.PositiveIntegerField()
        
        