# coding:utf-8
import os
import sys

current_directory = os.path.abspath(os.path.dirname(__file__))
print(current_directory)
rootPath = os.path.split(current_directory)[0]
print(rootPath)
sys.path.append(rootPath)
import unittest
import datetime
from user_case.testcase_1report import TestcaseReport
# 导入形成测试报告模板类
from other.BeautifulReport import BeautifulReport
from user_case.testcase_5money import TestcaseMoney
from user_case.testcase_6url import Testcase_url


class SuitTest(unittest.TestCase):

    def test_suit(self):
        # 设置测试报告的路径，文件名称
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        nowTime = datetime.datetime.now().strftime('%m%d%H%M')
        filename = str(nowTime) + '.html'
        path = '../report/' + time
        if os.path.exists(path):
            filepath = path
            url = filepath + '/' + filename
        else:
            os.mkdir(path)
            filepath = path
            url = filepath + '/' + filename

        # try:
        # rm_image.rm_image("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\img")
        #             # rm_image.del_files("C:\\Users\\wh\\Downloads\\")
        # except Exception as e:
        #     pass
        # 创建测试套件
        case_list = [TestcaseReport('test_0024')]
        mysuit = unittest.TestSuite()

        # 添加某个类中所有用例
        # mysuit.addTest(unittest.makeSuite(Testcase_url))
        mysuit.addTests(case_list)


        # 执行某个类中指定某些用例
        # 将测试用例放到测试套件中

        # for case in case_list:
        #     mysuit.addTest(Testcase_url(case))

        result = BeautifulReport(mysuit)
        result.report(description=u'悠易达测试报告', filename=filename, log_path=filepath)
        print(filename)


A = SuitTest()
A.test_suit()
