# 开发时间 2021/3/22 22:19
# 加油啊测试！！
#unittest课程
import unittest

class testDemo1(unittest.TestCase):
    # 类方法的上一行要这么写
    # 执行全部用例之前，先执行setUpClass方法，可以进行全局的准备

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    # 执行全部用例之后，最后执行tearDownClass方法，可以进行全局的清除

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None: #执行每条用例之前会先执行setUp，可以进行准备工作
        print("setUp")

    def tearDown(self) -> None: #执行每条用例之后会执行tearDown，可以进行清除等工作
        print("tearDown")

    def test_case01(self): #case要以test打头才能被识别
        print("test_case01")
        self.assertEqual(1,1,"不相等")

    def test_case02(self): #case要以test打头才能被识别
        print("test_case02")
        self.assertEqual(3,3,"不相等")

    @unittest.skipIf(1+1==2,"跳过这条case") #直接用skip就是无条件跳过，加if就是True条件跳过
    def test_case03(self): #case要以test打头才能被识别
        print("test_case03")
        self.assertEqual("1","2","不相等")
class testDemo2(unittest.TestCase):

    def test_Demo2_case1(self):
        print("test_Demo2_case1")

    def test_Demo2_case2(self):
        print("test_Demo2_case2")

if __name__ == '__main__':
    #unittest.main()
    #在容器unittest.TestSuite()中添加测试用例，只执行容器内的case
    suite = unittest.TestSuite()
    suite.addTest(testDemo1("test_case02"))
    suite.addTest(testDemo2("test_Demo2_case1"))
    unittest.TextTestRunner().run(suite)

    #在容器中加入测试类下的所有case，同时执行多个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testDemo1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(testDemo2)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
    #匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例