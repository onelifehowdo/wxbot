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
    def getQueNum(cls):
        return len(cls.MsgQueue)

    @classmethod
    def run(cls):
        while True:
            if Config.EVENTFLAG.is_set():
                break
            conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g",
                                   db="wxwork_message")
            Config.printLog.info("全部消息数据库打开成功")
            try:
                while True:
                    if Config.EVENTFLAG.is_set():
                        raise Exception("全部消息线程" + "主动退出")

                    if len(cls.MsgQueue) > 0:
                        if not Config.ALLMESSAGEFLAG.is_set():
                            # print("ALLSET")
                            Config.ALLMESSAGEFLAG.set()
                        conn.ping()
                        Q_msg = cls.MsgQueue.pop(0)

                        cpId = Q_msg.cpId
                        cpName = Q_msg.cpName
                        speakerId = Q_msg.speakid
                        speaker = Q_msg.speaker
                        text = Q_msg.text
                        time = Q_msg.time
                        seq = Q_msg.seq

                        if Config.isAllStaffById(speakerId):
                            speaker=Config.getAllStaffNameById(speakerId)

                        cursor = conn.cursor()
                        TestSql = "select * from wxwork_message.AllMessageTable where cpid=%s and speakid=%s and text=%s and time=%s"
                        cursor.execute(TestSql, (cpId, speakerId, text, time))
                        r = cursor.fetchall()
                        if (len(r) > 0):
                            conn.commit()
                            cursor.close()
                            continue
                        sql = 'INSERT INTO wxwork_message.AllMessageTable(cpid,cpname,speakid,speaker,text,time,workTime,seq) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                        data = (cpId, cpName, speakerId, speaker, text, time, Config.isWorkTime(time), seq)
                        cursor.execute(sql, data)
                        conn.commit()
                        cursor.close()
                        # print(text)
                    else:
                        if Config.ALLMESSAGEFLAG.is_set():
                            # print("ALLNOSET",len(cls.MsgQueue))
                            Config.ALLMESSAGEFLAG.clear()
            except Exception as e:
                # conn.rollback()
                logging.getLogger("sql").error(traceback.format_exc())
                Config.printLog.info("全部消息数据库断联")
                continue
                pass
            finally:
                if not conn is None:
                    conn.close()
                    Config.printLog.info("全部消息数据库关闭")
