import json
import logging
import traceback
from logging import handlers
import time

import pymysql
import Config
import threading
import requests


class check(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        while True:
            try:
                hz_at = {
                    "朱天华": "zhutianhua",
                    "孙志鹏": "sunzhipeng",
                    "盛玉霞": "shengxia",
                    "沈园园": "shenyuanyuan",
                    "祝平军": "zhupingjun",
                    "王海洋": "wanghaiyang",
                    "曲振": "quzhen",
                    "邓海": "denghai",
                    "谭立元": "tanliyuan",
                    "郑治": "zhengzhi",
                    "廖瑞": "liaorui",
                    "周维华": "zhouweihau",
                    "孙张鑫": "sunzhangxin",
                    "小助理": "xiaozhushou",
                    "伍珈沁": "wujiaqin",
                    "王磊": "wanglei",
                    "谢萧辉": "xiexiaohui",
                    "刘嘉诚": "liujiacheng",
                    "黄何":"huanghe"
                }
                #
                murl="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b8acdfc2-45eb-41d8-8a09-e2162e21477b"

                conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
                table = "msg"

                cursor = conn.cursor()
                for starf in Config.staffList:
                    text=""
                    data = {
                        "msgtype": "text",
                        "text": {
                            "content": "",
                            "mentioned_list": []
                        }
                    }
                    sql=str.format('SELECT * FROM %s WHERE engineer="%s" and type="message" and status=0 GROUP BY cpid' % (table,starf))
                    cursor.execute(sql)
                    r=cursor.fetchall()
                    if len(r) >0:
                        text+=str.format("未响应消息群数:[%d]\n" %len(r))
                        for i in r:
                            text=text+i[2]+"\n"

                    sql = str.format('SELECT * FROM %s WHERE engineer="%s" and type="problem" and status=0 GROUP BY cpid' % (table, starf))
                    cursor.execute(sql)
                    r = cursor.fetchall()
                    if len(r)>0:
                        text+="-"*49+"\n"
                        text+=str.format("未解决问题群数:[%d]\n" % len(r))
                        for i in r:
                            text+=i[2]+"\n"

                    if text !="":
                        text += time.strftime('%Y-%m-%d %H:%M', time.localtime())
                        data["text"]["content"] = text
                        data["text"]["mentioned_list"].append(hz_at[starf])
                        r = requests.post(url=murl, data=json.dumps(data))
                        # print(r.text)
                cursor.close()
                conn.close()
                time.sleep(60*5)
            finally:
                pass
        pass