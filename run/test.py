# import time
# week = time.strftime('%a', time.localtime())
# hor=int(time.strftime('%H', time.localtime()))
# print(week)
# print(hor)
# if not week in ["Sat", "Sun"]:
#     # 非工作日
#     pass
# else:
#     pass


import pymysql

CP = {}
conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
print("正在读取公司员工")
cursor = conn.cursor()
sql = 'SELECT rid,groupname FROM wxwork_message.groupnote'
cursor.execute(sql)
r = cursor.fetchall()
for i in r:
    CP[i[0]] = i[1]
conn.commit()
cursor.close()
conn.close()
