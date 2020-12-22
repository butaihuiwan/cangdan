import os
import sys
current_directory = os.path.abspath(os.path.dirname(__file__))
print(current_directory)
rootPath = os.path.split(current_directory)[0]
print(rootPath)
sys.path.append(rootPath)
import unittest
import datetime
from other.BeautifulReport import BeautifulReport
from common_data import common_value

# 导入形成测试报告模板类

from other import rm_image


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
        """删除img目录中上次保存的图片
           删除下载的模板文件"""
        # try:
        #     rm_image.rm_image("C:\\Users\\TP\\PycharmProjects\\cangdan-test\\suit\\img")
        #     # rm_image.del_files("C:\\Users\\TP\\Downloads\\")
        # except Exception as e:
        #     pass

        # 测试case目录下所有的测试用例
        if os.name == 'nt':
            test_dir = common_value.PROJECT_DIRECTORY + "\\user_case"
        else:
            test_dir = common_value.PROJECT_DIRECTORY + '/user_case'

        discover = unittest.defaultTestLoader.discover(test_dir, pattern='testcase_*.py')

        # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        result = BeautifulReport(discover)
        result.report(description='悠易达测试报告', filename=filename, log_path=filepath)


B = SuitTest()
B.test_suit()
