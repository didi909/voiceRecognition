import os
import datetime

# 定义机器能做的事情

# 调用浏览器并打开一个页面
def searchengine(url,appurl = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"'):
    para = appurl+' '+url
    print(url)
    os.system(para)

# searchengine('http://www.baidu.com')

def getCurrentTime():
    currentTime = datetime.datetime.now()
    currentTimeString = str(currentTime.year)+'年'+str(currentTime.month)+'月'+str(currentTime.day)+'日'+str(currentTime.hour)+'时'+str(currentTime.minute)+'分'+str(currentTime.second)+'秒'
    return currentTimeString