import os
import time
import re
import Config
import pymysql
from pymysql.converters import escape_string
import requests
import json
import threading
import init


def makeText(cursor, name):
    msgNum = 0
    msg = ""
    proNum = 0
    pro = ""
    sql = str.format(
        'SELECT cpname FROM wxwork_message.msg WHERE engineer="%s" and type="message" and status=0 GROUP BY cpid' % name)
    cursor.execute(sql)
    msgList = cursor.fetchall()
    sql = str.format(
        'SELECT cpname FROM wxwork_message.msg WHERE engineer="%s" and type="problem" and status=0 GROUP BY cpid' % name)
    cursor.execute(sql)
    proList = cursor.fetchall()

    if len(msgList) != 0:
        msgNum = len(msgList)
        mList = ["> " + i[0] + "\n" for i in msgList]
        for i in mList:
            msg += i

    if len(proList) != 0:
        proNum = len(proList)
        mList = ["> " + i[0] + "\n" for i in proList]
        for i in mList:
            pro += i

    if msgNum != 0:
        msg = str.format("**未响应消息群数[%d]**\n%s\n" % (msgNum, msg))
    if proNum != 0:
        pro = str.format("**未解决问题群数[%d]**\n%s" % (proNum, pro))
    flag = not (msgNum == 0 and proNum == 0)
    text = msg + pro
    return flag, text

init.init()
conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
cursor = conn.cursor()
for name in Config.staffList:
    try:
        r, text = makeText(cursor, name)
    except Exception as e:
        continue
    finally:
        pass
    if r:
        timeText=str.format("<font color=\"comment\">%s</font>\n" % time.strftime('%Y-%m-%d %H:%M', time.localtime()))
        text = "# "+name+"\n" + text+"\n"+timeText
        data = {"msgtype": "markdown", "markdown": {}}
        murl = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e6850cdf-a31a-48e5-bd46-2a7d92160af7"
        data["markdown"]["content"] = text
        r = requests.post(url=murl, data=json.dumps(data))
        print(r.text)
cursor.close()
conn.close()
