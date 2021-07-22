import os
import time
import re
import Config
import pymysql
from pymysql.converters import escape_string

conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
sql = 'SELECT *FROM wxwork_message.staff where rid is  NULL'
cursor = conn.cursor()
cursor.execute(sql)
r = cursor.fetchall()
print("没有记录RID的员工：")
print("-*-" * 2)
for i in r:
    name = i[2]
    if len(name) == 2:
        name = name[0] + " " + name[1]
    print(name)
    print("-*-" * 2)
else:
    print("正在扫描发言过的员工")
for i in r:
    name = i[2]
    sql1 = 'SELECT * FROM wxwork_message.ALLmessage where speaker="' + name + '" limit 1'
    cursor.execute(sql1)
    re = cursor.fetchone()
    if re is not None:
        print(name)
        id = re[3]
        sql3 = 'update wxwork_message.staff set rid="%s" where name="%s"'
        cursor.execute(str.format(sql3 % (id, name)))
conn.commit()
cursor.close()
conn.close()
