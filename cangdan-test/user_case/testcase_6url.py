import unittest

from user_script.test_url import Test_url


class Testcase_url(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_0001(self):
        """接口测试：注册"""
        re = Test_url()
        re.regit()

    def test_0002(self):
        """接口测试：舱单模板表格导入"""
        ex = Test_url()
        ex.import_excel()

    def test_0003(self):
        """导入舱单报文模板文件"""
        im = Test_url()
        im.import_edi()

    def test_0004(self):
        """上传批量订阅模板文件"""
        sub = Test_url()
        sub.sub_im()
