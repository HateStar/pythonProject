# 开发时间2021/3/17 21:47
# 加油啊测试！
#python 的面向对象
class woDeLei():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def print1(self):
        print(f"我的类中，a={self.a},b={self.b}")
c = woDeLei(2,3)
c.print1()