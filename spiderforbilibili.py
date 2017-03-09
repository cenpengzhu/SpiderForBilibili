#spiderbilibili

#coding=utf-8
import spider
import sys

reload(sys)

sys.setdefaultencoding('utf8')


requesturl = "http://space.bilibili.com/ajax/member/GetInfo"

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400"
headers['X-Requested-With'] = "XMLHttpRequest"
headers['Referer'] = "http://space.bilibili.com/2/"

type = "POST"


birthdataspyder = spider.Spider("birthdata")


mid = 33307722


while mid < 33307723 :
    values = dict()
    values['mid'] = mid
    mid = mid + 1
    birthdataspyder.Jobs.AddOneJob(type, requesturl, headers, values)

birthdataspyder.RequestOne()

birthdataspyder.WriteOne()




         