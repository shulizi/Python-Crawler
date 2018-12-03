# _*_coding:utf-8 _*_
import urllib2
import re
import os
import threading
hdr = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
def downloadImage(packagename,path):
    imageb=urllib2.urlopen(path,).read()
    imagename=re.search(r'(?<=/)[_0-9a-zA-Z\.-]*?(?:jpeg|jpg|jpng|JPG|JPNG|png|PNG|bmp|BMP)',path).group()
    print packagename+'/'+imagename
    with open(packagename+'//'+imagename,'wb') as f:
            f.write(imageb)
if __name__=='__main__':
    fp=open('soso.txt','r')
    
    url=fp.readline()
    while url:
        packagename='result/'+re.search(r'(?<=\.)[_0-9a-zA-Z%]+(?=\.)',url).group()
        try:
            os.mkdir(packagename)
        except:
            pass
        urlrequest=urllib2.Request(url, headers=hdr)
        website = urllib2.urlopen(urlrequest)
        html=website.read()
        imageurl=re.findall(r'//.*?(?=\")',html)
        
        with open('result/image.txt','a+') as f:
            for i in imageurl:
                i = r'http:'+i
                if re.match(r'http://.*?(?:jpeg|jpg|jpng|JPG|JPNG|png|PNG|bmp|BMP)$',i):
                    f.write(i+'\n')
                    print i
                    t=threading.Thread(target=downloadImage,args=(packagename,i))
                    t.start()
        url=fp.readline()
    fp.close()
