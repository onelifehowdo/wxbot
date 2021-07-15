boring = []
unusegrp = ["R:1075051383"]
CP = {}
hz_all_staff = []
staffList = []

def ungrp(rid):
    return not (rid in unusegrp)


def isStaff(id):
    engineer = {
        "1688852895879505": "孙张鑫"
    }
    return (True, engineer[id]) if (id in engineer.keys()) else (False, None)


def getCpname(id):
    return CP[id] if id in CP.keys() else id


def isBoring(text):
    return (text in boring)


def test_isStaff(name):
    return (name in staffList)



def test_isHZstaff(text):
    return (text in hz_all_staff)
