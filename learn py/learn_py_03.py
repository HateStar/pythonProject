# 开发时间2021/3/14 15:42
# 加油啊测试！
#函数的作用（封装好的代码段）：实现单一功能，或相关联功能的代码段；函数能提高应用的模块性，和代码的重复利用率
#函数调用：
from genshin import chouka  #其他文件调用函数时，需要import
import random
#chouka(1000000)
chouka()
#ctrl+d 可以复制一行代码
#函数不加return或者只写return，都会返回None
#默认参数：定义函数时使用k=v的形式，调用函数时不传参，就使用默认参数;传了参就用传的参数

#关键字参数：调用函数时，使用k=v的方式传参
#在函数调用、定义中，关键字必须跟随在位置参数后面
def func1(a=-1,b=-2,c=-3,d=-4):
    print("参数为：",a,b,c,d)
func1(1,3,d=12)

#lambda表达式 可以创建一个匿名函数

func2 = lambda z : z*3
print(func2(3))
#等价于下方func3
def func3(z):
    return z*3