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
                time.sleep(60*5)
                with Config.LOCK:
                    init.getUnUseMsg(F=False)
                    init.getIgnoreGrp(F=False)
                    init.getStaff(F=False)
                    init.getGrpId(F=False)
        finally:
            pass




