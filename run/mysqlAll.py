import logging
import traceback

import pymysql
import string
import time as ModelTime
import threading
import Config
import myTools


class ctrMsg:
    def __init__(self, ctr, msg):
        self.ctr = ctr
        self.msg = msg


class sqliteControl(threading.Thread):
    MsgQueue = []
    rsp = {}  # 响应标志

    def __init__(self):
        threading.Thread.__init__(self)

    @classmethod
    def add(cls, i):
        cls.MsgQueue.append(i)

    @classmethod
    def run(cls):
        while True:
            if Config.EVENTFLAG.is_set():
                break
            conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g",
                                   db="wxwork_message")
            tableName = "ALLmessage"
            print("全部消息数据库打开成功")
            try:
                while True:
                    if Config.EVENTFLAG.is_set():
                        raise Exception("全部消息线程" + "主动退出")
                    if len(cls.MsgQueue) > 0:
                        conn.ping()
                        Q_msg = cls.MsgQueue.pop(0)

                        cpId = Q_msg.cpId
                        cpName = Q_msg.cpName
                        speakerId = Q_msg.speakid
                        speaker = Q_msg.speaker
                        text = Q_msg.text
                        time = Q_msg.time

                        cursor = conn.cursor()
                        sql = 'INSERT INTO %s(cpid,cpname,speakid,speaker,text,time,workTime) values ("%s","%s","%s","%s","%s",%d,%d)'
                        data = (tableName, cpId, cpName, speakerId, speaker, text, time, Config.isWorkTime(time))
                        cursor.execute(str.format(sql % data))
                        conn.commit()
                        cursor.close()
                        # myTools.myPrint.print(
                        #     ModelTime.strftime('[%Y-%m-%d %H:%M]', ModelTime.localtime(time))+ cpName + "--" + speaker + ":" + text)

            except Exception as e:
                # conn.rollback()
                logging.getLogger("sql").error(traceback.format_exc())
                print("全部消息数据库断联")
                continue
                pass
            finally:
                if not conn is None:
                    conn.close()
                    print("全部消息数据库关闭")
