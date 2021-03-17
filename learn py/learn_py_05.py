# 开发时间2021/3/15 21:33
# 加油啊测试！
#模块
#第三方开源模块 需要使用 pip install 模块名 来安装
import yaml
import requests
import genshin #使用from 模块 import 方法时， 可以直接调用方法 但import 模块时， 需要模块.方法才能调用
from genshin import * #如果模块中的变量、方法、类太多，可以直接用*代表全部
import sys
#import 应该放在代码的最顶端
genshin()
chouka(75)

print(dir()) #展示当前模块下可以调用的变量、方法、类
print(dir(genshin))
print(sys.path)
#使用模块的总结
#提升代码可维护性 提升编码效率 函数名可重复（起名避免与系统重复）