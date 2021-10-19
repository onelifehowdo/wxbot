import time

import requests
import json

from run import Message, Config

data = {
    "seq": 5390,
    "limit": 1000
}


def on_message(message_type, message_data):
    if Config.ungrp(message_data["conversation_id"]):
        if message_type == "text":
            # 如果是文本消息
            print("文本消息")
            print(message_data)
            atList = message_data["at_list"]
            cpId = message_data["conversation_id"]
            cpName = Config.getCpname(cpId)
            senderId = message_data["sender"]
            speaker = "未知"
            text = str(message_data["content"]).replace("\"", "")
            mtime = int(message_data["send_time"])
            # myTools.myPrint.print(time.strftime('[%Y-%m-%d %H:%M]',
            #                                           time.localtime()) + cpName + "--" + speaker + ":" + text)
            # self.contraller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime))
            # self.allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime))
            # if "$$$" in text and (Config.test_isHZstaff(speaker) or Config.tempisrid(senderId)):
            #     p = text.split("$$$")
            #     m_name = p[0]
            #     m_note = p[1]
            #     grpNaGet.grpget(cpId, m_name, speaker, mtime, m_note).start()
            # pass
        else:
            print("文件消息")
            print(message_data)
            atList = []
            cpId = message_data["conversation_id"]
            cpName = Config.getCpname(cpId)
            senderId = message_data["sender"]
            speaker = "未知"
            text = "文$件$消$息"
            mtime = int(message_data["send_time"])
            # self.contraller.addMessage(Message.message(atList, cpId, cpName, senderId, speaker, text, mtime))
            # self.allMsgCtr.add(Message.message(None, cpId, cpName, senderId, speaker, text, mtime))


while True:
    r = requests.get("http://47.99.90.106:65535/message", params=data)
    Json = json.loads(r.text)
    for message_data in Json:
        data["seq"] = message_data["seq"]
        on_message(message_data["message_type"],message_data)
    time.sleep(0.5)
