# coding:utf-8
import os
import random
import re

import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from unittest import TestCase
import unittest
from selenium.webdriver.common.by import By

from common_data import common_value


class Commonshare():

    def __init__(self, driver):
        """初始化方法,创建浏览器对象"""
        self.driver = driver

    def rm_imput(self, locate_type, value):
        """清空指定元素输入框中内容"""
        el = self.locateElement(locate_type, value)
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.BACKSPACE)

    def locateElement(self, locate_type, value):
        """判断定位方式并调用相关方法"""
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        # 如果el不为None,则返回
        if el is not None:
            return el

    def click(self, locate_type, value):
        """指定对某一元素的点击操作"""
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()
        time.sleep(1)

    def input_data(self, locate_type, value, data):
        """ # 对指定的元素进行数据输入"""
        el = self.locateElement(locate_type, value)
        # 执行输入操作
        el.send_keys(data)

    def get_text(self, locate_type, value):
        """获取指定元素的文本内容"""
        el = self.locateElement(locate_type, value)
        return el.text

    def get_attr(self, locate_type, value, data):
        """ 获取指定元素的属性值"""
        el = self.locateElement(locate_type, value)
        return el.get_attribute(data)

    def compare_el(self, locate_type, value, data_value, ex):
        """断言：
                查看指定元素的文本属性值是否与给定参数值匹配
            locate_type：定位方式
            value: 定位表达式
            data_value: 匹配值
            ex：标题
            :return  i
        """
        data_get = Commonshare.get_text(self, locate_type, value)
        print(data_get)

        if data_value in data_get:
            print('%s ok' % ex)
        else:
            print('%s error' % ex)
            i = 0
            return i

    def el_show(self, locate_type, value, ex):
        """判断指定的元素是否加载成功"""
        el = None
        if locate_type == 'id':
            el = (By.ID, value)
        elif locate_type == 'name':
            el = (By.NAME, value)
        elif locate_type == 'css':
            el = (By.CSS_SELECTOR, value)
        elif locate_type == 'text':
            el = (By.LINK_TEXT, value)
        elif locate_type == 'xpath':
            el = (By.XPATH, value)
        elif locate_type == 'class':
            el = (By.CLASS_NAME, value)
        elif locate_type == 'partial link text':
            el = (By.PARTIAL_LINK_TEXT, value)
        elif locate_type == 'tag':
            el = (By.TAG_NAME, value)

        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(el))
            print('%s:ok' % ex)
        except Exception as e:
            print('error_错误：%s' % ex)

    def get_length(self, locate_type, value, ex):
        """断言：
                判断查询结果是否有值：选定元素 value 值的长度不为0则判断有值"""
        text = Commonshare.get_text(self, locate_type, value)
        print(text)
        num = len(text)
        if 0 != num:
            print('%s ok' % ex)
        else:
            print('%s error' % ex)
            i = 0
            return i

    def mouse_move(self, locate_type, value):
        """鼠标悬停到到指定元素
         locate_type：定位方式
        value: 定位表达式
        """
        target = self.locateElement(locate_type, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def keyboard(self):
        """键盘操作"""
        pass

    def select(self, locate_type, value, select_type, select_value):
        """下拉框选择
        locate_type：定位方式
        value: 定位表达式
        select_type: 选择下拉框定位类型
        select_value: 下拉框定位值
        """
        el = self.locateElement(locate_type, value)
        select = Select(el)
        if select_type == 'index':
            select.select_by_index(select_value)
        elif select_type == 'text':
            select.select_by_visible_text(select_value)
        elif select_type == 'value':
            select.select_by_value(select_value)
        time.sleep(1)

    def time_select(self, value, date):
        """选择时间
        value : 元素id值
        date 格式：2019-10-30"""
        js = 'document.getElementById(value).value = data'
        self.driver.execute_script(js)

    def addAttribute(self, elementobj, attributeName, value):

        self.driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)


def loginData():
    """data : 用户名，密码"""
    data = {
        "username": "customer1",
        "password": "123456"}
    return data


def login():
    """返回登陆cookies"""
    r = requests.post(
        url='http://192.168.17.50:2090/home/control/login',
        data=loginData(),
        headers={'Content-Type': 'application/json'})
    return r.cookies


def upload(url, file, data):
    """导入文件接口测试"""
    cookies = login()
    headers = {"Content_type": "multipart/form-data"}
    r = requests.post(url=url, params=data, headers=headers, cookies=cookies, files=file)
    code = r.status_code
    print(code)
    assert (200 == code)


if __name__ == '__main__':
    pass

