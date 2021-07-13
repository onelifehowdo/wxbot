import logging
import traceback

import pymysql
import string
import time
import threading

class ctrMsg:
    def __init__(self,ctr,msg):
        self.ctr=ctr
        self.msg=msg


class sqliteControl(threading.Thread):

    MsgQueue = []
    rsp={}#响应标志

    def __init__(self):
        threading.Thread.__init__(self)

    def add(cls, i):
        cls.MsgQueue.append(i)

    def run(cls):
        while True:
            conn=pymysql.connect(host="120.26.54.146",user="wxwork_message",passwd="6CmnpPoS1jwIM%5g",db="wxwork_message")
            tableName="ALLmessage"
            print("全部消息数据库打开成功")
            try:
                while True:
                    if len(cls.MsgQueue) > 0:
                        conn.ping()
                        Q_msg = cls.MsgQueue.pop(0)

                        cpId=Q_msg.cpId
                        cpName=Q_msg.cpName
                        speakerId=Q_msg.speakid
                        speaker=Q_msg.speaker
                        text=Q_msg.text
                        time=Q_msg.time

                        cursor = conn.cursor()
                        sql = 'INSERT INTO %s(cpid,cpname,speakid,speaker,text,time) values ("%s","%s","%s","%s","%s",%d)'
                        data = (tableName, cpId, cpName, speakerId, speaker, text, time)
                        cursor.execute(str.format(sql % data))
                        conn.commit()
                        cursor.close()

            except Exception as e:
                # conn.rollback()
                # logging.getLogger("sql").error(traceback.format_exc())
                print("全部消息数据库断联")
                continue
                pass
            finally:
                if not conn is None:
                    conn.close()
                    print("全部消息数据库关闭")