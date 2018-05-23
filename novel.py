import urllib.request
import re

def getNovelContent():

    html = urllib.request.urlopen('http://www.quanshuwang.com/book/0/269/')
    html = html.read()
    html = html.decode('gbk')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg = re.compile(reg)
    urls = re.findall(reg,html)

    for i in urls:
        novel_url = i[0]
        novel_title = i[1]
        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode('gbk')
        reg = '</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        reg = re.compile(reg,re.S)
        chapt_content = re.findall(reg,chapt_html)
        chapt_content = chapt_content[0].replace('<br />',"")
        chapt_content = chapt_content.replace('&nbsp;&nbsp;&nbsp;&nbsp;',"")

        print("????%s"%novel_title)
        f = open('{}.txt'.format(novel_title),'w')
        f.write(chapt_content)
        f.close

getNovelContent()
