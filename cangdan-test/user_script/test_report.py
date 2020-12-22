# encoding:utf-8
import os
import random
import time
from selenium.webdriver import ActionChains
from common_data import common_value
from other import rm_image
from other.Commonlib import Commonshare, upload
from selenium.webdriver.common.keys import Keys
from other.other_script import Date_add_clear
import other.rm_image

# 预报舱单申报模块
class TestReport(Date_add_clear):
    """预报舱单申报模块"""

    def update_mm(self):
        """修改密码"""
        driver = self.driver
        el = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[3]/a')
        ActionChains(driver).move_to_element(el).perform()
        driver.find_element_by_link_text('更改密码').click()
        self.el_show('xpath', '//*[@id="currentPassword"]', '原密码输入框')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="currentPassword"]').send_keys('123456')
        time.sleep(1)
        self.el_show('id', 'newPassword', '新密码输入框')
        driver.find_element_by_id('newPassword').send_keys('123456')
        self.el_show('id', 'newPasswordVerify', '新密码再次输入框')
        driver.find_element_by_id('newPasswordVerify').send_keys('123456')
        driver.find_element_by_link_text('确定').click()
        time.sleep(1)
        # 判断是否加载出提示成功信息
        TestReport.compare_el(self, 'xpath', '/html/body/div[6]/div/div/div[1]/div', '成功', '修改密码')

    def logout(self):
        """注销， 注册"""
        driver = self.driver
        el = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[3]/a')
        ActionChains(driver).move_to_element(el).perform()
        self.el_show('text', '注销', '注销')
        driver.find_element_by_link_text('注销').click()

    # def regit(self):
    #     url = "http://192.168.17.50:2090/home/control/userRegister"
    #     file = {"file": open(common_value.SHUIDAN, "rb")}
    #     data = {
    #         "userLoginId": "xxx123897",
    #         "password": "123456",
    #         "repeatPassword": "123456",
    #         "contactPerson": "1",
    #         "phoneNumber": "12345678910",
    #         "company": "1",
    #         "companyAddress": "1",
    #         "email": "146@qq.com",
    #         "businessLicensePicture": file
    #     }
    #
    #     upload(url, file, data)

    def query(self):
        """待发送-查询"""
        self.driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        self.driver.execute_script(js)
        self.el_show('text', '查询', '查询点击加载')
        self.driver.find_element_by_link_text('查询').click()
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[10]/a[1]', '待发送-查询')

    def add_creat(self, TDH, CM, HC, index):
        """
        新增--待发送 > 创建
               :param TDH: 提单号
            :param CM: 船名
               :param HC: 航次
               :return:
               """
        self.driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(1)
        # 选择发送人代码
        self.add_data(TDH, CM, HC, index)
        # 判断创建成功点击确定按钮是否加载出来
        self.exist_code()

    def seed(self, TDH, CM, HC, index):
        """
        新增--待发送 > 发送
        :param TDH: 提单号
     :param CM: 船名
        :param HC: 航次
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(1)
        self.add_data(TDH, CM, HC, index)
        self.add_data_box()
        self.send_code()

    def rm_wait_seed(self):
        """删除--待发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"待发送").click()
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

    def update_wait_seed(self, TDH, CM, HC):
        """修改 ：暂存-- 待发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'修改')])[1]").click()
        num = str(random.randint(1, 1000))
        self.el_show('xpath', '//input[@name="FREIGHT_NBR"]', '运编号')
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@name="FREIGHT_NBR"]').send_keys(num)
        self.el_show('text', '暂存', '暂存点击加载')
        driver.find_element_by_link_text("暂存").send_keys(Keys.ENTER)
        # 判断是否提示成功
        self.el_show('xpath', '//*[@id="toast-container"]/div/div[2]', '暂存提示成功加载')
        TestReport.compare_el(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '成功',
                              '待发送-修改-暂存')

    def update_wait_exist(self, TDH, CM, HC, index):
        """修改 ：发送，-- 待发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'修改')])[1]").click()
        self.data_clear(TDH, CM, HC)
        self.add_data(TDH, CM, HC, index)
        self.data_clear_box()
        self.add_data_box()
        self.send_code()

    def excel_history(self):
        """Excel历史查看--待发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"Excel历史").click()
        time.sleep(2)
        driver.find_element_by_id("buttonCancelEditExcel").click()

    # def import_excel(self):
    #     """舱单模板表格导入"""
    #     url = "http://192.168.17.50:4528/excelimport/update/excelFullImport"
    #     file = {"file": open(common_value.EXC_IMPORT, "rb")}
    #     data = {"file": file, "userLoginId": "customer1",
    #             "CID": "100002",
    #             "TYPE": "3"}
    #     upload(url=url,
    #            file=file,
    #            data=data)

    def seed_more(self):
        """批量发送-待发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        self.rm_imput('xpath', '//*[@id="from"]')
        driver.find_element_by_xpath('//*[@id="from"]').send_keys('2019-8-30')
        self.el_show('text', '查询', '查询点击加载')
        self.driver.find_element_by_link_text('查询').click()
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/thead/tr/th[1]/div/span/input').click()
        driver.find_element_by_link_text(u"批量发送").click()
        time.sleep(2)

    def update_seed(self):
        """修改--已发送  （暂存，重新发送）"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"修改").click()
        num = str(random.randint(1, 1000))
        self.el_show('xpath', '//input[@name="FREIGHT_NBR"]', '运编号')
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@name="FREIGHT_NBR"]').send_keys(num)
        self.el_show('text', '暂存', '暂存点击加载')
        driver.find_element_by_link_text(u"暂存").click()
        TestReport.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '已发送-修改：暂存')
        self.el_show('text', '更改报文发送', '更改报文发送点击加载')
        driver.find_element_by_link_text(u"更改报文发送").send_keys(Keys.ENTER)
        self.el_show('css', 'button.btn.btn-primary', '更改报文发送确认点击加载')
        time.sleep(5)
        driver.find_element_by_css_selector("button.btn.btn-primary").send_keys(Keys.ENTER)
        self.el_show('xpath', "//i[@onclick='returnQuery()']", '更改报文发送确认点击加载')
        # time.sleep(2)
        # # driver.find_element_by_xpath("//i[@onclick='returnQuery()']").click()

    def report_history(self):
        """报文历史查看--已发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="content-main-section"]/div[3]/div/div/div/div/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"报文历史").click()
        time.sleep(2)
        # driver.find_element_by_id("buttonCancelEditEdi").click()

    def excel_history_seed(self):
        """excel历史查看--已发送"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"Excel历史").click()
        time.sleep(2)
        # driver.find_element_by_id("buttonCancelEditExcel").click()

    def copy_add01(self, TDH, CM, HC):
        """
        复制新增--> 暂存
        TDH = 提单号； CM = 船名；   HC = 航次
        :return:
        """
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"复制新增").click()
        time.sleep(1)
        driver.find_element_by_id("BILL_NBR").clear()
        driver.find_element_by_id("E_SHIP_NAM").clear()
        driver.find_element_by_id("OUT_VOYAGE_NO").clear()
        driver.find_element_by_id('BILL_NBR').send_keys(TDH)
        driver.find_element_by_id('E_SHIP_NAM').send_keys(CM)
        driver.find_element_by_id('OUT_VOYAGE_NO').send_keys(HC)
        self.exist_code()

    def copy_add02(self, TDH, CM, HC):
        """
        复制新增--已发送 > 发送
        TDH = 提单号； CM = 船名；   HC = 航次
        :return:
        """
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"复制新增").click()
        time.sleep(1)
        driver.find_element_by_id('BILL_NBR').send_keys(TDH)
        driver.find_element_by_id('E_SHIP_NAM').send_keys(CM)
        driver.find_element_by_id('OUT_VOYAGE_NO').send_keys(HC)
        self.add_data_box()
        self.send_code()

    def select_seed(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_xpath(
            '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div/div/div/div/div[3]/div/a[2]').click()
        driver.find_element_by_link_text('已发送清单导出').click()

    # def import_edi(self):
    #     """导入舱单报文模板文件"""
    #     url = "http://192.168.17.50:4528/ediAnalyze/shipbilledi"
    #     file = {"file": open(common_value.CANGDANFILE, "rb")}
    #     data = {
    #         "upfile": file,
    #         "ACCOUNTNAME": "customer1",
    #         "enctype": "multipart/form-data"
    #     }
    #     upload(url=url, file=file, data=data)

    def record_edi(self):
        """# EDI解析记录"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text('EDI解析记录').click()
        js = 'document.getElementById("from").value = "2019-08-06"'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_link_text('查询').click()
        # 判断查询结果是否成功
        i = self.get_length('xpath', '//*[@id="purchaseOrdersearchTable"]/thead/tr/th[6]', 'EDI解析记录查询')
        assert_list.append(i)
        driver.find_element_by_link_text('重置').click()
        time.sleep(2)
        if 0 in assert_list:
            assert (1 == 2)

    def manifest_management(self):
        """ 代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text('代发舱单管理').click()
        driver.find_element_by_link_text('待处理').click()
        js = 'document.getElementById("from").value = "2018-08-06"'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_link_text('查询').click()
        el = self.get_text('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr/td')
        if el == 'No data available in table':
            i = None
            assert_list.append(i)
        else:
            i = self.get_length('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[5]', '代发舱单管理查询')
            assert_list.append(i)
            # 查看
            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[1]', '查看')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[1]').click()
            self.el_show('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]', 'xx')
            time.sleep(2)
            i = self.get_length('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]', '代发舱单管理查看')
            assert_list.append(i)
            time.sleep(2)

            driver.find_element_by_css_selector('#close > .fa').click()

            # 报文历史
            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[2]', '报文历史')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[2]').click()
            self.el_show('text', '取消', '取消点击')
            driver.find_element_by_link_text('取消').click()
            time.sleep(2)

            # 已处理
            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[3]', '报文历史')
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[3]').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]').click()
            # 撤回
            self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[4]', '撤回')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[4]').click()
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="message"]').send_keys('111')
            self.el_show('text', '确认', '确认点击')
            driver.find_element_by_link_text('确认').click()
        if 0 in assert_list:
            assert (1 == 2)

    def manifest_management01(self):
        """代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息"""
        driver = self.driver
        assert_list = []
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text('代发舱单管理').click()
        driver.find_element_by_link_text('已处理').click()
        js = 'document.getElementById("from").value = "2018-8-06"'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_link_text('查询').click()
        i = self.get_length('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[5]', '代发舱单管理查询')
        assert_list.append(i)
        # 查看
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a[1]').click()
        self.el_show('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]', 'xx')
        time.sleep(2)
        i = self.get_length('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]', '代发舱单管理查看')
        assert_list.append(i)
        time.sleep(2)
        driver.find_element_by_css_selector('#close > .fa').click()

        # 报文历史
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a[2]', '报文历史')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a[2]').click()
        time.sleep(2)
        # self.el_show('text', '取消', '取消点击')
        # driver.find_element_by_link_text('取消').click()
        if 0 in assert_list:
            assert (1 == 2)

    def down_db(self):
        """港口代码参照表下载，舱单模板下载"""
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_link_text('舱单模板下载').click()
        time.sleep(10)
        if os.path.exists(r"../download_data/新舱单导入模板.xlsx"):
            print('舱单模板下载 ok')
        else:
            print('舱单模板下载 error')
        driver.find_element_by_link_text('港口代码参照表').click()
        time.sleep(10)
        if os.path.exists(r"../download_data/5位海关可发港口.xlsx"):
            print('港口代码参照表下载 ok')
        else:
            print('港口代码参照表下载 error')
        try:
            rm_image.del_dir('../download_data')
        except Exception as e:
            print("删除模板文件", e)

    def fix_type_one(self,index):
        """判断船代类型,修改提单类型;
        中外运上传edi报文,提单类型TER修改为ORI"""
        rm_image.del_files(r'../download_data', '.txt')
        num = str(random.randint(1, 1000))
        num1 = str(random.randint(1, 1000))
        TDH = 'ex' + num + num1
        print(TDH)
        self.seed(TDH, num, num, index)
        driver = self.driver
        time.sleep(3)
        driver.back()
        driver.refresh()
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="main-navigation"]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="content-main-section"]/div[3]/div/div/div/div/ul/li[2]/a').click()
        self.input_data('xpath', '//*[@id="form"]/div/div[3]/div[1]/input', TDH)
        self.click('xpath',
                   '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div/div/div/div/div[3]/div/a[1]')
        driver.find_element_by_link_text(u"报文历史").click()
        print('报文历史ok')
        time.sleep(2)
        self.click('css', '#purchaseOrdersearchTable > tbody > tr > td:nth-child(5) > a:nth-child(2)')
        time.sleep(5)
        print('报文历史下载ok')
        """判断"""
        path = rm_image.find_filename(common_value.download_data, '.txt')
        print(path)
        path = '../download_data/' + path
        with open(path, 'r') as f:
            a = f.read()
            b = a.split('\n')
            name = b[0].split(":")[5]
            type = b[2].split(':')[1]
            print('输出船代名称:', name, '提单类型:', type)

            if name == '132210843' and type == 'ORI':
                print('ok')
            elif name != '132210843' and type == 'TER':
                print('ok')
            else:
                print('error')

    def fix_type_other(self):
        """判断船代类型,
             不是中外运上传edi报文,提单类型为TER"""
        self.fix_type_one(1)



