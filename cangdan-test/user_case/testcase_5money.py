import os
import time
import unittest
from selenium import webdriver
from common_data import common_value
from other.BeautifulReport import BeautifulReport
from other.Commonlib import upload


class TestcaseMoney(unittest.TestCase):
    """费用管理"""

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
        """关闭浏览器"""
        self.driver.quit()

    @BeautifulReport.add_test_img('费用管理')
    def test_0001(self):
        """费用管理"""
        from user_script.test_money import TestMoney
        log = TestMoney(self.driver)
        log.test_money()
        self.save_img('费用管理')

    # def test_0002(self):
    #     url = "http://192.168.17.50:4528/uploadDepositSlip"
    #     file = common_value.SHUIDAN
    #     data = {"userLoginId": "customer1",
    #             "abnormalUser": "false",
    #             "inputer": "",
    #             "depositAmount": "1111",
    #             "depositDate": "2019-12-04",
    #             "depositor": "1111",
    #             "depositType": "0",
    #             "uploadImg": common_value.SHUIDAN}
    #     upload(url, file, data)