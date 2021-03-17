# 开发时间2021/3/14 17:14
# 加油啊测试！
#常见的数据结构：列表、元祖、集合、字典
#列表
list_Decade = [5,9,7,56,1,5,3,5,2,4,9,87,7]
#list_Decade.append("Kuuga") #在列表末尾添加一个元素
#list_Decade.insert(1,"Agito")#在列表指定索引的位置插入一个元素 0代表第一个元素位置 a.insert(len(a),x)代表插入到最后
#list_Decade.remove("Agito")#删除列表中第一个指定值的元素，如果没有就抛出ValueError异常
#a = list_Decade.pop(1) #删除指定位置的元素并返回那个值
#print(a)
#list_Decade.sort(reverse=True) #将列表中的内容排序，reverse=True时，按倒序排序，不填写时默认reverse=False
list_Decade.reverse() #将列表中的内容反转，当前内容变成从后向前展示
#其他用法参见python的api文档
print(list_Decade)

"""
生成一个平方列表，比如[1,4,9...]使用for循环怎么写，使用列表生成式怎么写？
"""
list_j = []
for i in range(1,5):
    list_j.append(i**2)
print(list_j)
#接下来是推导式
list_jj = [i**2 for i in range(1,5) if i != 1] #直接用
print(list_jj)
#还可以直接使用嵌套循环
list_qiantao = [i*j for i in range(1,4) for j in range(1,4)]
#执行顺序是 先略过一开始的推导式 从第二句话依次向后执行 最后执行一开始的推导式 这样重复
print(list_qiantao)

#元组 使用()定义 tuple（元组） list（列表） range都是序列数据类型 元组是不可变的 可以通过解包、索引来访问
tuple_a = (1,2,3)
tuple_b = 1,2,3  #不使用（）时，定义的也是元组

print(type(tuple_a))
print(type(tuple_b))

#元组的不可变特性
#tuple_a [0] = 1
#直接修改会报错：TypeError: 'tuple' object does not support item assignment
#但元组中嵌套列表时，元组中存放的是变量指针，修改变量不会导致变量指针发生改变
a = 123
print(id(a),"a")
b = [0,1,2,3]
tuple_c = (1,2,a,b)
a = 456
print(id(a),"a")
print(id(b),"b")
tuple_c[3][3] = 5
print(id(b),"b")
print(tuple_c)
print(a)

#元组的内置函数
print(tuple_c.count(1)) #计算这个值在元组中出现了几次
print(tuple_c.index(123))#计算这个值在元组中的索引

#集合 由不重复元素组成的无序的集 基本用法包括成员检测和消除重复元素 可以使用{}或者set()函数创建集合
# 要创建一个空集合只能用set() 不能用{}
aa = {1}
bb = set()
print(type(aa),type(bb))
print(len(bb)) #查看集合长度 为0时就是空集合

#集合的常用内置函数
aaa = {1,3,5}
bbb = {1,2,3,4,5,6,7}

print(aaa.union(bbb)) #求两个集合的并集
print(aaa.intersection(bbb)) #求交集
print(bbb.difference(aaa)) #求差集 第一个集合中有，第二个集合中没有的元素
aaa.add("a")#在集合中增加元素 因为是无序的 所以没有索引
print(aaa)
#集合使用推导式
print({i for i in "asdasgasdcvcxaswersdfasdcxv"}) #别忘了加{}
#等同于：
ccc = "asdsiogjoisdhvnjuaioseythssmdv"
print(set(ccc))

#字典 k：v
# 以关键字为索引 关键字可以是任意不可变类型，通常是字符串或数字 如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字
dict_a = {"a":1,"b":2}
dict_b = dict(a=1,b=2)
print(dict_a)
print(type(dict_a))
print(dict_b)
print(type(dict_b))
print(dict_a.keys(),dict_a.values())
#print(dict_a.pop("a")) #删除指定k的kv
print(dict_a.popitem())#随机删除键值对,并返回这个键值对
print(dict_a)

dict_c = {}
dict_d = dict_c.fromkeys({1,2,3},"c") #fromkeys 拿出来一组k，一个v 生成一个字典
print(dict_d)

#字典推导式
print({i:i**2 for i in range(1,5)})
