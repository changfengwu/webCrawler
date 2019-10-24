#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

#下载一个 网页
url ='http://www.17k.com/list/2932117.html'
# 定义要爬虫到的章节, 15表示只爬到15章
chapter_num = 28
#模拟浏览器发送http请求
response = requests.get(url)
response.encoding ='utf-8'
html = response.text
#小说标题
tittle = re.findall(r'<h1 class="Title">(.*?)</h1', html)[0]
#print(tittle)
#新建文件保存小说内容
fb =open('%s.txt' % tittle, 'w', encoding ='utf-8')
dl = re.findall(r'<dl class="Volume">.*?</dl>', html, re.S)[0]
dd = re.findall(r'<dd>.*?</dd>', dl, re.S)[0]

#注意正则表达式易错，.不能代替换行符

# chapter_info_list = re.findall(r'href="(.*?)".*?>\n.*?<span class="ellipsis.*?">\n\s{60}(.*?)\s{52}<', dd)
chapter_info_list = re.findall(r'href="(.*?)"\n.*?>\n.*?\n\t{17}(.*?)\n.*?\n.*?</a>', dd)


#新建文件保存小说内容
#with open('%s.txt' % tittle) as f:
#循环每个章节，分别下载
i = 1
for chapter_info in chapter_info_list:
    if  i <= chapter_num:
        print('正在爬第'+str(i)+'章')
        # chapter_tittle = chapter_info[1]
        # chapter_url = chapter_info[0]
        chapter_url, chapter_tittle = chapter_info
        chapter_url ="http://www.17k.com%s" % chapter_url
        # print(chapter_url)
        #print(chapter_url, chapter_tittle)
        #下载章节内容
        chapter_response = requests.get(chapter_url)
        chapter_response.encoding ='utf-8'
        chapter_html = chapter_response.text
        #读取章节内容
        chapter_content = re.findall(r'<div class="[p]">(.*?)<p class="copy ">', chapter_html, re.S)[0]
        #清洗数据
        chapter_content = chapter_content.replace(' ', '')
        chapter_content = chapter_content.replace('&#12288;', '')
        chapter_content = chapter_content.replace('<br/>', '')
        chapter_content = chapter_content.replace('<p>', '')
        chapter_content = chapter_content.replace('</p>', '')
        chapter_content = chapter_content.replace('\t', '')
        #持久化
        fb.write(chapter_tittle)
        fb.write(chapter_content)
        fb.write('\n')
        i = i + 1

    else:
        break
print(chapter_url, chapter_tittle)

#exit()

