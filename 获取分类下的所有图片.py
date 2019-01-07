import requests  # 获取网页源码
from lxml import etree  # 解析网页源码
import os  # os = operation system = 操作系统  查看cpu、内存、硬盘。。。
# import urllib.request
# urllib.request.urlretrieve()

from urllib.request import urlretrieve

url = "http://www.ivsky.com/tupian/"
content = requests.get(url).text
root = etree.HTML(content)
big_category = root.xpath("//ul[@class='tpmenu']/li/a/text()")
big_category_url = root.xpath("//ul[@class='tpmenu']/li/a/@href")
for b_name, url in zip(big_category, big_category_url):
    os.makedirs(b_name, exist_ok=True)
    url = 'http://www.ivsky.com' + url
    content = requests.get(url).text
    root = etree.HTML(content)
    small_category = root.xpath("//div[@class='sline']/div/a/text()")
    small_category_url = root.xpath("//div[@class='sline']/div/a/@href")
    for s_name, url in zip(small_category, small_category_url):
        os.makedirs(b_name + '/' + s_name, exist_ok=True)
        page = 1
        while True:
            new_url = 'http://www.ivsky.com' + url + f'/index_{page}.html'
            content = requests.get(new_url).text
            root = etree.HTML(content)
            img_src = root.xpath("//img/@src")  # 图片地址
            if img_src:  # 如果列表不为空
                for src in img_src:
                    # split:切割、分割
                    img_name = src.split('/')[-1]  # 以'/'将字符串分为n部分,取倒数第一部分
                    print(img_name)
                    # 图片路径 = 文件夹路径 + / + 图片名字.jpg
                    urlretrieve(src, b_name + '/' + s_name + '/' + img_name)
                    print(f"下载{b_name}{s_name}第{page}页")
                page += 1
            else:
                print(f"{b_name}{s_name}到达最后一页")
                break
