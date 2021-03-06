import logging
import time

import pymysql
import xlrd
import Config

mlist = []


def clean(value):
    value = value.replace(" ", "")
    value = value.replace("\n", "")
    return value


class mdata:
    def __init__(self, name, model, keyList):
        self.name = name
        self.model = model
        self.keyList = keyList


def getWorkDay(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        Config.printLog.info("正在读取工作日配置")
    cursor = conn.cursor()
    sql = 'SELECT * FROM wxwork_message.workdate;'
    cursor.execute(sql)
    r = cursor.fetchall()
    Config.workDay.clear()
    Config.holiday.clear()
    for i in r:
        if i[2] == 0:
            Config.holiday.append(i[1])
        else:
            Config.workDay.append(i[1])
    else:
        cursor.close()
        conn.close()


def getUnUseMsg(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        Config.printLog.info("正在读取废话消息")
    cursor = conn.cursor()
    sql = 'SELECT message FROM boringmsg'
    cursor.execute(sql)
    r = cursor.fetchall()
    Config.boring.clear()
    for i in r:
        Config.boring.append(i[0])
    conn.commit()
    cursor.close()
    conn.close()
    # print("废话数量：",len(Config.boring))


def getStaff(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        Config.printLog.info("正在读取公司员工")
    cursor = conn.cursor()
    sql = 'SELECT rid , department,name FROM wxwork_message.staff'
    cursor.execute(sql)
    r = cursor.fetchall()
    Config.hz_all_staff.clear()
    Config.staffList.clear()
    for i in r:
        Config.hz_all_staff[i[0]] = i[2]
        if i[1] == "应用研发部":
            Config.staffList[i[0]] = i[2]
    conn.commit()
    cursor.close()
    conn.close()


def getGrpId(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        Config.printLog.info("正在读取群组名称")
    cursor = conn.cursor()
    sql = 'SELECT chat_id,name FROM wxwork_message.wx_group'
    cursor.execute(sql)
    r = cursor.fetchall()
    Config.CP.clear()
    for i in r:
        Config.CP[i[0]] = i[1]
        # print("没有配置群字典")
    conn.commit()
    cursor.close()
    conn.close()


def getIgnoreGrp(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        Config.printLog.info("正在读取不需要处理的群")
    cursor = conn.cursor()
    sql = 'SELECT rid,cpname FROM wxwork_message.ignoreGrp;'
    cursor.execute(sql)
    r = cursor.fetchall()
    Config.ignore.clear()
    for i in r:
        Config.ignore.append(i[0])
    conn.commit()
    cursor.close()
    conn.close()


def getrid(F=True):
    if F:
        Config.printLog.info("正在读取RID")
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    sql = 'SELECT *FROM wxwork_message.staff where rid is not NULL'
    cursor = conn.cursor()
    cursor.execute(sql)
    r = cursor.fetchall()
    for i in r:
        Config.tempRid.append(i[1])
    conn.commit()
    cursor.close()
    conn.close()

def getseq():
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    sql = 'SELECT max(seq) FROM wxwork_message.AllMessageTable'
    cursor = conn.cursor()
    cursor.execute(sql)
    r = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return r[0]


def init():
    Config.printLog.info("正在读取关键字")
    xl = xlrd.open_workbook(r'keyword.xlsx')
    sheet = xl.sheet_by_index(0)
    mlist.clear()
    for i in range(1, sheet.nrows):
        name = clean(str(sheet.cell(i, 0).value))
        model = clean(str(sheet.cell(i, 4).value))
        keywords = clean(str(sheet.cell(i, 6).value))
        keywords = keywords.strip("|")
        keywords = keywords.split("|")
        mlist.append(mdata(name, model, keywords))
    getWorkDay()
    getrid()
    getUnUseMsg()
    getIgnoreGrp()
    getStaff()
    getGrpId()
    return True


def getbean(msg):
    model = "another"
    name = None
    msg = str(msg).lower()
    for i in mlist:
        for j in i.keyList:
            # print(j)
            if j in msg:
                model = i.model
                name = i.name
                return model, name
    return model, name
# init()
# print(getbean("mqtt"))

if __name__ == "__main__":
    print(getseq())
