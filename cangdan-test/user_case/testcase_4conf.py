import os
import time
import unittest

from selenium import webdriver

from common_data import common_value
from user_script.test_conf import Test_conf
from other.BeautifulReport import BeautifulReport


class TestcaseConf(unittest.TestCase):
    """基础配置"""

    def setUp(self) -> None:
        opt = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': common_value.DOWNLOAD_PATH}  # 默认下载地址
        opt.add_experimental_option('prefs', prefs)
        opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        opt.add_argument("--window-size=1600,900")
        if os.name == "nt":
            self.driver = webdriver.Chrome(executable_path=common_value.CHROMEDRIVER, options=opt)
        else:
            opt.add_argument('--headless')
            opt.add_argument('--no-sandbox')
            # opt.add_argument('lang=zh_CN.UTF-8')
            self.driver = webdriver.Chrome(executable_path=common_value.CHROMEDRIVER, options=opt)

        self.driver.get('http://192.168.17.50:2090/home/control/main')
        driver = self.driver
        driver.find_element_by_name('USERNAME').send_keys('customer1')
        driver.find_element_by_name('PASSWORD').send_keys('123456')
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file(
            common_value.IMAGE + "%s.png" % img_name)

    def tearDown(self) -> None:
        self.driver.quit()

    @BeautifulReport.add_test_img('基础配置')
    def test_0001(self):
        """基础配置"""
        log = Test_conf(self.driver)
        log.test_conf()
        self.save_img('基础配置')

    @BeautifulReport.add_test_img('基础配置-邮箱管理')
    def test_0002(self):
        """基础配置-邮箱管理"""
        Test_conf(self.driver).test_email()
        self.save_img('基础配置-邮箱管理')

    @BeautifulReport.add_test_img('基础配置-手机号管理')
    def test_0003(self):
        """基础配置-手机号管理"""
        Test_conf(self.driver).test_mobile()
        self.save_img('基础配置-手机号管理')