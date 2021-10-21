# -*- coding: utf-8 -*-
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

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
import sqliteCtr
import Config
import loadData
import socket
import os

banner = r"""
                    
        
                           _ooOoo_
                          o8888888o
                          88" . "88
                          (| -_- |)
                          O\  =  /O
                       ____/`---'\____
                     .'  \\|     |//  `.
                    /  \\|||  :  |||//  \
                   /  _||||| -:- |||||-  \
                   |   | \\\  -  /// |   |
                   | \_|  ''\---/''  |   |
                   \  .-\__  `-`  ___/-. /
                 ___`. .'  /--.--\  `. . __
              ."" '<  `.___\_<|>_/___.'  >'"".
             | | :  `- \`.;`\ _ /`;.`/ - ` : | |
             \  \ `-.   \_ __\ /__ _/   .-` /  /
        ======`-.____`-.___\_____/___.-`____.-'======
                           `=---='
"""


# wxwork_manager = WxWorkManager(libs_path='libs')
#
#
# # wxwork_manager = None
#
#
# # 这里测试函数回调
# @wxwork.CONNECT_CALLBACK(in_class=False)
# def on_connect(client_id):
#     # print('[on_connect] client_id: {0}'.format(client_id))
#     # print(client_id)
#     # print(type(client_id))
#     pass
#
#
# @wxwork.RECV_CALLBACK(in_class=False)
# def on_recv(client_id, message_type, message_data):
#     # print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id, message_type,
#     #                                                                         json.dumps(message_data)))
#     # print(message_type)
#     # print(message_data)
#     pass
#
#
# @wxwork.CLOSE_CALLBACK(in_class=False)
# def on_close(client_id):
#     print('[on_close] client_id: {0}'.format(client_id))
#     # wxwork_manager.add_callback_handler(echoBot)
#
#
# class EchoBot(wxwork.CallbackHandler):
#     canworklist = [11041, 11042, 11043, 11044, 11045, 11048]
#     contraller = myTools.ctrl()
#     allMsgCtr = mysqlAll.sqliteControl()
#
#     @wxwork.RECV_CALLBACK(in_class=True)
#     def on_message(self, client_id, message_type, message_data):
#         if message_type in self.canworklist and Config.ungrp(message_data["conversation_id"]) and "R" in message_data[
#             "conversation_id"]:
#             if message_type == MessageType.MT_RECV_TEXT_MSG and "at_list" in message_data.keys():
#                 # 如果是文本消息
#                 # print("文本消息")
#                 print(message_data)
#                 atList = message_data["at_list"]
#                 cpId = message_data["conversation_id"]
#                 cpName = Config.getCpname(cpId)
#                 senderId = message_data["sender"]
#                 speaker = message_data["sender_name"]
#                 text = str(message_data["content"]).replace("\"", "")
#                 mtime = int(message_data["send_time"])
#                 # myTools.myPrint.print(time.strftime('[%Y-%m-%d %H:%M]',
#                 #                                           time.localtime()) + cpName + "--" + speaker + ":" + text)
#                 self.contraller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime))
#                 self.allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime))
#                 if "$$$" in text and (Config.test_isHZstaff(speaker) or Config.tempisrid(senderId)):
#                     p = text.split("$$$")
#                     m_name = p[0]
#                     m_note = p[1]
#                     grpNaGet.grpget(cpId, m_name, speaker, mtime, m_note).start()
#                 pass
#             else:
#                 # print("文件消息")
#                 atList = []
#                 cpId = message_data["conversation_id"]
#                 cpName = Config.getCpname(cpId)
#                 senderId = message_data["sender"]
#                 speaker = message_data["sender_name"]
#                 text = "文$件$消$息"
#                 mtime = int(message_data["send_time"])
#                 self.contraller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime))
#                 self.allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime))


def on_message(message_type, message_data):
    controller = myTools.ctrl()
    allMsgCtr = mysqlAll.sqliteControl()
    if Config.ungrp(message_data["conversation_id"]):
        if message_type == "text":
            # 如果是文本消息
            # print("文本消息")
            # print(message_data)
            seq = message_data["seq"]
            atList = message_data["at_list"]
            cpId = message_data["conversation_id"]
            with Config.LOCK:
                cpName = Config.getCpname(cpId)
            senderId = message_data["sender"]
            speaker = message_data["sender"]
            text = str(message_data["content"]).replace("\"", "")
            mtime = int(message_data["send_time"])
            # myTools.myPrint.print(time.strftime('[%Y-%m-%d %H:%M]',
            #                                           time.localtime()) + cpName + "--" + speaker + ":" + text)
            controller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime, seq))
            allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime, seq))
            # if "$$$" in text and (Config.test_isHZstaff(speaker) or Config.tempisrid(senderId)):
            #     p = text.split("$$$")
            #     m_name = p[0]
            #     m_note = p[1]
            #     grpNaGet.grpget(cpId, m_name, speaker, mtime, m_note).start()
            # pass
        else:
            # print("文件消息")
            # print(message_data)
            seq = message_data["seq"]
            atList = []
            cpId = message_data["conversation_id"]
            with Config.LOCK:
                cpName = Config.getCpname(cpId)
            senderId = message_data["sender"]
            speaker = message_data["sender"]
            text = "文$件$消$息"
            mtime = int(message_data["send_time"])
            controller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime, seq))
            allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime, seq))


class Resquest(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        try:
            if "data" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(myTools.myPrint.data).encode())
        except:
            pass

def getData():
    while True:
        data = {"limit": 1000}
        try:
            Config.MESSAGEFLAG.set()
            Config.ALLMESSAGEFLAG.set()
            # print(Config.MESSAGEFLAG.is_set(),Config.ALLMESSAGEFLAG.is_set())
            while True:
                if not (Config.MESSAGEFLAG.is_set() or Config.ALLMESSAGEFLAG.is_set()):
                    # print("加载数据")
                    data["seq"] = init.getseq()
                    # print("Seq",data["seq"])
                    r = requests.get("http://47.99.90.106:65535/message", params=data)
                    Json = json.loads(r.text)
                    for message_data in Json:
                        # data["seq"] = message_data["seq"]
                        on_message(message_data["message_type"], message_data)
                    # print("加载数据完毕，加载:",len(Json))
                    time.sleep(0.5)
                else:
                    # print("等待加载")
                    time.sleep(1)
        except Exception:
            time.sleep(1)
            continue

def myserver():
    IP = socket.gethostbyname(socket.gethostname())
    host = (IP, 8888)
    server = HTTPServer(host, Resquest)
    Config.printLog.info("Starting server, listen at: %s:%s" % host)
    server.serve_forever()




if __name__ == "__main__":
#####################
    print(banner)
#########################
    while True:
        filter = None
        loader = None
        allMessage = None
        server = None
        getMessage = None
        Config.EVENTFLAG.clear()
        if not (myTools.NetTools.ping() and myTools.NetTools.DBCanLink()):
            time.sleep(5)
            continue
        if init.init():
            if server is None:
                server = threading.Thread(target=myserver, name="ServerThread")
                server.start()
            if filter is None:
                filter = myTools.ctrl()
                filter.setName("FilterThread")
                filter.start()
            if allMessage is None:
                allMessage = mysqlAll.sqliteControl()
                allMessage.setName("WholeMessageThread")
                allMessage.start()
            if loader is None:
                loader = loadData.Loading()
                loader.setName("DynamicLoadingThread")
                loader.start()
            if getMessage is None:
                getMessage = threading.Thread(target=getData, name="GetMeassageThread")
                getMessage.start()
            while True:
                if myTools.NetTools.ping() and myTools.NetTools.DBCanLink():
                    myTools.myPrint.data['ThreadStatus'].clear()
                    for i in threading.enumerate():
                        myTools.myPrint.data['ThreadStatus'].append(i.getName())
                    time.sleep(0.5)
                else:
                    # logging.info(time.strftime([%Y-%m-%d %H:%M:%S],time.localtime(time.time())),"网络掉线")
                    Config.printLog.info("--------掉线--------")
                    Config.EVENTFLAG.set()
                    filter.join()
                    loader.join()
                    allMessage.join()
                    server.join()
                    getMessage.join()
                    break
                    # filter = None
                    # loader = None
                    # allMessage = None
                    # server = None
                    # getMessage = None



######################
# def myserver():
#     IP = socket.gethostbyname(socket.gethostname())
#     host = (IP, 8888)
#     server = HTTPServer(host, Resquest)
#     print(banner)
#     print("Starting server, listen at: %s:%s" % host)
#     server.serve_forever()
#
#
# threading.Thread(target=myserver, name="SERVER").start()
#
# echoBot = None
# allMessage = None
# filter = None
# loader = None
# check = None
# SysFlag = True
#
# while True:  # 循环重启
#     Config.EVENTFLAG.clear()
#     if myTools.WXSTU.ping() and myTools.WXSTU.DBCanLink():
#         if init.init():
#             # if allMessage is None:
#             #     allMessage = mysqlAll.sqliteControl()
#             #     allMessage.setName("All Message Threads")
#             #     allMessage.start()
#             if filter is None:
#                 filter = myTools.ctrl()
#                 filter.setName("Filter Thread")
#                 filter.start()
#             if loader is None:
#                 loader = loadData.Loading()
#                 loader.setName("Dynamic Loading Thread")
#                 loader.start()
#             # if check is None:
#             #     check = checker.check()
#             #     check.setName("Reminder Thread")
#             #     check.start()
#             # if echoBot is None:
#             #     echoBot = EchoBot()
#             #     wxwork_manager.add_callback_handler(echoBot)
#             #     # 添加回调实例对象
#             #
#             # wxwork_manager.manager_wxwork(smart=True)
#
#             # 阻塞主线程
#             while True:
#                 # print("----ThreadCount:", len(threading.enumerate()), threading.enumerate())
#                 myTools.myPrint.data['ThreadStatus'].clear()
#                 for i in threading.enumerate():
#                     myTools.myPrint.data['ThreadStatus'].append(i.getName())
#                 SysFlag = (
#                         myTools.WXSTU.getStatus() == "10" and allMessage.is_alive() and filter.is_alive() and loader.is_alive() and myTools.WXSTU.ping())
#                 if SysFlag:  # 系统无状况
#                     pass
#                 else:  # 系统掉线
#                     print("-----------掉线")
#                     if myTools.WXSTU.getStatus()[0] == "1":
#                         if myTools.WXSTU.shutWX():
#                             print("关闭微信成功")
#
#                     Config.EVENTFLAG.set()
#                     allMessage.join()
#                     filter.join()
#                     loader.join()
#                     check.join()
#
#                     allMessage = None
#                     filter = None
#                     loader = None
#                     check = None
#                     break
#     else:
#         Config.EVENTFLAG.set()
#         print("网络掉线")
#         # print("----DDDThreadCount:", len(threading.enumerate()), threading.enumerate())
#         time.sleep(5)
