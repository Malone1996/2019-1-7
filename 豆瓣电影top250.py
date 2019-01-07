import requests
from lxml import etree

for i in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={i}"
    content = requests.get(url).text
    root = etree.HTML(content)
    url1 = root.xpath("//div[@class='hd']/a/@href")
    for j in range(len(url1)):
        print(url1[1])
        # content1 = requests.get(url1[j]).text
        # root1 = etree.HTML(content1)
        # title = root1.xpath("//h1/span")
        # print(title)
