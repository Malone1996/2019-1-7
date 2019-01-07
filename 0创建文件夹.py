import os

# makedirs创建文件夹
# 参数1 path:文件夹路径
# 参数2 mod:文件夹权限/模式,默认为0o777
# 参数3 ,exist_ok:是否存在,默认为False,将False改为True避免二次创建文件夹不报错,强制覆盖
os.makedirs('a', exist_ok=True)  # 创建a文件夹
os.makedirs('1/2/3/4', exist_ok=True)  # 创建四级文件夹
