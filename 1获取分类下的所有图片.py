import requests  # 获取网页源码
from lxml import etree  # 解析网页源码
import os  # os=operation system操作内存,硬盘...

# 1.获取某个网页源码
url = "http://www.ivsky.com/tupian/"
content = requests.get(url).text
# print(content)

# 2.使用etree解析源码,使用xpath提取数据
root = etree.HTML(content)
big_category = root.xpath("//ul[@class='tpmenu']/li/a/text()")  #
# print(big_category)  # 以列表格式输出

# 创建分类文件夹
# for i in range(len(big_category)):
#     name = big_category[i]
#     os.makedirs(name, exist_ok=True)

# 获取大分类下的小分类
big_category_url = root.xpath("//ul[@class='tpmenu']/li/a/@href")  # 获取大分类的网址后缀
for i in range(len(big_category_url)):

    # 创建大分类文件夹
    b_name = big_category[i]
    os.makedirs(b_name, exist_ok=True)

    url = big_category_url[i]
    url = 'http://www.ivsky.com' + url  # 将域名与后缀拼接
    # print(url)
    content = requests.get(url).text
    root = etree.HTML(content)
    small_category = root.xpath("//div[@class='sline']/div/a/text()")  # 小分类名称
    # print(small_category)
    for j in range(len(small_category)):

        # 创建小分类文件夹
        s_name = small_category[j]
        # 目录结构应为大分类嵌套小分类
        os.makedirs(b_name + '/' + s_name, exist_ok=True)
