import logging
import traceback

import pymysql
import string
import time
import threading
import Config

class ctrMsg:
    def __init__(self, ctr, msg):
        self.ctr = ctr
        self.msg = msg


class sqliteControl(threading.Thread):
    MsgQueue = []
    rsp = {}  # 响应标志

    def __init__(self):
        threading.Thread.__init__(self)

    def add(cls, i):
        cls.MsgQueue.append(i)

    def run(cls):
        while True:
            conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g",
                                   db="wxwork_message")
            tableName = "msg"
            print("数据库打开成功")
            try:
                while True:
                    if len(cls.MsgQueue) > 0:
                        conn.ping()
                        mCtrMsg = cls.MsgQueue.pop(0)
                        ctr = mCtrMsg.ctr
                        Q_msg = mCtrMsg.msg

                        cpId = Q_msg.cpid
                        cpName = Q_msg.cpName
                        speakerId = Q_msg.speakerid
                        speaker = Q_msg.speaker
                        speakerType = Q_msg.speakerType
                        text = Q_msg.text
                        time = Q_msg.time
                        type = Q_msg.type
                        model = Q_msg.model
                        engineer = Q_msg.engineer
                        status = Q_msg.status
                        person = Q_msg.processor

                        if ctr == "HAVE_KEY":
                            cursor = conn.cursor()
                            sql = 'INSERT INTO %s(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor) values ("%s","%s","%s","%s","%s","%s","%s",%d,"%s","%s",%d,"%s")'
                            data = (
                            tableName, cpId, cpName, speakerId, speaker, text, speakerType, type, time, model, engineer,
                            status, person)
                            cursor.execute(str.format(sql % data))
                            conn.commit()
                            cursor.close()
                            cls.rsp[cpName] = False
                        elif ctr == "NO_KEY":
                            cursor = conn.cursor()
                            sql = 'SELECT processor FROM %s where cpid="%s" and type="message" and status=1 and speakertype="客户" order by time desc limit 1'
                            data = (tableName, cpId)
                            cursor.execute(str.format(sql % data))
                            t = cursor.fetchone()
                            if not t is None:
                                engineer = t[0]
                                if not Config.test_isStaff(t[0]):
                                    engineer="盛玉霞"
                            else:
                                engineer = "盛玉霞"

                            sql = 'INSERT INTO %s(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor) values ("%s","%s","%s","%s","%s","%s","%s",%d,"%s","%s",%d,"%s")'
                            data = (
                            tableName, cpId, cpName, speakerId, speaker, text, speakerType, type, time, model, engineer,
                            status, person)
                            cursor.execute(str.format(sql % data))
                            conn.commit()
                            cursor.close()
                            cls.rsp[cpName] = False
                        elif ctr == "STAFF":
                            if type == "message":
                                cursor = conn.cursor()
                                sql = 'UPDATE %s SET processor="%s" ,status=1 ,endtime=%d WHERE cpid="%s" and type="message" and status=0'
                                data = (tableName, speaker, time, cpId)
                                cursor.execute(str.format(sql % data))
                                conn.commit()
                                cursor.close()
                                print("[%s]响应" % speaker)
                            elif type == "problem":
                                cursor = conn.cursor()
                                sql = 'UPDATE %s SET processor="%s" ,status=1 WHERE cpid="%s" and type="message" and status=0'
                                data = (tableName, speaker, cpId)
                                cursor.execute(str.format(sql % data))
                                sql = 'INSERT INTO %s(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor) values ("%s","%s","%s","%s","%s","%s","%s",%d,"%s","%s",%d,"%s")'
                                data = (
                                tableName, cpId, cpName, speakerId, speaker, text, speakerType, type, time, model,
                                engineer, status, person)
                                cursor.execute(str.format(sql % data))
                                conn.commit()
                                cursor.close()
                                cls.rsp[cpName] = False
            except Exception as e:
                # conn.rollback()
                # logging.getLogger("sql").error(traceback.format_exc())
                print("数据库重连")
                continue
                pass
            finally:
                if not conn is None:
                    conn.close()
                    print("数据库关闭")
