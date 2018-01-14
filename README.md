# PttUserOnlineRecord
用來紀錄PTT使用者的上線紀錄


pip install pyinstaller

pyinstaller打包教學

step 1. 第一次build
pyinstaller -F PTT.py  -n PTTOnlineRecoder --icon=app.ico --noupx -w

step 2. 設定spec檔 將yaml加到輸出清單

step 3. 以後就只需要執行下面語法



p.s. 使用-w模式不開啟console視窗  
必須不能使用'stdout' 例如print()

工作排程器設定相關:  
勾選只有使用者登入才執行，取消勾選以最高權限執行

工作排程器預設會以C:\Windows\System32執行程式  
記得在新增工作->新增動作的開始位置欄位 填入程式的所在路徑



註:查詢多個帳號目前有bug 會抓不到使用者資訊 有時間再修正