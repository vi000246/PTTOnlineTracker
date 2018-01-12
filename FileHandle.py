# 放置和資料存取紀錄有關的程式碼
import csv
import datetime
import os

# 讀取最近一次上線紀錄 回傳時間，IP
def GetLastRecord(userId):
    csvPath = _GetFilePath(userId)

    if not os.path.isfile(csvPath):
        return '',''

    with open(csvPath, 'r', encoding='utf-8-sig', newline='') as myfile:
        last_line = myfile.readlines()[-1].replace('"', '').strip()
        lis = last_line.split(',')
        return lis[0],lis[1]


# 寫入CSV檔
def SaveToCSV(userId,logintime,ip,isp,city,contry):
    # 判斷檔案存不存在
    csvPath = _GetFilePath(userId)
    # 如果不存在就開一個新檔案
    if not os.path.isfile(csvPath):
        with open(csvPath, 'w',encoding='utf-8-sig',newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            csvHeader = [u'登入時間',u'IP',u'ISP',u'城市',u'國家']
            wr.writerow(csvHeader)
            wr.writerow([logintime,ip,isp,city,contry])

    # 如果存在就append new row
    else:
        with open(csvPath, 'a',encoding='utf-8-sig',newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([logintime,ip,isp,city,contry])

# 取得檔案連結
def _GetFilePath(userId):
    FileName = userId + '_' + datetime.datetime.now().strftime('%Y%m') + '.csv'
    directory = os.getcwd() + '\\LoginHistory\\'
    if not os.path.exists(directory):
        os.makedirs(directory)
    csvPath = directory + FileName
    return csvPath



if __name__ == "__main__":
    # SaveToCSV('vi000246','2018-01-30 11:30:26','127.0.0.1')
    a,b = GetLastRecord('vi000246')
    print(a)