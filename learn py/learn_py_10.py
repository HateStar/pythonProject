# 开发时间 2021/3/21 16:38
# 加油啊测试！！
#python标准库
import os
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context #全局取消ssl证书验证，避免urllib库报错


#os模块常用方法
print(os.listdir("./"))#展示选定目录的文件列表，返回list格式
#os.mkdir("test")  #指定目录创建一个文件夹，名字不能重复
#os.removedirs("test") #删除指定的文件夹，没有时不能删除
print(os.getcwd()) #获取当前的绝对路径
print(os.path.exists("test")) #判断目录是否存在，返回布尔类型
#创建一个文件夹，和文件夹下面的文件，并写入数据
if not os.path.exists("test"):
    os.mkdir("test")
if not os.path.exists("test/1.txt"):
    f = open("test/1.txt","w")
    f.write("这是新建的文件，使用os库编写的")
    f.close()

#time模块常用方法
print(time.time()) #生成当前时间的时间戳
print(time.asctime()) #展示当前时间的西方格式
print(time.localtime()) #将时间戳转成时间元组，不填写时默认将当前时间戳转换成元组
print(time.strftime("%Y年%m月%d日  %H:%M:%S", time.localtime())) #格式化输出一个时间，前面填写时间格式，后面填写时间元祖

#获取两天前的时间
#time.sleep(3) #程序执行时，等待多少秒
now_time_stamp = time.time()
two_days_ago = now_time_stamp - 60*60*24*2
print(time.strftime("%Y年%m月%d日  %H:%M:%S", time.localtime(two_days_ago)))

#urllib 可以请求地址
import urllib.request
response = urllib.request.urlopen("https://www.baidu.com")
print(response.status)
print(response.headers)

#math库 科学计算的库
import math

print(math.ceil(3.5)) #向上取整
print(math.floor(5.999)) #向下取整
print(math.sqrt(256)) #开方，给出算术平方根，float类型