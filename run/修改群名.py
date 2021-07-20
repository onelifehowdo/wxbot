import os
import time
import re
import Config
import pymysql
from pymysql.converters import escape_string
conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
sql = 'SELECT rid,groupname FROM wxwork_message.groupnote'
cursor = conn.cursor()
cursor.execute(sql)
r = cursor.fetchall()
for i in r:
    cpid = i[0]
    cpname = i[1]
    sql1 = 'update wxwork_message.msg set cpname="%s" where cpid="%s"'
    sql2 = 'update wxwork_message.ALLmessage set cpname="%s" where cpid="%s"'
    cursor.execute(str.format(sql1 % (cpname, cpid)))
    cursor.execute(str.format(sql2 % (cpname, cpid)))
    print(cpname)
conn.commit()
cursor.close()
conn.close()
input("修改完成！")