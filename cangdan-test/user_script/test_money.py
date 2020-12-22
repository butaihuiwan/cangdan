import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common_data import common_value
from other.Commonlib import Commonshare, upload


class TestMoney(Commonshare):
    """ 费用账单: 预配舱单计费 > 口岸数据服务计费 > 港区数据服务计费 > 查询数据服务计费"""

    def test_money(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[8]/a').click()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-09-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[3]/a').click()
        self.el_show('xpath', '//*[@id="toast-container"]/div/div[2]', '预配舱单计费查询')
        driver.find_element_by_xpath('//*[@id="downloadBtn"]').click()

        # 口岸数据服务计费
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-09-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[3]/a').click()
        self.el_show('xpath', '//*[@id="toast-container"]/div/div[2]', '口岸数据服务计费查询')

        # 港区数据服务计费
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-08-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[3]/a').click()
        self.el_show('xpath', '//*[@id="toast-container"]/div/div[2]', '港区数据服务计费')

        # 查验数据服务计费
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-08-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[3]/a').click()
        self.el_show('xpath', '//*[@id="toast-container"]/div/div[2]', '查验数据服务计费')

        """水单管理： 上传 > 查看水单
        接口测试，返回状态码 200 视为成功"""
        # driver.find_element_by_link_text('水单管理').click()
        # # 上传
        # driver.find_element_by_link_text('上传').click()
        # self.el_show('xpath', '//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[1]/div/div/input', '充值金额加载')
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[1]/div/div/input').send_keys(
        #     '100')
        #
        # self.el_show('xpath', '//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[2]/div/div/input', '充值日期加载')
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[2]/div/div/input').send_keys(
        #     '2019-10-30')
        #
        # self.el_show('xpath', '//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[2]/div/div/input', '付款人加载')
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[2]/div/div/input').click()
        # driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[3]/div/div/input').send_keys(
        #     '100')
        #
        # self.el_show('xpath', '//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[3]/div/div/input', '支付类型')
        # el = driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[4]/div/div/select')
        # select = Select(el)
        # select.select_by_visible_text('代付')
        # el = driver.find_element_by_xpath('//*[@id="uploadImg"]')
        # time.sleep(2)
        # ActionChains(driver).move_to_element(el).move_by_offset(5, 5).click().perform()
        # time.sleep(2)
        # """上传水单模板文件"""
        # os.system(
        #     '%s "%s"' % (common_value.AUEXE, common_value.SHUIDAN))
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[2]/button').click()
        # url = "http://192.168.17.50:4528/uploadDepositSlip"
        # file = common_value.SHUIDAN
        # data = {"userLoginId": "customer1",
        #         "abnormalUser": "false",
        #         "inputer": "",
        #         "depositAmount": "1111",
        #         "depositDate": "2019-12-04",
        #         "depositor": "1111",
        #         "depositType": "0",
        #         "uploadImg": common_value.SHUIDAN}
        """查看"""
        driver.find_element_by_link_text('水单管理').click()
        driver.find_element_by_xpath('//*[@id="exchangeListTable"]/tbody/tr[1]/td[8]/a').click()
        self.el_show('xpath', '//*[@id="detailDiv"]/img', '水单图片元素加载')
        url = self.get_attr('xpath', '//*[@id="detailDiv"]/img', 'src')
        print(url)
        try:
            driver.get(url)
            print('水单图片查看 ok')
        except:
            print('水单图片查看失败')
            raise
