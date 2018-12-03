import urllib2
import re
hdr = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

fp=open('soso.txt','r')
output = open('links.txt','a+')
url=fp.readline()
while url:
    urlrequest=urllib2.Request(url, headers=hdr)
    website = urllib2.urlopen(urlrequest)
    html = website.read()
    links = re.findall('https?://(.*?\.(?:com|cn|net|org|cc))',html)
    for i in links:
        m=re.search(r'.*\.(bing|bingj|microsoft|baidu|sogou|baike)\..*',i)
        if not m:
            if  i!="s.cn":
                output.write(i+'\n')
                print i
    url=fp.readline()
output.close()
fp.close()
