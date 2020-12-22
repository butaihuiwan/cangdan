import os
import time

from selenium import webdriver

from common_data import common_value
from user_script.test_track import TestTrack
import unittest
from other.BeautifulReport import BeautifulReport

class TestcaseTrack(unittest.TestCase):
    """数据服务"""

    def setUp(self) -> None:
        opt = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': common_value.DOWNLOAD_PATH}  # 默认下载地址
        opt.add_experimental_option('prefs', prefs)
        opt.add_argument("--window-size=1600,900")
        opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
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

    @BeautifulReport.add_test_img('口岸数据')
    def test_0001(self):
        """ 口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比"""
        log = TestTrack(self.driver)
        log.query_track()
        self.save_img('口岸数据')

    @BeautifulReport.add_test_img('新舱单节点查询导入模板下载')
    def test_0002(self):
        """新舱单节点查询导入模板下载"""
        log = TestTrack(self.driver)
        log.down_db()
        self.save_img('新舱单节点查询导入模板下载')

    @BeautifulReport.add_test_img('查验数据')
    def test_0003(self):
        """查验数据: 查询 > 添加订阅 > 批量订阅 > 重置"""
        log = TestTrack(self.driver)
        log.check()
        self.save_img('查验数据')

    @BeautifulReport.add_test_img('查验数据查询导入模板下载')
    def test_0004(self):
        """查验数据查询导入模板下载"""
        log = TestTrack(self.driver)
        log.down_cd()
        self.save_img('查验数据查询导入模板下载')

    # def test_0005(self):
    #     """接口测试： 上传批量模板文件"""
    #     sub = TestTrack(self.driver)
    #     sub.sub_im()
