import os
import threading
import time as ModelTime

import pymysql

import sqliteCtr
import Config
import init
import filter


class myPrint:
    # i = 0

    data = {'dataList': [], 'ThreadStatus': []}

    @classmethod
    def print(cls, s, flag=False):
        if flag:
            print(s)
        if len(cls.data['dataList']) >= 2000:
            cls.data['dataList'].pop(0)
        cls.data['dataList'].append(s)
        # print(s)
        # cls.i += 1
        # cls.i = cls.i % 500
        # if cls.i == 10:
        #     os.system("cls")


class message:
    def __init__(self, cpName, id, speaker, text, time):
        self.cpName = cpName
        self.id = id
        self.speaker = speaker
        self.text = text
        self.time = time


class WXSTU:
    @classmethod
    def getStatus(cls):
        wx = "0"
        re = "0"
        cmd = 'tasklist'
        res = os.popen(cmd)
        output_str = res.read()  # 获得输出字符串
        if "WXWork.exe" in output_str:
            wx = "1"
        if "TxBugReport.exe" in output_str:
            re = "1"
        return wx + re

    @classmethod
    def shutWX(cls):
        try:
            cmd = 'taskkill /f /t /im TxBugReport.exe'
            if "成功" in os.popen(cmd):
                print("企业微信崩溃")
        except:
            pass
        finally:
            pass
        cmd = 'taskkill /f /t /im WXWork.exe'
        res = os.popen(cmd)
        output_str = res.read()  # 获得输出字符串
        return True if ("成功" in output_str) else False

    @classmethod
    def ping(cls):
        cmd = 'ping -n 1 www.tencent.com'
        res = os.popen(cmd)
        output_str = res.read()  # 获得输出字符串
        return True if ("已发送" in output_str) else False

    @classmethod
    def DBCanLink(cls):
        conn = None
        flag = True
        try:
            conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g",
                                   db="wxwork_message", connect_timeout=2)
        except Exception:
            flag = False
        finally:
            if not conn is None:
                conn.close()
            return flag


# 任务分配线程
class ctrl(threading.Thread):
    messageList = []
    ins = None

    def __new__(cls, *args, **kwargs):
        if cls.ins is None:
            cls.ins = super().__new__(cls)
        return cls.ins

    def __init__(self):
        self.id = id
        self.m_ctr = sqliteCtr.sqliteControl()
        self.m_ctr.setName("message Thread")
        threading.Thread.__init__(self)

    @classmethod
    def addMessage(cls, msg):
        cls.messageList.append(msg)

    def run(self):
        # 任务分配
        print("任务分配启动")
        self.m_ctr.start()
        while True:
            if Config.EVENTFLAG.is_set():
                self.m_ctr.join()
                raise Exception(self.name + "主动退出")
            with Config.LOCK:
                if len(self.messageList) > 0:
                    r, msg = filter.filte(self.messageList.pop(0))
                    if not r is None:
                        self.m_ctr.add(sqliteCtr.ctrMsg(r, msg))
                    else:
                        myPrint.print(
                            ModelTime.strftime('[%Y-%m-%d %H:%M:%S][UNUSEFUL]',
                                          ModelTime.localtime(msg.time/1000)) + msg.cpName + "--" + msg.speaker + ":" + msg.text)


if __name__ == "__main__":
    if WXSTU.getStatus():
        print("ok")
    else:
        WXSTU.shutWX()
