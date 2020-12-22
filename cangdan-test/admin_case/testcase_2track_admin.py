import random
import time
import unittest
from selenium import webdriver
from user_script.test_report import TestReport
from admin_script.test_track_admin import TestTrackAdmin
from other.BeautifulReport1 import BeautifulReport
from admin_script.test_manage import TestManage


# class CaseTrackAdmin(unittest.TestCase):
#     """预备舱单申报"""
#
#     def setUp(self):
#         """登陆管理员账号"""
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://192.168.17.50:2090/home/control/main')
#         driver = self.driver
#         # 设置隐士等待时间 10s
#         driver.implicitly_wait(10)
#         driver.find_element_by_name('USERNAME').send_keys('company')
#         driver.find_element_by_name('PASSWORD').send_keys('123456')
#         driver.maximize_window()
#         time.sleep(1)
#         login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
#         login.click()
#
#     def save_img(self, img_name):
#         """截图"""
#         self.driver.get_screenshot_as_file("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\img\\%s.png" % img_name)
#
#     def tearDown(self) -> None:
#         """关闭浏览器"""
#         self.driver.quit()
#         time.sleep(2)
#
#     @BeautifulReport.add_test_img('待发送-查询')
#     def test_0001(self):
#         """申报预备舱单：待发送-查询"""
#         TestReport(self.driver).query()
#         self.save_img('待发送-查询')
#
#     @BeautifulReport.add_test_img('待发送-新增-创建-暂存')
#     def test_0002(self):
#         """ 待发送-- 新增 > 创建 > 暂存"""
#         add = TestReport(self.driver)
#         num = str(random.randint(1, 10000))
#         TDH = 'ex' + num
#         add.add_creat(TDH, num, num)
#         # self.save_img('待发送-新增-创建-暂存')
#
#     @BeautifulReport.add_test_img('新增发送')
#     def test_0003(self):
#         """待发送-- 新增 > 发送"""
#         add = TestReport(self.driver)
#         num = str(random.randint(1, 1000))
#         print(num)
#         TDH = 'ex' + num
#         add.seed(TDH, num, num)
#         self.save_img('新增发送')
#
#     @BeautifulReport.add_test_img('导入')
#     def test_0004(self):
#         """待发送--导入"""
#         im = TestReport(self.driver)
#         im.import_excel()
#         self.save_img('导入')
#
#     @BeautifulReport.add_test_img('批量发送')
#     def test_0005(self):
#         """待发送--批量发送"""
#         se = TestReport(self.driver)
#         se.seed_more()
#         self.save_img('批量发送')
#
#     @BeautifulReport.add_test_img('待发送-修改-暂存')
#     def test_0006(self):
#         """待发送-- 修改-暂存"""
#         num = str(random.randint(1, 1000))
#         TDH = 'ex' + num
#         TestReport(self.driver).update_wait_seed(TDH, num, num)
#         self.save_img('待发送-修改-暂存')
#
#     @BeautifulReport.add_test_img('待发送-修改-发送')
#     def test_0007(self):
#         """待发送-- 修改-发送"""
#         num = str(random.randint(1, 1000))
#         TDH = 'ex' + num
#         TestReport(self.driver).update_wait_exist(TDH, num, num)
#         self.save_img('待发送-修改-发送')
#         # 代发送-- excel查看
#
#     @BeautifulReport.add_test_img('待发送--excel查看')
#     def test_0008(self):
#         """待发送-- excel查看"""
#         excel = TestReport(self.driver)
#         excel.excel_history()
#         self.save_img('待发送--excel查看')
#         # 待发送--删除
#
#     @BeautifulReport.add_test_img('待发送--删除')
#     def test_0009(self):
#         """待发送--删除"""
#         rm = TestReport(self.driver)
#         rm.rm_wait_seed()
#         self.save_img('待发送--删除')
#         # 已发送--查询
#
#     @BeautifulReport.add_test_img('已发送--查询')
#     def test_0010(self):
#         """已发送--查询"""
#         se = TestReport(self.driver)
#         se.select_seed()
#         self.save_img('已发送--查询')
#         # 已发送--修改
#
#     @BeautifulReport.add_test_img('暂存，更改报文重新发送')
#     def test_0013(self):
#         """已发送--修改-暂存，更改报文重新发送"""
#         update = TestReport(self.driver)
#         update.update_seed()
#         self.save_img('暂存，更改报文重新发送')
#
#         # 已发送--复制新增 > 创建 >暂存
#
#     @BeautifulReport.add_test_img('复制新增-创建-暂存')
#     def test_0014(self):
#         """已发送--复制新增 > 暂存"""
#         log = TestReport(self.driver)
#         num = str(random.randint(1, 1000))
#         TDH = 'TEST' + num
#         log.copy_add01(TDH, num, num)
#         self.save_img('复制新增-创建-暂存')
#
#     @BeautifulReport.add_test_img('已发送--复制新增 > 发送')
#     def test_0016(self):
#         """已发送--复制新增 > 发送"""
#         num = str(random.randint(1, 1000))
#         TDH = 'TEST' + num
#         TestReport(self.driver).copy_add02(TDH, num, num)
#         self.save_img('已发送--复制新增 > 发送')
#
#     @BeautifulReport.add_test_img('已发送--excel 查看')
#     def test_0017(self):
#         """已发送--excel 查看"""
#         ex = TestReport(self.driver)
#         ex.excel_history_seed()
#         self.save_img('已发送--excel 查看')
#
#     @BeautifulReport.add_test_img('已发送--报文历史查看')
#     def test_0018(self):
#         """已发送--报文历史查看"""
#         re = TestReport(self.driver)
#         re.report_history()
#         self.save_img('已发送--报文历史查看')