# 开发时间2021/3/13 12:05
# 加油啊测试！
#变量赋值
a = 1
b = 1
c,d = 3,4

print(a,b,c,d)

#数字类型 int float complex
int_a = 3
float_a = 44.5
complex_a = 1234j

print(type(complex_a))
print(type(int_a))
print(type(float_a))
#输出如下结果
#<class 'complex'>
#<class 'int'>
#<class 'float'>

#字符串

string_a = "第一行\n第二行"
print(string_a)

#想要输出\n时
string_b = "第一行\\n第一行"
string_c = r"第一1行\n第一1行" #r：忽略转义符的作用
print(string_b)
print(string_c)

#拼接字符串
print(string_c+string_b+string_a)
print("aa" "bb")
#+ 可以用在变量之间的连接，空格不能

#引用语法f+{} / format
D = "Decade"
DD = f"DDD{D}"
DDD = "DDD{}"
print(DD)
print(DDD.format(D))
#输出：DDDDecade

#多个变量使用format拼接的简单使用
D_a = "Dec"
D_b = "ade"
DDDD = "DDD{}{}"
print(DDDD.format(D_a,D_b))

#多个变量使用format拼接的精确使用
DDdd = "DDD{a}{b}"
print(DDdd.format(a=D_a,b=D_b))

#列表索引
list_a = [1,2,4,5,"asd","zxcv",2j]
print(list_a[0])
print(list_a[-2]) #倒数第2个值用-2 以此类推

#列表切片
print(list_a[3:5]) #取下标3-5之间，包括下标3，不包括下标5 区间：[3,5)
