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
    "星与六十",
    "Meta: 龙绘",
    "Final Meta: 让我们的色彩为世间增添欢笑",
]

titles_to_num = {
    
}

i = 0
for title in titles:
    titles_to_num[title] = i
    i += 1
    
import json

total = json.load(open("hint.json", "r"))

# print(total)

def check(item):
    item["question"]
    item["id"] + 1
    item["content"]
    item["price"] + 10
    
total_items = []

for problem in total:
    problem_no = titles_to_num[problem]
    i = 0
    hint = total[problem]
    for item in hint:
        i += 1
        item["id"] = i + 100 * problem_no
        item["price"] = int(item["price"])
        check(item)
        # print(item)
        total_items.append(item)
        

"""
export "MYSQL_ADDRESS"="sh-cynosdbmysql-grp-j8d36gqe.sql.tencentcdb.com:28987"
export "MYSQL_PASSWORD"="DY89sdYz"
export "MYSQL_USERNAME"="root"

"""

import mysql.connector


# 打开数据库连接
db = mysql.connector.connect(user='root', password='DY89sdYz',
                              host='sh-cynosdbmysql-grp-j8d36gqe.sql.tencentcdb.com',
                              port = '28987',
                              database='django_demo')
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

sql =  ("INSERT INTO hint "
        "(id, price, content, question) "
        "VALUES (%s, %s, %s, %s)")



for item in total_items:
# 使用execute方法执行SQL语句
    print(item)
    cursor.execute(sql, (item["id"], item["price"], item["content"], item["question"]))


db.commit()
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetch()

cursor.close()
db.close()

