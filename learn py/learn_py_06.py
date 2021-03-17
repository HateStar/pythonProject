# 开发时间2021/3/15 22:21
# 加油啊测试！
#python的输入与输出
#字面量
#字面量插值 格式化输出 通过string.format()方法拼接  Formatted string literals：字符串格式化机制(>=python3.6)(最推荐最简单)
#格式化输出 查看转换表 不演示了
#format（）方法
name = "Decade"
age = 20
print("my name is {0},age is {1}{1}{0}".format(name,age)) #{}里的数字代表填写format()里的第几个变量，可以多次调用
#format支持列表、字典
list1 = [1,2,3]
dic1 = {"a" : "a","b" : "b","c" : "c"}
print("输出列表{}和字典{}".format(list1,dic1))
#一个列表拆分多个元素输出到format中
print("现在有的数字{}{}{}".format(*list1)) #列表前方写一个*就是解包
#字典的解包
print("现在有的字母{a}{b}{b}".format(**dic1))

#F-strings:字符串格式化机制
#{}中可以放常量、变量、表达式、函数
#使用方法 f"这是一个字符串" 在字符串前面加f就可以了
print(f"我的名字是{name},age is {age},{list1[0]}{dic1['a']}")
#{}中不能转义\ 可以是函数或表达式
print(f"举例的表达式{3+2},{name.upper()}，{(lambda x:x**2)(2)}") #大写变量name  {}中不能加: 需要时用()括起来

#文件读取
#第一步 打开文件，获取文件描述符
#第二步 操作文件描述符 读或写
#第三步 关闭文件
#使用open()
a = open("learn_py_06.txt")
print(a.readable()) #查询文件是否可读
#print(a.readlines()) #读取文件的所有行并返回一个列表
print(a.readline()) #读取文件的一行
a.close()

#with语句块，可以将文件打开之后，操作完毕，自动关闭这个文件
with open("learn_py_06.txt","rt") as b:
    while True:
        line = b.readline()
        if line:
            print(line)
        else:
            break
#    print(b.readlines()) 会占用太多系统资源
# 图片读取需要使用rb 读取二进制的格式
#正常文本使用rt 也就是默认格式

#Json 格式转化
import json
data = {
    "name":["Decade","DDD"],
    "age":30,
    "ride":"kaman"
}

data1 = json.dumps(data) #将json转化为字符串
print(type(data))
print(data)
print(data1)
print(type(data1))
data2 = json.loads(data1) #将字符串转化为json
print(data2)
print(type(data2))