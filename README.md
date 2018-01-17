# PttUserOnlineRecord
用來紀錄PTT使用者的上線紀錄


pip install pyinstaller

pyinstaller打包教學

第一次build的語法備份
pyinstaller -F PTT.py  -n PTTOnlineRecoder --icon=app.ico -w --noupx 

有修改程式直接執行以下語法
pyinstaller PTTOnlineRecoder.spec



p.s. 使用-w模式不開啟console視窗  
必須不能使用'stdout' 例如print()
----------------------------------------------------  
工作排程器設定相關:  
勾選只有使用者登入才執行，取消勾選以最高權限執行

工作排程器預設會以C:\Windows\System32執行程式  
記得在新增工作->新增動作的開始位置欄位 填入程式的所在路徑

觸發程序設定成登入執行
將Windows設為不需密碼自動登入

待修bug:
1.查詢多個帳號目前有bug 會抓不到使用者資訊 有時間再修正
2.每月第一天 會爬不到過去上站紀錄 造成誤判為使用者上線
