import os
import random
import time
from common_data import common_value
from other.BeautifulReport import BeautifulReport
from user_script.test_report import TestReport
import unittest
from selenium import webdriver


class TestcaseReport(unittest.TestCase):
    """预报舱单申报模块"""

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file(
            common_value.IMAGE + "%s.png" % img_name)

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
        # driver.maximize_window()
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()

    def tearDown(self) -> None:
        self.driver.quit()
        time.sleep(1)
        print('bye')

    @BeautifulReport.add_test_img('更改密码')
    def test_1000(self):
        """更改密码"""

        log = TestReport(self.driver)
        log.update_mm()
        self.save_img('更改密码')

    @BeautifulReport.add_test_img('待发送-查询')
    def test_0001(self):
        """待发送--查询"""
        log = TestReport(self.driver)
        log.query()
        time.sleep(2)
        self.save_img('待发送-查询')

    @BeautifulReport.add_test_img('待发送-新增-创建-暂存')
    def test_0002(self):
        """ 待发送-- 新增 > 创建 > 暂存"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 10000))
        TDH = 'ex' + num
        add.add_creat(TDH, num, num, 1)
        self.save_img('待发送-新增-创建-暂存')

    @BeautifulReport.add_test_img('待发送-新增-发送')
    def test_0004(self):
        """待发送-- 新增 > 发送"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        num1 = str(random.randint(1, 1000))
        TDH = 'ex' + num + num1
        add.seed(TDH, num, num, 1)
        self.save_img('待发送-新增-发送')

    # # @BeautifulReport.add_test_img('待发送--导入')
    # def test_0005(self):
    #     """舱单模板表格导入"""
    #     im = TestReport(self.driver)
    #     im.import_excel()
    #     # self.save_img('待发送--导入')

    @BeautifulReport.add_test_img('待发送--批量发送')
    def test_0006(self):
        """待发送--批量发送"""
        se = TestReport(self.driver)
        se.seed_more()
        self.save_img('待发送--批量发送')

    @BeautifulReport.add_test_img('待发送-修改-暂存')
    def test_0007(self):
        """待发送-- 修改-暂存"""
        num = str(random.randint(1, 1000))
        TDH = 'ex' + num
        TestReport(self.driver).update_wait_seed(TDH, num, num)
        self.save_img('待发送-修改-暂存')

    @BeautifulReport.add_test_img('待发送-修改-发送')
    def test_0003(self):
        """待发送-- 修改-发送"""
        num = str(random.randint(1, 1000))
        TDH = 'ex' + num
        TestReport(self.driver).update_wait_exist(TDH, num, num, 1)
        self.save_img('待发送-修改-发送')

    @BeautifulReport.add_test_img('待发送--excel查看')
    def test_0008(self):
        """待发送-- excel查看"""
        excel = TestReport(self.driver)
        excel.excel_history()
        self.save_img('待发送--excel查看')

    @BeautifulReport.add_test_img('待发送--删除')
    def test_0009(self):
        """待发送--删除"""
        rm = TestReport(self.driver)
        rm.rm_wait_seed()
        self.save_img('待发送--删除')

    @BeautifulReport.add_test_img('已发送--查询')
    def test_0010(self):
        """已发送--查询"""
        se = TestReport(self.driver)
        se.select_seed()
        self.save_img('已发送--查询')

    @BeautifulReport.add_test_img('暂存，更改报文重新发送')
    def test_0013(self):
        """已发送--修改-暂存，更改报文重新发送"""
        update = TestReport(self.driver)
        update.update_seed()
        self.save_img('暂存，更改报文重新发送')

    @BeautifulReport.add_test_img('复制新增-创建-暂存')
    def test_0014(self):
        """已发送--复制新增 > 暂存"""
        log = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        TDH = 'TEST' + num
        log.copy_add01(TDH, num, num)
        self.save_img('复制新增-创建-暂存')

    @BeautifulReport.add_test_img('已发送-复制新增-发送')
    def test_0016(self):
        """已发送--复制新增 > 发送"""
        num = str(random.randint(1, 1000))
        TDH = 'TEST' + num
        TestReport(self.driver).copy_add02(TDH, num, num)
        self.save_img('已发送-复制新增-发送')

    @BeautifulReport.add_test_img('已发送--excel 查看')
    def test_0017(self):
        """已发送--excel 查看"""
        ex = TestReport(self.driver)
        ex.excel_history_seed()
        self.save_img('已发送--excel 查看')

    @BeautifulReport.add_test_img('已发送--报文历史查看')
    def test_0018(self):
        """已发送--报文历史查看"""
        re = TestReport(self.driver)
        re.report_history()
        self.save_img('已发送--报文历史查看')

    # # @BeautifulReport.add_test_img('导入EDI舱单报文')
    # def test_0019(self):
    #     """接口测试导入EDI舱单报文"""
    #     log = TestReport(self.driver)
    #     log.import_edi()
    #     # self.save_img('导入EDI舱单报文')

    @BeautifulReport.add_test_img('EDI解析记录')
    def test_0020(self):
        """EDI解析记录"""
        log = TestReport(self.driver)
        log.record_edi()
        self.save_img('EDI解析记录')

    @BeautifulReport.add_test_img('代发舱单管理--待处理')
    def test_0021(self):
        """代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回"""
        log = TestReport(self.driver)
        log.manifest_management()
        self.save_img('代发舱单管理--待处理')

    @BeautifulReport.add_test_img('代发舱单管理--已处理')
    def test_0022(self):
        """代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息"""
        log = TestReport(self.driver)
        log.manifest_management01()
        self.save_img('代发舱单管理--已处理')

    @BeautifulReport.add_test_img('舱单模板下载')
    def test_0023(self):
        """港口代码参照表下载，舱单模板下载"""
        log = TestReport(self.driver)
        log.down_db()
        self.save_img('舱单模板下载')

    def test_0024(self):
        """判断船代类型,修改提单类型;
       中外运上传edi报文,提单类型TER修改为ORI"""

        log = TestReport(self.driver)
        log.fix_type_one(6)

    def test_0025(self):
        """判断船代类型,
      不是中外运上传edi报文,提单类型为TER"""
        log = TestReport(self.driver)
        log.fix_type_other()


if __name__ == '__main__':
    unittest.main()
