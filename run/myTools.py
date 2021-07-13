import os
import threading
import time
import sqliteCtr
import Config
import init
import filter


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
    m_ctr.start()

    def __init__(self):
        self.id = id
        threading.Thread.__init__(self)

    def addMessage(self, msg):
        self.messageList.append(msg)

    def run(cls):
        # 任务分配
        print("任务分配启动")
        while True:
            if len(cls.messageList) > 0:
                r, msg = filter.filte(cls.messageList.pop(0))
                if not r is None:
                    cls.m_ctr.add(sqliteCtr.ctrMsg(r, msg))
                # r,msg,name=filter().filt(cls.messageList.pop(0))
                # if not r is None:
                #     if r=="response":
                #         m_ctrmsg = sqliteCtr.ctrMsg("response", r,msg,None)
                #         cls.m_ctr.add(m_ctrmsg)
                #     elif r=="solve":
                #         m_ctrmsg = sqliteCtr.ctrMsg("solve", r,msg,None)
                #         cls.m_ctr.add(m_ctrmsg)
                #     else:
                #         print("[%s:%s]:'%s'" % (msg.cpName, msg.speaker, msg.text))
                #         print("[%s][%s]问题指派->%s" % (msg.cpName,r, name))
                #         m_ctrmsg=sqliteCtr.ctrMsg("insert",r,msg,name)
                #         cls.m_ctr.add(m_ctrmsg)
