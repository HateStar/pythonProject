# 开发时间2021/3/13 22:26
# 加油啊测试！

import random
#分支结构
a = 0
#单分支
if a == 0:
    print("a==0")
else:
    print("a!=0")
#多重分支
b = 0

if a == 0 & b != 0:
    print("a == 0 and b != 0")
elif a == 0 & b == 0:
    print("a == 0 and b == 0")
elif a != 0 & b != 0:
    print("a != 0 and b != 0")
else:
    print("a != 0 and b == 0")

#分支嵌套
if a == 0:
    if b == 0:
        print("a=0,b=0")
    else:
        print("a=0,b!=0")
else:
    print("a!=0")
#能扁平的时候就不嵌套：嵌套层数多了之后可读性会下降
print("------------------------------------------------------")
#range函数：产生一个不变的数值序列，且这个序列通常会用在循环中
'''
range(101)产生0到100的整数序列
range(1,100)1到99的整数序列
range(1,100,2)1到99的奇数整数序列，2是步长，每次+2
'''

#for-in循环 明确知道要执行的次数时，推荐for循环
#对1到100求和
'''
    count = 0
    for i in range(101):
        print(i)
        count = count+i
    print(count)
'''
#加入分支结构，实现1到100的偶数求和
count_1 = 0
for j in range(101):
    if (j+2)%2 == 0:
        count_1 = count_1 + j
#    print(count_1)
#震惊！ 如上，else里不执行任何语句时，就不需要else了

#使用range()实现1到100的偶数求和
count_2 = 0
for k in range(2,101,2):
    count_2 = count_2 + k
print(count_2)

#while循环 不知道具体循环次数时，推荐使用while循环
l = 0
while l < 5:
    print(l)
    l = l +1
else:
    print("l大于等于5了")
#如果while循环体中只有一条语句，就可以将该语句写在while的同一行

#break和continue

#计算机生成一个数字，人工输入一个数字，不等时给出提示，相等时游戏结束
#random库中可以生成随机数
computer_number = random.randint(1,100)

while True:
        person_number = int(input("请输入一个数字\n"))
        if computer_number == person_number:
            print("猜对了")
            break
        elif computer_number > person_number:
            print("小了")
        else:
            print("大了")
