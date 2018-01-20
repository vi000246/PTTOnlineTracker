import requests
import re

def getIpInfo(ip):
    r = requests.post("http://dir.twseo.org/ip-query3.php",data={'inputip':ip},headers={'Content-type':'application/x-www-form-urlencoded; charset=UTF-8'})
    r.encoding='utf8'
    match = re.search('IP國別:[^>]*>[^>]*>(?P<contry>[^<]*).*ISP來源:[^>]*>(?P<ISP>[^<]*).*IP地理: 城市:[^>]*>(?P<city>[^<]*)',
                      r.text)
    if match:
        isp = match.group('ISP')
        matchIsp = re.search('(?P<isp>[\u4e00-\u9fff]+)',isp)
        if matchIsp:
            isp = matchIsp.group('isp').replace("股份有限公司", "")
        return match.group('contry'),isp,match.group('city')
    else:
        return '','',''

if __name__ == "__main__":
    a,b,c=getIpInfo('114.136.1asdfsf')
    print(a,b,c)