# 放置和PTT相關的程式碼
import sys
import telnetlib
import time
import re
from datetime import datetime
import FileHandle
import FindIP
from config import config
import Log

log = Log.Logger()
log.cleanLog()
logging = log.setup_custom_logger()

class Ptt(object):
    def __init__(self, host):

        self.settings = config()
        self._host = host
        self._user = self.settings.account
        self._password = self.settings.password
        self._telnet = telnetlib.Telnet(host)
        self._content = ''
    # 更新content
    # PrintContent:boolean 是否要印出content
    # 註:read_very_eager()只有在輸入完指令才能呼叫 若重覆呼叫會取得空的content
    def updateContent(self,PrintContent = False ,title = ''):
        self._content = self._telnet.read_very_eager().decode('big5', 'ignore')
        if PrintContent:
            logging.info('-----' + title + '------\n' + self._content + '\n-----------\n')

    @property
    def LoginProcess(self):
        # 錯誤嘗試次數
        errorCount = 0
        while u"主功能表" not in self._content:

            if errorCount>=10:
                return False
            elif errorCount>=1:
                logging.info('錯誤重試次數:'+ str(errorCount))
                time.sleep(0.2)

            if u"密碼不對" in self._content:
                logging.info("密碼不對或無此帳號。程式結束")
                sys.exit()
            elif u"您想刪除其他重複登入" in self._content:
                logging.info("刪除其他重複登入的連線....")
                self._telnet.write(b"y\r\n")
                time.sleep(7)
                self.updateContent()
            elif u"按任意鍵繼續" in self._content:
                logging.info("資訊頁面，按任意鍵繼續...")
                self._telnet.write(b"\r\n")
                time.sleep(0.2)
                self.updateContent()
            elif u"您要刪除以上錯誤嘗試" in self._content:
                logging.info("刪除以上錯誤嘗試...")
                self._telnet.write(b"y\r\n")
                time.sleep(3)
                self.updateContent()
            elif u"您有一篇文章尚未完成" in self._content:
                logging.info('刪除尚未完成的文章....')
                # 放棄尚未編輯完的文章
                self._telnet.write(b"q\r\n")
                time.sleep(3)
                self.updateContent()
            elif u"登入太頻繁" in self._content:
                logging.info('登入太頻繁')
                self._telnet.write(b"qqq\r\n")
                time.sleep(7)
                self.updateContent()
            elif not self._content:
                logging.info('Content為空')
                return False
            errorCount+=1
        return True
    # 輸入帳號密碼
    @property
    def input_user_password(self):
        if u"請輸入代號" in self._content:
            logging.info('輸入帳號中...')
            self._telnet.write(self._user + b"\r\n")
            logging.info('輸入密碼中...')
            self._telnet.write(self._password + b"\r\n")
            time.sleep(2)
            self.updateContent()
            # 輸入完帳密後進到主畫面
            return self.LoginProcess
        return False

    def is_connect(self):
        self.updateContent()
        if u"系統過載" in self._content:
            logging.info('系統過載, 請稍後再來')
            sys.exit(0)
        return True
    # 登入流程
    def login(self):
        if self.input_user_password:
            logging.info("----------------------------------------------")
            logging.info("------------------ 登入完成 ------------------")
            logging.info("----------------------------------------------")
            return True
            logging.info("沒有可輸入帳號的欄位，網站可能掛了")
        return False

    def logout(self):
        logging.info("登出中...")
        self._telnet.write(b"qqqqqqqqqg\r\ny\r\n")
        time.sleep(1)
        self._telnet.close()
        logging.info("----------------------------------------------")
        logging.info("------------------ 登出完成 ------------------")
        logging.info("----------------------------------------------")
    # 進入休閒聊天區頁面
    def GotoTalkPage(self):
        logging.info("進入休閒聊天區中...")
        self._telnet.write(b"T\r\n")
        time.sleep(0.2)
        self.updateContent()

    # 取得使用者資訊 註:要在休閒聊天頁面
    def GetUserInfo(self,account):
        logging.info("查詢網友中...")
        self._telnet.write(b"Q\r\n")
        time.sleep(1)
        self.updateContent(False,'查詢網友')
        logging.info("輸入網友ID中...")
        self._telnet.write((account + "\r\n").encode("big5"))
        time.sleep(1)
        self.updateContent(True,'輸入網友ID')

        if(u"線上使用者列表" in self._content):
            logging.info('使用者不存在')
            return '',''

        # 取得上站時間跟IP
        match = re.search('《上次上站》(?P<loginTime>\d+\/\d+\/\d+\s\d+:\d+:\d+).*《上次故鄉》(?P<ip>[\w\.]+)', self._content)
        if match:
            datetime_object = datetime.strptime(match.group('loginTime'), '%m/%d/%Y %H:%M:%S')
            ip = match.group('ip')
        else:
            datetime_object = '無法取得上站時間'
            ip = '無法取得ip'
        # 返回休閒聊天區
        self._telnet.write(b"\r\n")
        time.sleep(1)
        self.updateContent(False,'返回休閒聊天區')

        return datetime_object , ip

    # 丟水球 註:要在休閒聊天頁面
    def sendWater(self,UserId,LoginTime,IP):
        logging.info("進入線上使用者列表...")
        self._telnet.write(b"U\r\n")
        time.sleep(0.2)
        self.updateContent(False,'進入線上使用者列表')
        # 切換休閒聊天或好友列表模式 按f切換
        if u"休閒聊天" not in self._content:
            self._telnet.write(b"f")
            time.sleep(0.2)
            self.updateContent(False,'切換模式')
        logging.info("準備水球中...")
        self._telnet.write(("s"+self.settings.WaterTarget+"\r\n").encode("big5"))
        time.sleep(0.2)
        self.updateContent(False,'輸入水球目標ID')
        if not self._content:
            logging.info('水球發送對象不存在或不在站上')
            return
        self._telnet.write(("w"+UserId+" 登入時間: "+str(LoginTime)+"\r\n").encode("big5"))
        time.sleep(0.2)
        self.updateContent(False,'輸入水球訊息')
        self._telnet.write(b"y\r\n")
        time.sleep(0.2)
        self.updateContent(False,'發送水球')
        logging.info('水球發送完成')
        # 回到休閒聊天頁面
        self._telnet.write(b"e")
        time.sleep(0.2)
        self.updateContent(False,'回到休閒聊天頁面')




def main():
    host = 'ptt.cc'
    retryConnectTimes = 10
    retryCount = 0
    retryFlag = True

    while(retryFlag):

        if retryCount >= retryConnectTimes:
            retryFlag = False
            logging.info('重試次數超過' + str(retryConnectTimes) + ' 程式中止')
            sys.exit(0)

        ptt = Ptt(host)
        time.sleep(1)
        if ptt.is_connect():
            if ptt.login():

                # 進到休閒聊天頁面
                ptt.GotoTalkPage()

                # loop搜尋使用者
                for account,IsSendWater in ptt.settings.GetTargets():
                    # 取得使用者上站資訊
                    loginTime,ip = ptt.GetUserInfo(account)
                    # 取得ip資訊
                    if ip is not '無法取得ip':
                        contry,isp,city = FindIP.getIpInfo(ip)
                    else:
                        contry, isp, city ='','',''

                    # 從csv取得上一次上線紀錄
                    lastLoginTime ,_ = FileHandle.GetLastRecord(account)

                    # 如果使用者不存在 回傳空的loginTime lastLoginTime也會為空 IsChangeLoginTime=False
                    if str(loginTime) == lastLoginTime or str(loginTime) == '無法取得上站時間':
                        IsChangeLoginTime = False
                    else:
                        IsChangeLoginTime = True


                    # 如果變更上線時間且開啟丟水球功能 丟水球通知
                    if IsSendWater and IsChangeLoginTime:
                        ptt.sendWater(account , loginTime , ip)

                    # 存檔
                    if IsChangeLoginTime:
                        logging.info('使用者已變更上線紀錄')
                        FileHandle.SaveToCSV(account,loginTime,ip,isp,city,contry)



                # 跳出While迴圈
                retryFlag = False

        ptt.logout()
        retryCount += 1


if __name__ == "__main__":
    try:
        main()
    except:
        logging.error()
