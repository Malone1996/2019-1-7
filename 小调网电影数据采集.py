import requests
from lxml import etree
import re

# 获取所有页面
url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
content = requests.get(url).text
root = etree.HTML(content)
pages = root.xpath("//select/option/@value")

for page in pages:
    url = "https://www.dy2018.com" + page
    content = requests.get(url)
    content.encoding = content.apparent_encoding
    content = content.text
    root = etree.HTML(content)
    movie_titles = root.xpath("//b/a/@title")  # 获取所有电影标题
    movie_hrefs = root.xpath("//b/a/@href")  # 获取所有电影详情页地址
    for movie_title, movie_href in zip(movie_titles, movie_hrefs):
        movie_href = "https://www.dy2018.com" + movie_href
        # 标题只保留尖括号里面的
        pattern = re.compile(r"《(.*?)》")  # 正则表达式
        movie_title = pattern.findall(movie_title)
        content = requests.get(movie_href)
        content.encoding = content.apparent_encoding
        content = content.text
        if content:
            root = etree.HTML(content)
            download_url = root.xpath("//td[@bgcolor='#fdfddf']/a/text()")[0]  # 有多个下载地址,取第一个
            print(movie_title, download_url)

            # 文件存储代码
            f = open("F:/movie.txt", 'a+')
            f.write(movie_title[0])
            f.write(':')
            f.write(download_url)
            f.write('\n')
            f.close()
