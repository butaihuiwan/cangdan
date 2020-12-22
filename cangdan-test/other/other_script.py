import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .Commonlib import Commonshare


class Date_add_clear(Commonshare):
    """舱单数据操作"""

    def data_clear(self, TDH, CM, HC):
        """修改清空舱单数据"""
        # 选择发送人代码
        driver = self.driver
        self.select('id', 'BILL_SENDER_CODE', 'index', 1)
        time.sleep(1)
        # 选择接受人代码
        self.select('id', 'BILL_RECEIVER_CODE', 'index', 1)
        # 订舱信息
        try:
            driver.find_element_by_id('BILL_NBR').clear()

            driver.find_element_by_id('E_SHIP_NAM').clear()

            driver.find_element_by_id('OUT_VOYAGE_NO').clear()

            self.rm_imput('id', 'TRUST_INFO')

            driver.find_element_by_name('FREIGHT_NBR').clear()

            driver.find_element_by_name('BILL_ORIG_NUM').clear()

            driver.find_element_by_name('MASTER_NO').clear()
        except Exception as e:
            print('订舱信息加载失败', e)

        # 发货人信息
        try:
            driver.find_element_by_id('SHIPPER_COD').clear()

            driver.find_element_by_id('E_SHIPPER_NAM').clear()

            time.sleep(1)

            self.rm_imput('id', 'SHIPPER_COUNTRY_COD')

            driver.find_element_by_id('SHIPPER_ADD_STR').clear()

            driver.find_element_by_id('SHIPPER_TE_STR').clear()

            driver.find_element_by_id('SHIPPER_EM_STR').clear()

            driver.find_element_by_id('SHIPPER_FX_STR').clear()
        except Exception as e:
            print('发货人信息加载失败', e)

        # 收货人信息
        try:
            driver.find_element_by_id('CONSIGNEE_COD').clear()

            driver.find_element_by_id('E_CONSIGNEE_NAM').clear()

            self.rm_imput('id', 'CONSIGNEE_COUNTRY_COD')

            self.rm_imput('name', 'CONSIGNEE_ADD_STR')

            driver.find_element_by_id('CONSIGNEE_TE_STR').clear()

            driver.find_element_by_id('CONSIGNEE_EM_STR').clear()

            driver.find_element_by_id('SHIPPER_FX_STR').clear()

            driver.find_element_by_id('CONSIGNEE_CONTACT_NAM').clear()

            self.rm_imput('id', 'CONSIGNEE_CONTACT_TE_STR')

            driver.find_element_by_id('CONSIGNEE_CONTACT_EM_STR').clear()

            driver.find_element_by_id('CONSIGNEE_CONTACT_FX_STR').clear()

            self.rm_imput('name', 'CONSIGNEE_AEO')
        except Exception as e:
            print('收货人信息加载失败', e)

            # 通知人信息
        try:
            driver.find_element_by_id('NOTIFY_COD').clear()

            driver.find_element_by_id('E_NOTIFY_NAM').clear()

            self.rm_imput('id', 'NOTIFY_COUNTRY_COD')
            self.rm_imput('name', 'NOTIFY_ADD_STR')
            driver.find_element_by_id('NOTIFY_TE_STR').clear()

            driver.find_element_by_id('NOTIFY_EM_STR').clear()

            driver.find_element_by_id('NOTIFY_FX_STR').clear()
        except Exception as e:
            print('通知人信息加载失败', e)

        # 地点信息
        try:
            self.rm_imput('name', 'START_PORT_NAM')

            self.rm_imput('name', 'LOAD_PORT_FULLNAM')

            self.rm_imput('name', 'DISCHRG_PORT_FULLNAM')

            self.rm_imput('name', 'TRANS_PORT_FULLNAM')

            self.rm_imput('name', 'DEST_PORT_FULLNAM')
        except Exception as e:
            print('地点信息加载失败', e)

    def data_clear_box(self):
        """清除箱号，货物信息数据"""
        driver = self.driver
        try:
            while True:
                self.el_show('xpath', '//*[@id="tbody-info"]/tr/td[7]/a[2]', '货物信息删除点击加载')
                driver.find_element_by_xpath('//*[@id="tbody-info"]/tr/td[7]/a[2]').click()
                driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button[2]').click()
                driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button').click()
                time.sleep(2)
        except Exception as e:
            print('货物信息删除pass')
            time.sleep(2)
        try:
            while True:
                self.el_show('xpath', '//*[@id="tbody-info"]/tr/td[8]/a[2]', '箱号信息删除点击加载')
                time.sleep(2)
                driver.find_element_by_xpath(
                    '//*[@id="tbody-info"]/tr/td[8]/a[2]').click()
                self.el_show('xpath', '/html/body/div[8]/div/div/div[2]/button[2]', '箱号信息删除确认1点击加载')
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button[2]').send_keys(Keys.ENTER)
                self.el_show('xpath', '/html/body/div[10]/div/div/div[2]/button', '箱号信息删除确认2点击加载')
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button').click()
                time.sleep(2)
        except Exception as e:
            print('箱号删除pass')
        time.sleep(1)
        target = driver.find_element_by_xpath(
            '//*[@id="text-body"]/div[2]/div[1]/a')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 鼠标拖动到可见的元素去
        time.sleep(2)
        """清空舱单箱子，货物信息"""

        """清空舱单总件毛体数据"""
        try:
            self.el_show('xpath', '//*[@id="PIECE_NUM"]', '总件数')
            self.rm_imput('xpath', '//*[@id="PIECE_NUM"]')

            self.el_show('xpath', '//*[@id="GWEIGHT_TON"]', '总体积')
            self.rm_imput('xpath', '//*[@id="GWEIGHT_TON"]')
            time.sleep(2)
            self.el_show('xpath', '//*[@id="GVOL_NUM"]', '总毛重')
            self.rm_imput('xpath', '//*[@id="GVOL_NUM"]')
        except Exception as e:
            print('总件毛体点击加载失败', e)

    def add_data(self, TDH, CM, HC, index):
        """新增填写舱单的数据"""
        driver = self.driver
        # 选择发送人代码
        self.select('id', 'BILL_SENDER_CODE', 'index', 1)
        time.sleep(1)
        # 选择接受人代码
        self.select('id', 'BILL_RECEIVER_CODE', 'index', index)
        time.sleep(2)
        # 订舱信息
        try:
            driver.find_element_by_id('BILL_NBR').send_keys(TDH)
            driver.find_element_by_id('E_SHIP_NAM').send_keys(CM)
            driver.find_element_by_id('OUT_VOYAGE_NO').send_keys(HC)
            driver.find_element_by_id('TRUST_INFO').send_keys('YML：阳明')
            self.select('id', 'TYPE_OF_BILL', 'text', '电放')
            self.select('id', 'PAY_WAY_ID', 'text', '到付')
            driver.find_element_by_name('FREIGHT_NBR').send_keys('TEST20191022')
            self.select('id', 'DR_TYPE_STR', 'text', 'CY-FOR')
            driver.find_element_by_name('BILL_ORIG_NUM').send_keys('1')
            driver.find_element_by_name('MASTER_NO').send_keys('TEST20191022')
            time.sleep(2)
        except Exception as e:
            print('订舱信息加载失败', e)

        # 发货人信息
        try:
            driver.find_element_by_id('SHIPPER_COD').send_keys('USCI+91320412MA1MGBN10R')
            driver.find_element_by_id('E_SHIPPER_NAM').send_keys('CHANGZHOU JIANKAI WOOD CO.,LTD')
            driver.find_element_by_id('SHIPPER_COUNTRY_COD').send_keys('CN')
            driver.find_element_by_id('SHIPPER_ADD_STR').send_keys(
                'NO.89,WEIFU ROAD,CUIQIAO,HENGLIN TOWN,WUJIN DISTRICT,CHANGZHOU CITY,JI')
            driver.find_element_by_id('SHIPPER_TE_STR').send_keys('0519-85189799')
            driver.find_element_by_id('SHIPPER_EM_STR').send_keys('1234567789@qq.com')
            driver.find_element_by_id('SHIPPER_FX_STR').send_keys('123456')
            driver.find_element_by_name('CONSIGNEE_AEO').send_keys('SH')
        except Exception as e:
            print('发货人信息加载失败', e)

        # 收货人信息
        try:
            driver.find_element_by_id('CONSIGNEE_COD').send_keys('CHAMBER OF COMMERCE NUMBER+198326691502')
            driver.find_element_by_id('E_CONSIGNEE_NAM').send_keys('TOUCH EXPERTS GENERAL TRADING CO.,LTD')
            driver.find_element_by_id('CONSIGNEE_COUNTRY_COD').send_keys('IQ')
            driver.find_element_by_name('CONSIGNEE_ADD_STR').send_keys('IRAQ BAGHDAD VICTORY SQUAE')
            driver.find_element_by_id('CONSIGNEE_TE_STR').send_keys('123456789')
            driver.find_element_by_id('CONSIGNEE_EM_STR').send_keys('123456789@163.COM')
            driver.find_element_by_id('SHIPPER_FX_STR').send_keys('123456789')
            driver.find_element_by_id('CONSIGNEE_CONTACT_NAM').send_keys('BJ')
            driver.find_element_by_id('CONSIGNEE_CONTACT_EM_STR').send_keys('12345678@qq.com')
            driver.find_element_by_id('CONSIGNEE_CONTACT_FX_STR').send_keys('12345678')
        except Exception as e:
            print('收货人信息加载失败', e)

        # 通知人信息
        try:
            driver.find_element_by_id('NOTIFY_COD').send_keys('CHAMBER OF COMMERCE NUMBER+198326691502')
            driver.find_element_by_id('E_NOTIFY_NAM').send_keys('TOUCH EXPERTS GENERAL TRADING CO.,LTD')
            driver.find_element_by_id('NOTIFY_COUNTRY_COD').send_keys('IQ')
            driver.find_element_by_name('NOTIFY_ADD_STR').send_keys('IRAQ BAGHDAD VICTORY SQUAE')
            driver.find_element_by_id('NOTIFY_TE_STR').send_keys('123456')
            driver.find_element_by_id('NOTIFY_EM_STR').send_keys('123456@qq.com')
            driver.find_element_by_id('NOTIFY_FX_STR').send_keys('1132123')
        except Exception as e:
            print('通知人信息加载失败', e)

        # 地点信息
        try:
            driver.find_element_by_name('START_PORT_NAM').send_keys('ADA')
            driver.find_element_by_xpath(
                '//*[@id="formDtl"]/div[6]/table/tbody/tr[1]/td[2]/div[1]/span/div/div/div[1]').click()

            driver.find_element_by_name('LOAD_PORT_FULLNAM').send_keys('as')
            driver.find_element_by_xpath(
                '//*[@id="formDtl"]/div[6]/table/tbody/tr[1]/td[4]/div[1]/span/div/div/div[2]').click()
            driver.find_element_by_name('DISCHRG_PORT_FULLNAM').send_keys('BS')
            driver.find_element_by_xpath(
                '//*[@id="formDtl"]/div[6]/table/tbody/tr[2]/td[2]/div[1]/span/div/div/div[3]').click()
            driver.find_element_by_name('TRANS_PORT_FULLNAM').send_keys('CC')
            driver.find_element_by_xpath(
                '//*[@id="formDtl"]/div[6]/table/tbody/tr[2]/td[4]/div[1]/span/div/div/div').click()
            driver.find_element_by_name('DEST_PORT_FULLNAM').send_keys('ss')
            driver.find_element_by_xpath(
                '//*[@id="formDtl"]/div[6]/table/tbody/tr[3]/td[2]/div[1]/span/div/div/div').click()

            time.sleep(1)
            target = driver.find_element_by_xpath(
                '//*[@id="text-body"]/div[2]/div[1]/a')
            driver.execute_script("arguments[0].scrollIntoView();", target)  # 鼠标拖动到可见的元素去
        except Exception as e:
            print('地点信息加载失败', e)

    def add_data_box(self):
        """货物信息新增数据"""
        driver = self.driver
        try:
            self.el_show('css', '#text-body > div.body-div.portlet.light.bordered > div:nth-child(2) > a', '货物信息点击加载')
            time.sleep(2)
            driver.find_element_by_css_selector(
                '#text-body > div.body-div.portlet.light.bordered > div:nth-child(2) > a').click()
            time.sleep(2)
            self.el_show('css', 'div.col-md-8 > #PIECE_NUM', '货物信息件数输入框')
            driver.find_element_by_css_selector("div.col-md-8 > #PIECE_NUM").send_keys("220")
            time.sleep(2)
            self.el_show('css', 'div.col-md-8 > #GWEIGHT_TON', '货物信息体积输入框')
            driver.find_element_by_css_selector("div.col-md-8 > #GWEIGHT_TON").send_keys("220")

            time.sleep(2)
            driver.find_element_by_css_selector(
                "#inputCargoDtl > div > div.modal-body > div > div > div:nth-child(6) > div > div > input").send_keys(
                "220")
            self.el_show('xpath', "//form[@id='inputCargoDtl']/div/div/div/div/div[3]/div/div/span/input[2]", '货物信息')
            element = driver.find_element_by_xpath(
                "//form[@id='inputCargoDtl']/div/div/div/div/div[3]/div/div/span/input[2]")
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys('Rod/RD')
            driver.find_element_by_css_selector("div.col-md-8 > #GVOL_NUM").send_keys("220")
            driver.find_element_by_css_selector(
                '#inputCargoDtl > div > div.modal-body > div > div > div:nth-child(8) > div > div > textarea').send_keys(
                'WU')
            time.sleep(2)
            driver.find_element_by_id("buttonInputCargoDtl").click()
            self.el_show('xpath', '/html/body/div[8]/div/div/div[2]/button', '货物信息新增成功点击加载')
            driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/button").click()
        except Exception as e:
            print('货物信息新增加载失败', e)

        # 新增箱号集装箱细目
        try:
            self.el_show('xpath', '//*[@id="text-body"]/div[2]/div[2]/a', '箱号新增点击加载')
            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="text-body"]/div[2]/div[2]/a').click()
            self.el_show('css', '#inputCntrDtl > div:nth-child(1) > div > div > input', '箱号输入框加载')
            time.sleep(2)
            driver.find_element_by_css_selector('#inputCntrDtl > div:nth-child(1) > div > div > input').send_keys(
                "TEST1234568")  # 箱号
            self.el_show('xpath', '//*[@id="CNTR_SIZE_COD"]', '箱类型选择框加载')
            self.select('xpath', '//*[@id="CNTR_SIZE_COD"]', 'text', '20')
            self.select('xpath', '//*[@id="CNTR_TYPE_COD"]', 'text', 'GP')

            self.el_show('css', '#inputCntrDtl > div:nth-child(2) > div > div > input', '铅封号输入框加载')
            driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(2) > div > div > input").send_keys(
                "220")  # 铅封号

            self.el_show('css', '#inputCntrDtl > div:nth-child(4) > div > div > input', '件数输入框加载')
            driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(4) > div > div > input").send_keys(
                "220")  # 件数

            self.el_show('css', '#inputCntrDtl > div:nth-child(6) > div > div > input', '货内箱体积输入框加载')
            driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(6) > div > div > input").send_keys(
                "220")  # 货内箱体积

            self.el_show('css', '#inputCntrDtl > div:nth-child(5) > div > div > input', '货内货重输入框加载')
            driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(5) > div > div > input").send_keys(
                "220")  # 货内货重

            self.el_show('xpath', '//div[7]/div/div/select', '整箱输入框加载')
            Select(driver.find_element_by_xpath("//div[7]/div/div/select")).select_by_visible_text(u"整箱")

            self.el_show('id', 'SOC_ID', '货主箱输入框加载')
            Select(driver.find_element_by_id("SOC_ID")).select_by_visible_text(u"货主箱")

            time.sleep(2)
            # 点击保存新增箱号
            self.el_show('id', 'buttonInputCntrDtl', '点击保存新增箱号加载')
            driver.find_element_by_id("buttonInputCntrDtl").click()

            time.sleep(1)
            # 点击箱号新增操作成功
            self.el_show('xpath', '/html/body/div[10]/div/div/div[2]/button', '点击箱号新增操作成功加载')
            driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button').click()
        except Exception as e:
            print('新增箱号集装箱细目加载失败', e)

        #  总件毛体
        try:
            self.el_show('xpath', '//*[@id="PIECE_NUM"]', '总件数')
            driver.find_element_by_xpath(
                "//*[@id='PIECE_NUM']").send_keys('220')
            time.sleep(2)
            self.el_show('xpath', '//*[@id="GWEIGHT_TON"]', '总体积')

            driver.find_element_by_xpath(
                '//*[@id="GWEIGHT_TON"]').send_keys(
                '220')
            self.el_show('xpath', '//*[@id="GVOL_NUM"]', '总毛重')

            driver.find_element_by_xpath(
                '//*[@id="GVOL_NUM"]').send_keys(
                '220')
            time.sleep(3)
            # driver.find_element_by_xpath(
            #     '//*[@id="GWEIGHT_TON"]').click()
        except Exception as e:
            print('总件毛体点击加载失败', e)

        target = driver.find_element_by_xpath(
            '//*[@id="sendButton"]')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 鼠标下拉框向上移动

    def exist_code(self):
        """先创建后暂存点击"""
        self.el_show('text', '创建', '待发送新增-创建')
        self.driver.find_element_by_link_text('创建').click()
        self.el_show('xpath', '/html/body/div[8]/div/div/div[2]/button', '创建确认点击加载')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button').click()
        time.sleep(3)
        self.el_show('text', '暂存', '暂存点击加载')
        time.sleep(2)
        self.driver.find_element_by_link_text('暂存').send_keys(Keys.ENTER)
        self.el_show('xpath', '//*[@id="toast-container"]/div/div[2]', '暂存成功提示加载')
        i = self.compare_el('xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '待发送新增-暂存')
        assert_list = []
        assert_list.append(i)
        if 0 in assert_list:
            assert (1 == 2)

    def send_code(self):
        """发送点击"""
        self.el_show('xpath', '//*[@id="sendButton"]', '发送点击加载')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="sendButton"]').click()
        time.sleep(2)
        self.el_show('xpath', '/html/body/div[10]/div/div/div[2]/button[2]', '确认点击加载')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button[2]').click()
        self.el_show('xpath', '/html/body/div[10]/div/div/div[2]/button', '确认点击')
        self.click('xpath', '/html/body/div[10]/div/div/div[2]/button')
        time.sleep(3)
        # self.el_show('xpath', '/html/body/div[10]/div/div/div[1]/div', '待发送修改-发送')
