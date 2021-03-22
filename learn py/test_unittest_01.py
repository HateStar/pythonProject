# 开发时间 2021/3/22 22:57
# 加油啊测试！！

import unittest

class TestGo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUPClass")
    def testOne(self):
        print("testone111")
        self.assertEqual(1, 1, "1")
    def testTwo(self):
        print("testtwo222")
        self.assertEqual(1,1,"1")
    def testThree(self):
        print("testtwo333")
        self.assertEqual(1, 2, "1")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
if __name__ == '__main__' :
    unittest.main()