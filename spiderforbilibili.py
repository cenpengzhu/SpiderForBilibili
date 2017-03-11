#spiderforbilibili

#coding=utf-8
import spider
import sys
import socket
import fcntl
import struct
import subprocess
import time

SIOCGIFADDR = 0x8915

def GetIp(ifname):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try :
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),SIOCGIFADDR,struct.pack('256s',ifname[:15]))[20:24])
        return ip
    except:
        return ''

shellstr = 'ifup wan'

def Redial():
    if subprocess.call(shellstr,shell=True) == 0 :
        return True
    return False



reload(sys)

sys.setdefaultencoding('utf8')


requesturl = "http://space.bilibili.com/ajax/member/GetInfo"

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400"
headers['X-Requested-With'] = "XMLHttpRequest"
headers['Referer'] = "http://space.bilibili.com/2/"

type = "POST"


birthdataspider = spider.Spider("birthdata1")

mid = 1
requestno = 0
oldIpList = []
oldIpList.append(GetIp('pppoe-wan'))
print oldIpList

while mid < 2 :
    if requestno > 190 :
        while True :
            if Redial() :
                print 'redial success'
                break
            time.sleep(1)
        while True :
            time.sleep(5)
            newIp = GetIp('pppoe-wan')
            if newIp != '' :
                print"newIp is %s"%newIp
                break
        if newIp in oldIpList :
           # pirnt "Ip List is %s"%str(oldIpList)
            print "this IP repeat ip:%s"%newIp
            time.sleep(1)
            continue
        else :
            oldIpList.append(newIp)
            if len(oldIpList) > 500 :
               oldIpList.pop(oldIpList[0])
            requestno = 0

    values = dict()
    values['mid'] = mid
    mid = mid + 1
    birthdataspider.Jobs.AddOneJob(type,requesturl,headers,values)

    if birthdataspider.RequestOne() == False:
        requestno = 200
        continue


    birthdataspider.WriteOne()
    requestno = requestno + 1








    









         