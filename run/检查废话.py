import os
import time
import re
import Config
import pymysql
from pymysql.converters import escape_string

boring=[]
def getUnUseMsg():
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    print("正在读取废话消息")
    cursor = conn.cursor()
    sql = 'SELECT message FROM boringmsg'
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        boring.append(i[0])
    conn.commit()
    cursor.close()
    conn.close()

def isBoring(text):
    if text == "":
        return True
    return text in boring

def cleanMsg(m_text):
    print("清洗前的消息是：" + m_text)
    m_text = re.sub(r'.+\n.+\n-{6}\n', "", m_text)  # 去除引用
    m_text = re.sub(r'@\S+\b', "", m_text)  # 去除@
    m_text = re.sub(r'，|,|。|\.|、|!|！|？|\?|;|；|=|\s|\'\"\‘\“', "", m_text)  # 去除符号
    m_text = re.sub(r'\d+', "", m_text)#去除数字
    m_text = re.sub(r'\[[^\[\]]{1,4}\]', "", m_text)#去除表情

    print("清洗后的消息是："+m_text)
    return m_text

def toboring(text):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    sql = 'INSERT INTO wxwork_message.boringmsg(message) values ("%s")'
    data = (text,)
    cursor = conn.cursor()
    cursor.execute(str.format(sql % data))
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    getUnUseMsg()
    while True:
        string = input("输入鉴定的文字：")
        string = cleanMsg(string)
        if isBoring(string):
            print("鉴定结果为：废话")
            input("回车键继续：")
            continue
        else:
            print("鉴定结果为：有用信息")
            print("是否添加废话？ Y/N")
            s=input("")
            if s=="Y" or s=="y":
                string=escape_string(string)
                toboring(string)
                print("添加废话成功!")