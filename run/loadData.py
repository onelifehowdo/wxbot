import threading
import time
import init
import Config
class Loading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self) -> None:
        try:
            while True:
                for i in range(60*5):
                    if Config.EVENTFLAG.is_set():
                        raise Exception(self.name + "主动退出")
                    time.sleep(1)
                with Config.LOCK:
                    # print(time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time())), "load...")
                    init.getWorkDay(F=False)
                    init.getUnUseMsg(F=False)
                    init.getIgnoreGrp(F=False)
                    init.getStaff(F=False)
                    init.getGrpId(F=False)
                    # print(time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())),"load ok")
        finally:
            pass




