import time
import unittest
from selenium import webdriver
from user_case.BeautifulReport1 import BeautifulReport
from admin_script.test_manage import TestManage


class CaseManage(unittest.TestCase):

    def setUp(self):
        """登陆管理员账号"""
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.17.50:2090/home/control/main')
        self.driver.maximize_window()
        driver = self.driver
        # 设置隐士等待时间 10s
        driver.implicitly_wait(10)
        driver.find_element_by_name('USERNAME').send_keys('company')
        driver.find_element_by_name('PASSWORD').send_keys('123456')
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\img\\%s.png" % img_name)

    def tearDown(self) -> None:
        """关闭浏览器"""
        self.driver.quit()
        time.sleep(2)

    @BeautifulReport.add_test_img('舱单信息总清单')
    def test_0001(self):
        """ 舱单信息总清单：查询，查看 ,excel历史，报文历史，重置"""
        TestManage(self.driver).manifest_im('舱单管理')
        self.save_img('舱单信息总清单')

    @BeautifulReport.add_test_img('代发信息总清单')
    def test_0002(self):
        """ 代发信息总清单：查询，查看 ,excel历史，报文历史，重置"""
        TestManage(self.driver).substitute_im()
        self.save_img('代发信息总清单')

    @BeautifulReport.add_test_img('舱单信息统计')
    def test_0003(self):
        """舱单信息统计: 查询，重置"""
        TestManage(self.driver).manifest_im_sas('舱单管理')
        self.save_img('舱单信息统计')

    @BeautifulReport.add_test_img('舱单节点信息统计')
    def test_0004(self):
        """ 舱单节点信息统计：查询，重置"""
        TestManage(self.driver).manifest_node_im_sas('舱单管理')
        self.save_img('舱单节点信息统计')

    @BeautifulReport.add_test_img('计费统计')
    def test_0005(self):
        """ 计费统计: 查询，扣费明细下载"""
        TestManage(self.driver).money_sas()
        self.save_img('计费统计')

    @BeautifulReport.add_test_img('水单审核')
    def test_0006(self):
        """  水单审核：查询， 查看，重置"""
        TestManage(self.driver).water_list()
        self.save_img('水单审核')

    @BeautifulReport.add_test_img('计费规则管理')
    def test_0007(self):
        """计费规则管理：查询，新增"""
        TestManage(self.driver).money_rule()
        self.save_img('计费规则管理')

    @BeautifulReport.add_test_img('EDI解析记录')
    def test_0008(self):
        """ EDI解析记录：查询，解析问价名称下载，重置"""
        TestManage(self.driver).edi_history()
        self.save_img('EDI解析记录')

    @BeautifulReport.add_test_img('用户管理')
    def test_0009(self):
        """用户管理：查询，余额（用户费用明细），预配舱单，提单确认，口岸服务，港区服务，查验服务，新增，新增二级代发账号，重置"""
        TestManage(self.driver).user_admin()
        self.save_img('用户管理')
