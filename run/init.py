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


def getUnUseMsg(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        print("正在读取废话消息")
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

def getStaff(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        print("正在读取公司员工")
    cursor = conn.cursor()
    sql = 'SELECT name , department FROM wxwork_message.staff'
    cursor.execute(sql)
    r = cursor.fetchall()
    Config.hz_all_staff.clear()
    for i in r:
        Config.hz_all_staff.append(i[0])
        if i[1] == "应用研发部":
            Config.staffList.append(i[0])
    conn.commit()
    cursor.close()
    conn.close()

def getGrpId(F=True):
    conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g", db="wxwork_message")
    if F:
        print("正在读取群组名称")
    cursor = conn.cursor()
    sql = 'SELECT rid,groupname FROM wxwork_message.groupnote'
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
        print("正在读取不需要处理的群")
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


def init():
    print("正在读取关键字")
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
