import win32serviceutil
import PTT
from config import config
import time
import Log

log = Log.Logger()
logging = log.setup_custom_logger()

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "PTTOnlineRecoder"
    _svc_display_name_ = "PTT上線紀錄器"
    _svc_description_ = "PTT上線紀錄器"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.isAlive = True

    def SvcStop(self):
        self.isAlive = False

    def SvcDoRun(self):
        try:
            while self.isAlive:
                PTT.main()
                time.sleep(config().SleepTime)
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Service)
