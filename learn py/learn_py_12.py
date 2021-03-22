# 开发时间 2021/3/22 19:56
# 加油啊测试！！
#第三方库：pytest requests
import requests
r = requests.get("https://www.baidu.com")
print(r.status_code) #返回的状态码
print(r.encoding)  #返回的编码格式
r.encoding = "utf-8"  #返回的编码格式不是utf-8时，下方text会是乱码 需要手动改下编码格式
print(r.text) #返回的内容