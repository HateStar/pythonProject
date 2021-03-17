# 开发时间2021/3/13 23:48
# 加油啊测试！
#使用随机数，做的原神抽卡模拟器
import random

class genshin():
    pass


def chouka(gacha_a=10):
    """

    :return:
    """
    #a = int(input("输入抽卡次数:")) #想要抽卡的次数
    a = gacha_a
    number = 0 #当前抽的是第几次
    count_90 = 0 #90保底计数
    count_10 = 0 #10次保底计数
    ssr = 0
    sr = 0
    r = 0

    while number < a:
        gacha = random.randint(1,1000)
        if count_90 > 73: #判断是否开始累加概率
            if gacha - (count_90 - 72) * 60 < 7:
                ssr = ssr +1
                count_10 = count_10 + 1
                count_90 = 0
                number = number + 1
            elif gacha > 6 and gacha < 52:
                sr = sr +1
                count_10 = 0
                count_90 = count_90 + 1
                number = number + 1
            else:
                r = r + 1
                count_10 = count_10 + 1
                count_90 = count_90 + 1
                number = number + 1
        else:
            if gacha < 7:
                ssr = ssr + 1
                count_90 = 0
                count_10 = count_10 + 1
                number = number + 1
            elif gacha > 6 and gacha < 52:
                sr = sr + 1
                count_10 = 0
                count_90 = count_90 + 1
                number = number + 1
            else:
                r = r +1
                count_10 = count_10 + 1
                count_90 = count_90 + 1
                number = number + 1
        if  count_10 == 9:  #4星保底计算
            if gacha - (count_90 - 72) * 60 < 7:
                count_10 = 0
            elif gacha < 7:
                count_10 = 0
            elif gacha > 6 and gacha < 52:
                count_10 = 0
            else:
                r = r -1
                sr = sr +1
                count_10 = 0
    print("SSR:" + str(ssr) + " " + str(ssr / gacha_a * 100) + "%")
    print("SR:" + str(sr)+ " " + str(sr / gacha_a * 100) + "%")
    print("R:" + str(r)+ " " + str(r / gacha_a * 100) + "%")
    return