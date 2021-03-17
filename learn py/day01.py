# 开发时间2021/3/2 21:25
# 加油啊测试！

#day01 print()函数  常用的转义字符
#输出数字
print(123)
#输出字符串
print("123")
print('123')
#含有运算符的表达式
print(1+3*5)
#将内容输出到文件中,注意点：1.所指定的【盘符必须存在 2.在print中使用file = open（'文件路径/文件名.后缀'，'a+'）
#这里的a+是写权限什么的，如果文件不存在将创建文件
file1 = open('E:/python_space/test1.txt','a+') #开启文件
print('这里是print输出的内容',file=file1)
file1.close() #关闭文件

#在一行内输出内容
print('第一，绝不意气用事','第二，','第三，')

#转义字符
print('hello\nworld') #换行
print('hello\tworld')#增加一个制表位的缩进（和按tab进行缩进同理），一个制表位占4个字母长度
print('helloooo\tworld')#前方内容可以被4整除时（占满了之前的制表位），\t就重开新的制表位，占4字母的长度，否则占用上个制表位的剩余部分
print('hello\rworld')#\r是将光标移到一行的开始,所以\r之后的内容会覆盖掉上次打印的内容
print('hello\bworld')#退格 打印之后使用\b删除之前的1个字符，之后继续打印后续内容

print('http:\\\\www.baidu.com')#使用\\  \\两个反斜杠来输出一个反斜杠
print('他说\' wdnmd\'') #使用\'来使该'不表示字符串的结束，而表示字符串的内容

#原字符：使字符串中的转义字符不生效，在字符串前加r或R  同时字符串的最后不能以单个反斜杠结束\
print(r'DDDD\recade')
#print(r'asd\')  错误示范
print(r'asd\\') #正确示范
