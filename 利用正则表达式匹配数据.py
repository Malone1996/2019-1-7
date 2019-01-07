import re

# 匹配字符串中连续四个数字
content = "欢迎来到2019年"
pattern = re.compile(r"\d{4}")
result = pattern.findall(content)
print(result)

# 匹配连续的数字,至少一个,至多一个
pattern = re.compile(r"\d{1,4}")
# 匹配连续的数字,至少一个,至多不确定
pattern = re.compile(r"\d{1,}")
result = pattern.findall(content)
print(result)

# 匹配《》中的内容
content = "2019年最新电影《大黄蜂》正在上映"
pattern = re.compile(r"《(.*?)》")
result = pattern.findall(content)
print(result)