# 开发时间2021/3/16 23:50
# 加油啊测试！
#错误和异常
#错误基本都是语法错误，熟练之后可以避免
#主要看异常

from genshin import chouka

class MyError(Exception): #自定义异常类
    def __init__(self):
        self.value = 90


while True:
    try:
        x = int(input("请输入抽卡次数："))
        if x > 90:
            raise MyError
    except ValueError:
        print("您输入的不是数字，请再次尝试") #要求输入int，输入了非数字，不能转换成int时报错
    except MyError as asd:
        print(f"您一次最多只能抽{asd.value}发")
    else:
        chouka(x)
        break
    finally:
        print("finally")
print("抽卡结束")

#预定义的清理行为
with open("learn_py_06.txt") as ff:
    for line in ff:
        print(line, end="")