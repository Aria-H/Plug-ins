# 1.获取要爬取的母网页的内容
import urllib.request
import re

url = "https://findicons.com"
webPage=urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')

# 2.对母网页内容处理，提取出里面的图片链接
k = re.split(r'\s+',data)
s = []
sp = []
si = []
for i in k :
    if (re.match(r'src',i) or re.match(r'href',i)):
        if (not re.match(r'href="#"',i)):
            if (re.match(r'.*?jpg"',i) or re.match(r'.*?ico"',i)):
                if (re.match(r'src',i)):
                    s.append(i)

for it in s :
    if (re.match(r'.*?jpg"',it)):
        sp.append(it)


# 3.获取这些图片链接的内容，并保存成本地图片,保存目录可以自行设定
cnt = 0
cou = 1
for it in sp:
    m = re.search(r'src="(.*?)"',it)
    iturl = m.group(1)
    print(iturl)
    if (iturl[0]=='/'):
        continue;
    web = urllib.request.urlopen(""+iturl)
    itdata = web.read()
    if (cnt%3==1 and cnt>=4 and cou<=30):
        f = open('C:/Users/HTT/Desktop/img/'+str(cou)+'.jpg',"wb")
        cou = cou+1
        f.write(itdata)
        f.close()
        print(it)
    cnt = cnt+1


