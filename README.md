# PttUserOnlineRecord
用來紀錄PTT使用者的上線紀錄

pip install pyinstaller

使用pyinstaller打包  
記得到Log.py把DebugMode設為False  
pyinstaller -F PTT.py  -n PTTOnlineRecoder --icon=app.ico --noupx -w

p.s. 使用-w模式不開啟console視窗  
必須不能使用'stdout' 例如print()

工作排程器設定相關:  
把vbs放在和exe檔同個目錄
勾選只有使用者登入才執行，取消勾選以最高權限執行