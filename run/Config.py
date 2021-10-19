import threading
import time

EVENTFLAG = threading.Event()
MESSAGEFLAG = threading.Event()
ALLMESSAGEFLAG = threading.Event()
LOCK = threading.Lock()
lock = threading.Lock()
boring = []
ignore = []
CP = {}
hz_all_staff = {}
staffList = {}
tempRid = []

holiday = []
workDay = []



def isStaffById(id):
    return id in staffList.keys()
def isStaffByName(name):
    flag=False
    for m_id in staffList:
        if staffList[m_id]==name:
            flag=True
            break
    return flag

def isAllStaffById(id):
    return id in hz_all_staff.keys()
def isAllStaffByName(name):
    flag=False
    for m_id in hz_all_staff:
        if hz_all_staff[m_id]==name:
            flag=True
            break
    return flag

def getAllStaffNameById(id):
    return hz_all_staff[id]



# def tempisrid(rid):
#     return rid in tempRid


def ungrp(rid):
    return not (rid in ignore)


# def isStaff(id):
#     engineer = {
#         "1688852895879505": "孙张鑫"
#     }
#     return (True, engineer[id]) if (id in engineer.keys()) else (False, None)


def getCpname(id):
    return CP[id] if id in CP.keys() else id


def isBoring(text):
    if text == "":
        return True
    return text in boring


# def test_isStaff(name):
#     return name in staffList


# def test_isHZstaff(text):
#     return text in hz_all_staff


def isWorkTime(mt):
    mt = time.localtime(int(mt/1000))
    todayWork = False
    WEEK = int(time.strftime('%w', mt))
    DATE = time.strftime('%Y-%m-%d', mt)
    TIME = time.strftime('%H:%M', mt)

    if DATE not in holiday:
        if 1 <= WEEK <= 5:
            todayWork = True
        else:
            if DATE in workDay:
                todayWork = True

    nowWork = ("09:00" <= str(TIME) <= "20:00")

    return 1 if (todayWork and nowWork) else 0

# if __name__ == "__main__":
#     engineer = {
#         "1688852895879505": "孙张鑫"
#     }
#     engineer["1"]="sss"
#
# def isStaffById(id):
#     return id in engineer.keys()
# def isStaffByName(name):
#     flag=False
#     for m_id in engineer:
#         if engineer[m_id]==name:
#             flag=True
#             break
#     return flag
# print(engineer)