import logging
import sys
import datetime

class Logger:

    def __init__(self):
        self.logFilename = 'program.log'

    def setup_custom_logger(self):
        logger = logging.getLogger('lg')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # 寫入文件
            fileHandler = logging.FileHandler(self.logFilename, 'w', 'utf-8')
            fileHandler.setLevel(logging.DEBUG)
            # 在console印出
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setLevel(logging.INFO)

            logger.addHandler(fileHandler)
            logger.addHandler(consoleHandler)

        logger.info('=======執行時間: '+str(datetime.datetime.now())+'=======')


        return logger

    def cleanLog(self):
        # 清空log
        with open(self.logFilename, 'w'):
            pass

if __name__ == "__main__":
    # for i in range(2):
    log = Logger()
    log.cleanLog()
    logging = log.setup_custom_logger()