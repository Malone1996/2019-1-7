import requests
from lxml import etree

for i in range(0, 250, 25):
    url = f"https://book.douban.com/top250?start={i}"
    content = requests.get(url).text
    root = etree.HTML(content)
    title = root.xpath("//a/@title")
    for j in range(len(title)):
        print(title[j])
