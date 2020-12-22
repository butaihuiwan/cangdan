# import datetime
# import os
#
# import filePath as filePath
# import requests
# from idna import unicode
#
# from common_data import common_value
# from other.Commonlib import upload, login


# url = "http://192.168.17.50:4528/uploadDepositSlip"
# file = {"file": open(common_value.SHUIDAN, "rb")}
#
# data = {"userLoginId": "customer1",
#         "abnormalUser": "false",
#         "inputer": "",
#         "depositAmount": "1111",
#         "depositDate": "2019-12-04",
#         "depositor": "1111",
#         "depositType": "0",
#         "uploadImg": file}
# upload(url, file, data)
# def upload1():
#     """导入文件接口测试"""
#
#     cookies = login()
#     url = "http://192.168.17.50:4528/uploadDepositSlip"
#     file = {"file": open(common_value.SHUIDAN, "rb")}
#     data = {"userLoginId": "customer1",
#             "abnormalUser": "false",
#             "inputer": "",
#             "depositAmount": "1111",
#             "depositDate": "2019-12-09",
#             "depositor": "1111",
#             "depositType": "0",
#             "uploadImg": file,
#             "filename": "水单图片.jpg"}
#
#     headers = {"Content_type": "multipart/form-data"}
#     r = requests.post(url=url, params=data, headers=headers, cookies=cookies, files=file)
#     code = r.status_code
#     print(code)
#     assert (200 == code)

# url = 'http://192.168.17.50:4528/excelimport/billnodeinfo'
# file = {"file": open(common_value.SUBFILE, "rb")}
# data = {
#     "file": file,
#     "userLoginId": "customer1"
# }
# upload(url=url, file=file, data=data)
# nowTime = datetime.datetime.now().strftime('%m%d%H%M')
# print(nowTime)
# print(type(datetime.datetime.now().strftime('%Y-%m-%d')))
# data = datetime.datetime.now().strftime('%Y-%m-%d')
# path = '../report/' + data
# if os.path.exists(path):
#     print(00)
#
# else:
#     os.mkdir(path)
# def test(func):
#     print("1")
#
#     def test1(*args, **kwargs):
#         print('2')
#         func(*args, **kwargs)
#
#     return test1
#
#
# def test01(func):
#     print('3')
#
#     def test02(*args, **kwargs):
#         print('4')
#         func(*args, **kwargs)
#
#     return test02
#
#
# @test01
# @test
# def func(*args, **kwargs):
#     print("jj")

#
# func("5", "6")
import os
#
# path = os.listdir(r'C:\Users\TP\PycharmProjects\cangdan-test\download_data')[0]
# print(type(path))
# path = 'C:\\Users\\TP\PycharmProjects\\cangdan-test\\download_data' + "\\" + path
# print(path)
# # print(path)
# f = open(path, 'r')
# a = f.read()
# b = a.split('\n')
# name = b[0].split(":")[5]
# type = b[2].split(':')[1]
# print('输出船代名称:', name, '提单类型:', type)
#
# if name == '132210843' and type == 'ORI':
#     print('ok')
# else:
#     print('error')

from other import rm_image

# path = rm_image.find_filename(r'C:\Users\TP\PycharmProjects\cangdan-test\download_data', '.txt')
# print(path)
# path = '../' + path
# # print(path)
import os
fileList = os.listdir(r'D:\ceshi\代码\cangdan-test\other')
emailreport_path = fileList[0]





