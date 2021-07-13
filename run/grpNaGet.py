import threading
import pymysql
import re

class grpget(threading.Thread):
    def __init__(self,rid,grpName,admin,time,note):
        threading.Thread.__init__(self)
        self.rid=rid
        self.grpName=grpName
        self.admin=admin
        self.time=time
        self.note=note or ""

    def run(self) -> None:
        conn = pymysql.connect(host="120.26.54.146", user="wxwork_message", passwd="6CmnpPoS1jwIM%5g",db="wxwork_message")
        cursor = conn.cursor()
        sql = str.format('insert into groupnote(rid,groupname,admin,creattime,note) values ("%s","%s","%s",%d,"%s")' % (self.rid,self.grpName,self.admin,self.time,self.note))
        cursor.execute(sql)
        conn.commit()
