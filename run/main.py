# -*- coding: utf-8 -*-
import logging

import wxwork
import json
import time
from wxwork import WxWorkManager, MessageType

import myTools
import Config
import init
import Message
import checker
import grpNaGet
import mysqlAll
import Config
import loadData
import os

wxwork_manager = WxWorkManager(libs_path='libs')
# wxwork_manager = None



# 这里测试函数回调
@wxwork.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    # print('[on_connect] client_id: {0}'.format(client_id))
    # print(client_id)
    # print(type(client_id))
    pass


@wxwork.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    # print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id, message_type,
    #                                                                         json.dumps(message_data)))
    # print(message_type)
    # print(message_data)
    pass


@wxwork.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))
    # wxwork_manager.add_callback_handler(echoBot)



class EchoBot(wxwork.CallbackHandler):
    canworklist = [11041, 11042, 11043, 11044, 11045]
    contraller = myTools.ctrl()
    allMsgCtr = mysqlAll.sqliteControl()

    @wxwork.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        if message_type in self.canworklist and Config.ungrp(message_data["conversation_id"]) and "R" in message_data[
            "conversation_id"] and ("at_list" in message_data.keys()):
            if message_type == MessageType.MT_RECV_TEXT_MSG:
                # 如果是文本消息
                # print("-" * 30)
                # print("文本消息")
                # # print(message_type)
                # print(message_data)
                # print("-" * 30)
                atList = message_data["at_list"]
                cpId = message_data["conversation_id"]
                cpName = Config.getCpname(cpId)
                senderId = message_data["sender"]
                speaker = message_data["sender_name"]
                text = str(message_data["content"]).replace("\"", "")
                mtime = int(message_data["send_time"])
                myTools.myPrint.print("[" + time.strftime('%Y-%m-%d %H:%M',
                                                          time.localtime()) + "]" + cpName + "--" + speaker + ":" + text)
                self.contraller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime))
                self.allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime))
                if "$$$" in text and (Config.test_isHZstaff(speaker) or Config.tempisrid(senderId)):
                    p = text.split("$$$")
                    m_name = p[0]
                    m_note = p[1]
                    grpNaGet.grpget(cpId, m_name, speaker, mtime, m_note).start()
                pass
            else:
                # print("文件消息")
                atList = []
                cpId = message_data["conversation_id"]
                cpName = Config.getCpname(cpId)
                senderId = message_data["sender"]
                speaker = message_data["sender_name"]
                text = "文$件$消$息"
                mtime = int(message_data["send_time"])
                myTools.myPrint.print("[" + time.strftime('%Y-%m-%d %H:%M',
                                                          time.localtime()) + "]" + cpName + "--" + speaker + ":" + text)
                self.contraller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime))
                self.allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime))


if __name__ == "__main__":

    echoBot = None
    allMessage = None
    filter = None
    loader = None
    check = None
    SysFlag = True
    while True:  # 循环重启
        if myTools.WXSTU.ping():
            if init.init():
                if allMessage is None:
                    allMessage = mysqlAll.sqliteControl()
                    allMessage.start()
                if filter is None:
                    filter = myTools.ctrl()
                    filter.start()
                if loader is None:
                    loader = loadData.Loading()
                    loader.start()
                if check is None:
                    check = checker.check()
                    check.start()
                if echoBot is None:
                    echoBot = EchoBot()
                    wxwork_manager.add_callback_handler(echoBot)
                    # 添加回调实例对象

                wxwork_manager.manager_wxwork(smart=True)

                # 阻塞主线程
                while True:
                    SysFlag = (myTools.WXSTU.ping()
                                # allMessage.is_alive() and filter.is_alive() and loader.is_alive() and myTools.WXSTU.ping()\
                               )
                    if SysFlag:  # 系统无状况
                        print(allMessage.is_alive(), "ALL")
                        pass
                    else:  # 系统掉线
                        print("-----------掉线")
                        if myTools.WXSTU.getStatus():
                            if myTools.WXSTU.shutWX():
                                print("关闭微信成功")

                        allMessage = None
                        filter = None
                        loader = None
                        check = None
                        break
                    time.sleep(0.5)
        else:
            print("网络掉线")
            time.sleep(5)
