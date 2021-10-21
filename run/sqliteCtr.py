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
            # tableName = "msg"
            Config.printLog.info("消息数据库打开成功")
            try:
                while True:
                    if Config.EVENTFLAG.is_set():
                        raise Exception("消息线程主动退出")

                    if len(cls.MsgQueue) > 0:
                        if not Config.MESSAGEFLAG.is_set():
                            # print("messageSET")
                            Config.MESSAGEFLAG.set()

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
                        seq = Q_msg.seq

                        if ctr == "HAVE_KEY":
                            cursor = conn.cursor()
                            TestSql = "select * from wxwork_message.workMsg where cpid=%s and speakerid=%s and text=%s and time=%s"
                            cursor.execute(TestSql,(cpId,speakerId,text,time))
                            r = cursor.fetchall()
                            if(len(r)>0):
                                conn.commit()
                                cursor.close()
                                continue
                            sql = 'INSERT INTO wxwork_message.workMsg(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor,workTime,seq) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            data = (cpId, cpName, speakerId, speaker, text, speakerType, type, time, model,
                                engineer,
                                status, person,Config.isWorkTime(time),seq)
                            cursor.execute(sql ,data)
                            conn.commit()
                            cursor.close()
                            myTools.myPrint.print(
                                ModelTime.strftime('[%Y-%m-%d %H:%M:%S][MESSAGE]',
                                                   ModelTime.localtime(
                                                       time/1000)) + cpName + ":" + text+" -> "+engineer)
                            cls.rsp[cpName] = False
                        elif ctr == "NO_KEY":
                            cursor = conn.cursor()
                            TestSql = "select * from wxwork_message.workMsg where cpid=%s and speakerid=%s and text=%s and time=%s"
                            cursor.execute(TestSql,(cpId,speakerId,text,time))
                            r = cursor.fetchall()
                            if(len(r)>0):
                                conn.commit()
                                cursor.close()
                                continue
                            # sql = 'SELECT processor FROM %s where cpid="%s" and type="message" and status=1 and speakertype="客户" order by time desc limit 1'
                            sql = 'SELECT processor FROM wxwork_message.workMsg where cpid=%s and type="message" and status=1 order by time desc limit 1'
                            data = (cpId,)
                            cursor.execute(sql,data)
                            t = cursor.fetchone()
                            if not t is None:
                                engineer = t[0]
                                if not Config.isStaffByName(t[0]):
                                    engineer = "盛玉霞"
                            else:
                                engineer = "盛玉霞"

                            sql = 'INSERT INTO wxwork_message.workMsg(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor,workTime,seq) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            data = (cpId, cpName, speakerId, speaker, text, speakerType, type, time, model,
                                engineer,
                                status, person,Config.isWorkTime(time),seq)
                            cursor.execute(sql,data)
                            conn.commit()
                            cursor.close()
                            myTools.myPrint.print(
                                ModelTime.strftime('[%Y-%m-%d %H:%M:%S][MESSAGE]',
                                                   ModelTime.localtime(
                                                       time/1000)) + cpName + ":" + text+" -> "+engineer)
                            cls.rsp[cpName] = False
                        elif ctr == "TRANSFER":
                            # print("消息转移")
                            cursor = conn.cursor()
                            TestSql = "select * from wxwork_message.workMsg where cpid=%s and speakerid=%s and text=%s and time=%s"
                            cursor.execute(TestSql,(cpId,speakerId,text,time))
                            r = cursor.fetchall()
                            if(len(r)>0):
                                conn.commit()
                                cursor.close()
                                continue
                            sql = 'UPDATE wxwork_message.workMsg SET processor=%s ,status=1 ,endtime=%s WHERE cpid=%s and speakerid !=%s and type="message" and status=0'
                            data = (speaker, time, cpId,speakerId)
                            cursor.execute(sql,data)
                            sql = 'INSERT INTO wxwork_message.workMsg(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor,workTime,seq) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            data = (cpId, cpName, speakerId, speaker, text, speakerType, type, time, model,
                                engineer,
                                status, person,Config.isWorkTime(time),seq)
                            cursor.execute(sql,data)
                            conn.commit()
                            cursor.close()
                            myTools.myPrint.print(
                                ModelTime.strftime('[%Y-%m-%d %H:%M:%S][TRANSFER]',
                                                   ModelTime.localtime(time/1000)) + cpName + ":[" +speaker+"]"+ text+" -> "+engineer)
                            cls.rsp[cpName] = False
                        elif ctr == "STAFF":
                            if type == "message":
                                cursor = conn.cursor()
                                TestSql = "select * from wxwork_message.workMsg where cpid=%s and speakerid=%s and text=%s and time=%s"
                                cursor.execute(TestSql, (cpId, speakerId, text, time))
                                r = cursor.fetchall()
                                if (len(r) > 0):
                                    conn.commit()
                                    cursor.close()
                                    continue
                                sql = 'UPDATE wxwork_message.workMsg SET processor=%s ,status=1 ,endtime=%s WHERE cpid=%s and speakerid !=%s and type="message" and status=0'
                                data = (speaker, time, cpId,speakerId)
                                cursor.execute(sql,data)
                                conn.commit()
                                cursor.close()
                                # myTools.myPrint.print("[%s]响应" % speaker)
                                # print(
                                #     ModelTime.strftime('[%Y-%m-%d %H:%M][RESPONSE]',
                                #                        ModelTime.localtime(
                                #                            time/1000)) + cpName + "--" + speaker + ":" + text)
                                myTools.myPrint.print(
                                    ModelTime.strftime('[%Y-%m-%d %H:%M:%S][RESPONSE]',
                                                       ModelTime.localtime(
                                                           time/1000)) + cpName + "--" + speaker + ":" + text)
                            elif type == "problem":
                                cursor = conn.cursor()
                                TestSql = "select * from wxwork_message.workMsg where cpid=%s and speakerid=%s and text=%s and time=%s"
                                cursor.execute(TestSql, (cpId, speakerId, text, time))
                                r = cursor.fetchall()
                                if (len(r) > 0):
                                    conn.commit()
                                    cursor.close()
                                    continue
                                sql = 'UPDATE wxwork_message.workMsg SET processor=%s ,status=1 ,endtime=%s WHERE cpid=%s and type="message" and status=0'
                                data = (speaker, time, cpId)
                                cursor.execute(sql,data)
                                sql = 'INSERT INTO wxwork_message.workMsg(cpid,cpname,speakerid,speaker,text,speakertype,type,time,model,engineer,status,processor,workTime,seq) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                data = (cpId, cpName, speakerId, speaker, text, speakerType, type, time, model,
                                    engineer, status, person,Config.isWorkTime(time),seq)
                                cursor.execute(sql,data)
                                conn.commit()
                                cursor.close()
                                myTools.myPrint.print(
                                    ModelTime.strftime('[%Y-%m-%d %H:%M:%S][PROBLEM]',
                                                       ModelTime.localtime(
                                                           time/1000)) + cpName + "--" + speaker + ":" + text)
                                cls.rsp[cpName] = False
                    else:
                        if Config.MESSAGEFLAG.is_set():
                            # print("messageNOSET",len(cls.MsgQueue))
                            Config.MESSAGEFLAG.clear()

            except Exception as e:
                # conn.rollback()
                logging.getLogger("sql").error(traceback.format_exc())
                Config.printLog.info("消息数据库重连")
                continue
                pass
            finally:
                if not conn is None:
                    conn.close()
                    Config.printLog.info("消息数据库关闭")
