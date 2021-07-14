import pymysql
import os


def checkmessage():
    os.system("cls")
    name = input("消息查询，输入姓名：")
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    cursor = conn.cursor()
    sql = str.format('SELECT * FROM msg where engineer="%s" and type="message" and status=0 group by cpid' % name)
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        print("[" + i[2], end="]")
        print(i[5])
    else:
        print("共%d条消息" % len(r))
    conn.close()


def checkproblem():
    os.system("cls")
    name = input("问题查询，输入姓名：")
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    cursor = conn.cursor()
    sql = str.format('SELECT * FROM msg where engineer="%s" and type="problem" and status=0 group by cpid' % name)
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        print("[" + i[2], end="]")
        print(i[5])
    else:
        print("共%d条问题" % len(r))
    conn.close()


def checkALLmessage():
    os.system("cls")
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    cursor = conn.cursor()
    sql = str.format('SELECT * FROM msg where type="message" and status=0 group by cpid')
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        print("[" + i[2], end="]")
        print(i[5] + "--->" + i[10])
    else:
        print("共%d条消息" % len(r))
    conn.close()


def checkALLproblem():
    os.system("cls")
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    cursor = conn.cursor()
    sql = str.format('SELECT * FROM msg where type="problem" and status=0 group by cpid')
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        print("[" + i[2], end="]")
        print(i[5] + "--->" + i[10])
    else:
        print("共%d条问题" % len(r))
    conn.close()


while True:
    os.system("color 02")
    print("-"*22)
    print("|[1]:查询自己未响应的消息|")
    print("|[2]:查询自己未解决的问题|")
    print("|[3]:查询所有人未响应消息|")
    print("|[4]:查询所有人未解决问题|")
    print("-" * 22)
    i = int(input("输入指令：\n"))
    if i == 1:
        checkmessage()
    elif i == 2:
        checkproblem()
    elif i == 3:
        checkALLmessage()
    elif i == 4:
        checkALLproblem()