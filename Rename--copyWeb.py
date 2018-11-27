import urllib
import  urllib.request
import re

# url = "http://undorable.com/huace-detail.php?cid=21&id=34"
def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def getImg(html):
    reg = 'src="(.+?\.jpg)"'        #正则表达式
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.decode('utf-8'))
    x = 1
    for imgurl in imglist  :
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)    # 设置了要下载的图片资源路径和要命名的名字
        print('正在下载第%s张图片' % x)
        x+=1
        if x>6:                     #设置爬取图片的张数
            break
    return None

html = getHtml("https://findicons.com")
getImg(html)
