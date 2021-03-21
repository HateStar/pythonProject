# 开发时间2021/3/18 19:38
# 加油啊测试！
#使用全局变量
import copy

a = 1

def put1():
    global a
    a = 2
    print(a)
    print(id(a))
    #函数默认return none,只写return也是返回none
print(id(a))
put1()
print(id(a))

#使用嵌套函数，闭包函数
def demo1():
    def demo2():
        print("demo2")
    return demo2


if __name__ == '__main__': #python执行入口  main函数在文件被当做模块导入时不执行
    demo1()()


b = a
print(id(a))
print(id(b))
b = 3
print(id(b))
    #两个变量指向的内存空间互不影响

#浅拷贝：只拷贝第一层，不拷贝第2层
aa = [1,2,3,[4,5,6],4]
bb = aa.copy()
bb[0] = 11
print(aa)
print(bb)
bb[3][0] = 33
print(aa)
print(bb)
#深拷贝：完全拷贝出一个新的内容,原对象怎么变都不影响当前对象
aaa = [1,2,3,[4,5,6],4]
bbb = copy.deepcopy(aaa)
bbb[0] = 111
bbb[3][0] = 444
print("aaa",aaa)
print("bbb",bbb)

#from import相当于深拷贝
#import相当于浅拷贝