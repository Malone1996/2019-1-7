import requests
from lxml import etree
import os

url = "https://www.dy2018.com/html/gndy/dyzz/index.html"

# 解决乱码问题
content = requests.get(url)
content.encoding = content.apparent_encoding
content = content.text

root = etree.HTML(content)
tag = root.xpath("//td/a/text()")
print(tag)

for i in range(len(tag)):
    name = tag[i]
    os.makedirs(name, exist_ok=True)
