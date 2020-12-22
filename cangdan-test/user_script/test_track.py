import os
import random
import time
from selenium import webdriver

from common_data import common_value
from other.Commonlib import Commonshare, upload
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .test_report import TestReport


class TestTrack(Commonshare):
    """物流节点跟踪"""

    def query_track(self):
        """口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_css_selector('#main-navigation > ul > li:nth-child(3) > a').click()
        driver.find_element_by_link_text('口岸数据').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="BILL_NBR"]').send_keys('W')
        driver.find_element_by_xpath('//*[@id="BARGE_NAM"]').send_keys('W')
        driver.find_element_by_xpath('//*[@id="BARG_VOYAGE_NO"]').send_keys('WW')
        driver.find_element_by_link_text('查询').click()
        i = self.get_length('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[4]', '口岸数据查询')
        assert_list.append(i)
        driver.find_element_by_link_text('重置').click()
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[8]/a').click()
        TestTrack.el_show(self, 'text', '取消', '取消')
        driver.find_element_by_link_text('取消').click()
        # time.sleep(2)
        # TestTrack.el_show(self, 'text', '批量订阅', '批量订阅')
        # time.sleep(2)
        # # js = 'document.getElementByClassName(" icon-action-new ").click();'
        # # driver.execute_script(js)
        # driver.find_element_by_link_text('批量订阅').send_keys(Keys.ENTER)
        # time.sleep(1)
        # os.system(r'D:\模板文件\test.exe "D:\模板文件\新舱单节点查询导入模板.xlsx"')
        # self.el_show('css', '#toast-container > div > div.toast-message', '提示')
        # i = self.compare_el('css', '#toast-container > div > div.toast-message', '*成功', '批量订阅')
        assert_list.append(i)
        if 0 in assert_list:
            assert (1 == 2)

    # def sub_im(self):
    #     """上传批量模板文件"""
    #     url = 'http://192.168.17.50:4528/excelimport/billnodeinfo'
    #     file = {"file": open(common_value.SUBFILE, "rb")}
    #     data = {
    #         "file": file,
    #         "userLoginId": "customer1"
    #     }
    #     upload(url=url, file=file, data=data)

    def down_db(self):
        """新舱单节点查询导入模板下载"""
        driver = self.driver
        driver.find_element_by_css_selector('#main-navigation > ul > li:nth-child(3) > a').click()
        driver.find_element_by_link_text('新舱单节点查询导入模板下载').click()
        time.sleep(10)
        if os.path.exists(r"C:\Users\wh\Downloads\新舱单节点查询导入模板.xlsx"):
            print('新舱单节点查询导入模板下载 ok')
        else:
            print('新舱单节点查询导入模板下载 error')

    def check(self):
        """ 查验数据: 查询 > 添加订阅 > 批量订阅 > 重置"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_css_selector('#main-navigation > ul > li:nth-child(3) > a').click()
        driver.find_element_by_link_text('查验数据').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        driver.execute_script(js)
        driver.find_element_by_link_text('查询').click()
        i = self.get_length('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[2]','查验数据')
        assert_list.append(i)
        if 0 in assert_list:
            assert (1 == 2)
        driver.find_element_by_link_text('重置').click()

    def down_cd(self):
        """查验数据查询导入模板下载"""
        driver = self.driver
        driver.find_element_by_css_selector('#main-navigation > ul > li:nth-child(3) > a').click()
        driver.find_element_by_link_text('查验数据').click()
        driver.find_element_by_link_text('查验数据查询导入模板下载').click()
        time.sleep(10)
        if os.path.exists(r"C:\Users\wh\Downloads\新舱单查验数据导入模板.xlsx"):
            print('新舱单查验数据导入模板下载 ok')
        else:
            print('港新舱单查验数据导入模板下载 error')

