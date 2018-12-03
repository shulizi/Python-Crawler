# _*_coding:utf-8 _*_
import urllib2
import re

hdr = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
fp=open('soso.txt','r')
target_url=fp.readline()
while target_url:
    urlrequest=urllib2.Request(target_url, headers=hdr)
    html = urllib2.urlopen(urlrequest)
    content = html.read()
    lines = re.findall(r'(?<=>)(?:\w|[^x00-xff])+(?=<)',content)
    with open('links.txt','a+') as output:
        for i in lines:
            if i!='' and ord(i[0])!=10:
                #print i
                output.write(i+'\n')
    target_url=fp.readline()
fp.close()
