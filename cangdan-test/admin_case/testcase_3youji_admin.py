import time
import unittest
from selenium import webdriver
from admin_script.test_manage import TestManage
from user_case.BeautifulReport1 import BeautifulReport


class CaseYouji(unittest.TestCase):

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

    @BeautifulReport.add_test_img('悠技舱单信息总清单')
    def test_0001(self):
        TestManage(self.driver).manifest_im('悠技舱单管理')
        self.save_img('悠技舱单信息总清单')

    @BeautifulReport.add_test_img('悠技舱单信息统计')
    def test_0002(self):
        TestManage(self.driver).manifest_im_sas('悠技舱单管理')
        self.save_img('悠技舱单信息统计')

    @BeautifulReport.add_test_img('悠技舱单节点信息统计')
    def test_0003(self):
        TestManage(self.driver).manifest_node_im_sas('悠技舱单管理')
        self.save_img('悠技舱单节点信息统计')
