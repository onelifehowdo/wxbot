import os
import threading
import time
import sqliteCtr
import Config
import init
import filter


class myPrint:
    i = 0

    @classmethod
    def print(cls, s):
        print(s)
        cls.i += 1
        cls.i = cls.i % 500
        if cls.i == 10:
            os.system("cls")


class message:
    def __init__(self, cpName, id, speaker, text, time):
        self.cpName = cpName
        self.id = id
        self.speaker = speaker
        self.text = text
        self.time = time


# 任务分配线程
class ctrl(threading.Thread):
    messageList = []
    m_ctr = sqliteCtr.sqliteControl()
    ins = None

    def __new__(cls, *args, **kwargs):
        if cls.ins is None:
            cls.ins = super().__new__(cls)
        return cls.ins

    def __init__(self):
        self.id = id
        threading.Thread.__init__(self)

    def addMessage(cls, msg):
        cls.messageList.append(msg)

    def run(cls):
        # 任务分配
        print("任务分配启动")
        cls.m_ctr.start()
        while True:
            with Config.LOCK:
                if len(cls.messageList) > 0:
                    r, msg = filter.filte(cls.messageList.pop(0))
                    if not r is None:
                        cls.m_ctr.add(sqliteCtr.ctrMsg(r, msg))
