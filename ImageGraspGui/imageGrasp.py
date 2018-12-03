# _*_coding:GBK _*_
import urllib2
import re
import os
import threading
hdr = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
class ImageGrasp:
    def __init__(self,keyword):
        print keyword,type(keyword)
        self.keyword=keyword.encode('GBK')
        self.url="http://pic.sogou.com/pics?query="+self.keyword+"&di=2&_asf=pic.sogou.com&_ast=1464879163&w=05009900&sut=2545&sst0=1464879199592"
        self.keyword=self.keyword.decode('GBK').encode('utf-8')
        print self.keyword+' is ready!'
        self.openURL()
    def downloadImage(self,path):
        imageb=urllib2.urlopen(path,).read()
        imagename=re.search(r'(?<=/)[_0-9a-zA-Z\.-]*?(?:jpeg|jpg|jpng|JPG|JPNG|png|PNG|bmp|BMP)',path).group()
        print self.keyword+'/'+imagename
        with open(self.keyword+'//'+imagename,'wb') as f:
                f.write(imageb)
    def openURL(self):
        try:
            os.mkdir(self.keyword)
        except:
            pass
        urlrequest=urllib2.Request(self.url, headers=hdr)
        website = urllib2.urlopen(urlrequest)
        html=website.read()
        print self.url+'\nread html ok! download now...'
        imageurl=re.findall(r'http://.*?(?=\")',html)
        with open('image.txt','a+') as f:
            for i in imageurl:
                if re.match(r'http://.*?(?:jpeg|jpg|jpng|JPG|JPNG|png|PNG|bmp|BMP)$',i):
                    f.write(i+'\n')
                    print i
                    t=threading.Thread(target=self.downloadImage,args=(i,))
                    t.start()
print 'Downloader is available!'
