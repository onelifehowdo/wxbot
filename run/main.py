# -*- coding: utf-8 -*-

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

wxwork_manager = WxWorkManager(libs_path='libs')
sendList = ["nihao"]
clientID = None


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
    # print(message_data)
    pass


@wxwork.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


class EchoBot(wxwork.CallbackHandler):

    @wxwork.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        # 如果是文本消息
        if message_type == MessageType.MT_RECV_TEXT_MSG and message_data["conversation_id"]!="R:1075051383":
            atList=message_data["at_list"]
            cpId = message_data["conversation_id"]
            cpName = Config.getCpname(cpId)
            senderId = message_data["sender"]
            speaker = message_data["sender_name"]
            text = str(message_data["content"]).replace("\"", "")
            mtime = int(message_data["send_time"])
            print("["+time.strftime('%Y-%m-%d %H:%M', time.localtime())+"]:"+text)
            myTools.ctrl().addMessage(Message.message(atList,cpId, cpName, senderId, speaker, text, mtime))
            mysqlAll.sqliteControl().add(Message.message(None,cpId, cpName, senderId, speaker, text, mtime))
            if "$$$" in text:
                p=text.split("$$$")
                m_name=p[0]
                m_note=p[1]
                grpNaGet.grpget(cpId,m_name,speaker,mtime,m_note).start()
            pass


if __name__ == "__main__":
    if init.init():
        mysqlAll.sqliteControl().start()
        myTools.ctrl().start()
        echoBot = EchoBot()
        checker.check().start()

    # 添加回调实例对象
    wxwork_manager.add_callback_handler(echoBot)
    wxwork_manager.manager_wxwork(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)
