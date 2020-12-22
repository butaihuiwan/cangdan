import time

from other.Commonlib import Commonshare
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class TestManage(Commonshare):
    """
    舱单管理：
        舱单信息总清单：查询，查看 ,excel历史，报文历史，重置
        代发信息总清单：查询，查看 ,excel历史，报文历史，重置
         舱单信息统计: 查询，重置
         舱单节点信息统计：查询，重置
         计费统计: 查询， 扣费明细下载
         水单审核：查询， 查看，重置
         计费规则管理：查询，新增
         EDI解析记录：查询，解析问价名称下载，重置
         用户管理：查询，余额（用户费用明细），预配舱单，提单确认，口岸服务，港区服务，查验服务，新增，新增二级代发账号，重置
    """

    def manifest_im(self, name):
        """ 舱单信息总清单：查询，查看 ,excel历史，报文历史，重置"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_link_text(name).click()
        time.sleep(2)
        self.rm_imput('xpath', '//*[@id="from"]')
        driver.find_element_by_xpath('//*[@id="from"]').send_keys('2019-10-30')
        driver.find_element_by_link_text('查询').click()
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr/td[14]/a[1]', '查询数据"查看”加载')
        """断言是否查出数据"""
        i = self.get_length('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr/td[14]/a[1]', '舱单信息总清单查询')
        assert_list.append(i)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr/td[14]/a[1]').click()
        driver.find_element_by_css_selector('#close > .fa').click()
        time.sleep(1)
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[14]/a[2]', 'excel历史点击加载')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[14]/a[2]').click()
        time.sleep(1)
        driver.find_element_by_link_text('取消').click()
        time.sleep(1)
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[14]/a[3]', '报文历史点击加载')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[14]/a[3]').click()
        time.sleep(1)
        driver.find_element_by_link_text('取消').click()
        time.sleep(2)
        self.el_show('xpath', '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div[3]/div/a[2]', '重置点击加载')
        driver.find_element_by_xpath(
            '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div[3]/div/a[2]').click()
        el = driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/input').get_attribute('value')
        num = len(el)
        """判断是否重置"""
        assert (0 == num)
        if i == 0:
            assert (1 == 2)

    def substitute_im(self):
        """ 代发信息总清单：查询，查看 ,excel历史，报文历史，重置"""
        driver = self.driver
        driver.find_element_by_link_text('舱单管理').click()
        driver.find_element_by_link_text('代发信息总清单').click()
        time.sleep(1)
        self.time_select('from', '2019-10-30')
        driver.find_element_by_link_text('查询').click()
        time.sleep(1)
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[17]/a[1]', '查看点击加载')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[17]/a[1]').click()
        driver.find_element_by_css_selector('#close > .fa').click()
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[17]/a[2]', 'excel历史点击加载')

        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[17]/a[2]').click()
        driver.find_element_by_link_text('取消').click()
        time.sleep(2)
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[17]/a[3]', '报文历史点击加载')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[17]/a[3]').click()
        time.sleep(1)
        driver.find_element_by_link_text('取消').click()
        time.sleep(2)
        self.el_show('text', '重置', '重置点击加载')
        driver.find_element_by_link_text('重置').click()
        el = driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/input').get_attribute('value')
        num = len(el)
        assert (0 == num)

    def manifest_im_sas(self, name):
        """舱单信息统计: 查询，重置"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_link_text(name).click()
        driver.find_element_by_link_text('舱单信息统计').click()
        js = 'document.getElementById("from").value = "2018-10-30"'
        driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        # 判断查询
        i = self.get_length('xpath',
                            '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div[3]/div[1]/label[2]',
                            '舱单信息统计查询')
        assert_list.append(i)
        self.el_show('text', '重置', '重置点击加载')
        driver.find_element_by_link_text('重置').click()

    def manifest_node_im_sas(self, name):
        """ 舱单节点信息统计：查询，重置"""
        driver = self.driver
        driver.find_element_by_link_text(name).click()
        driver.find_element_by_link_text('舱单节点信息统计').click()
        js = 'document.getElementById("from").value = "2018-10-30"'
        driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        time.sleep(2)
        self.el_show('text', '重置', '重置点击加载')
        driver.find_element_by_link_text('重置').click()

    def money_sas(self):
        """ 计费统计: 查询，扣费明细下载 """
        driver = self.driver
        assert_list = []
        driver.find_element_by_link_text('舱单管理').click()
        driver.find_element_by_link_text('计费统计').click()
        js = 'document.getElementById("from").value = "2019-08-30"'
        driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        i = self.compare_el('xpath', '//*[@id="toast-container"]/div/div[2]', '*成功', '查询')
        assert_list.append(i)
        if 0 in assert_list:
            assert (1 == 2)
        driver.find_element_by_link_text('扣费明细下载').click()

    def water_list(self):
        """  水单审核：查询， 查看，重置"""
        driver = self.driver
        driver.find_element_by_link_text('舱单管理').click()
        driver.find_element_by_link_text('水单审核').click()
        js = 'document.getElementById("from").value = "2019-08-30"'
        driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        self.el_show('text', '查看', '查看点击加载')
        driver.find_element_by_link_text('查看').click()
        self.el_show('text', '取消', '取消点击加载')
        driver.find_element_by_link_text('取消').click()
        self.el_show('text', '重置', '重置点击加载')
        driver.find_element_by_link_text('重置').click()

    def money_rule(self):
        """计费规则管理：查询，新增"""
        driver = self.driver
        driver.find_element_by_link_text('舱单管理').click()
        driver.find_element_by_link_text('计费规则管理').click()
        js = 'document.getElementById("from").value = "2019-07-30"'
        driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        self.el_show('xpath', '//*[@id="rulesTable"]/tbody/tr[1]/td[6]', '查询数据加载')
        self.el_show('text', '新增', '新增点击加载')
        driver.find_element_by_link_text('新增').click()
        time.sleep(2)
        num = random.randint(10)
        money = random.randint(100)
        self.el_show('xpath', '//*[@id="chargeRulesForm"]/div[1]/div/div/div/div[1]/div/div/select', '数据来源选择框加载')
        self.select('xpath', '//*[@id="chargeRulesForm"]/div[1]/div/div/div/div[1]/div/div/select', 'index', num)
        self.el_show('xpath', '//*[@id="senderCode"]', '发送方代码加载')
        self.input_data('xpath', '//*[@id="senderCode"]', '123456789: 管理员账号(201909111)')
        self.input_data('xpath', '//*[@id="chargeRulesForm"]/div[1]/div/div/div/div[3]/div/div/input', '2019-10-31')
        self.input_data('xpath', '//*[@id="chargeRulesForm"]/div[1]/div/div/div/div[4]/div/div/input', money)
        self.el_show('text', '确定', '确定点击加载')
        time.sleep(2)
        driver.find_element_by_link_text('确定').click()

    def edi_history(self):
        """ EDI解析记录：查询，解析问价名称下载，重置"""
        driver = self.driver
        driver.find_element_by_link_text('舱单管理').click()
        driver.find_element_by_link_text('EDI解析记录').click()
        js = 'document.getElementById("from").value = "2019-08-30"'
        driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a', '查询数据加载')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a').click()
        time.sleep(2)
        driver.find_element_by_link_text('重置').click()

    def user_admin(self):
        """用户管理：查询，余额（用户费用明细），预配舱单，提单确认，口岸服务，港区服务，查验服务，新增，新增二级代发账号，重置"""
        driver = self.driver
        driver.find_element_by_link_text('舱单管理').click()
        driver.find_element_by_link_text('用户管理').click()
        self.el_show('text', '查询', '查询点击加载')
        driver.find_element_by_link_text('查询').click()
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]', '查询数据加载')
        el = driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]')
        el = el.text
        if el == '-NA-':
            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[9]/a', '预备舱单加载')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[9]/a').click()

            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[10]/a', '提单确认加载')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[10]/a').click()

            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[111]/a', '口岸服务加载')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[11]/a').click()

            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a', '港区服务加载')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a').click()

            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a', '查验服务加载')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a').click()
        else:
            pass
