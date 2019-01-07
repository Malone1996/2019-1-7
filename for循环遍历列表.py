a = ['a', 'b', 'c', 'd']
b = [20, 30, 40, 50]
c = [200, 300, 400, 500]

# 1.通过索引遍历(不推荐)
for i in range(len(a)):
    name = a[i]
    print(name)

# 2.通过in遍历
for i in a:
    print(i)

# 3.同时遍历多个列表
# zip压缩
# 前提:列表长度需要保持一致
for i, j, k in zip(a, b, c):
    print(i, j, k)
