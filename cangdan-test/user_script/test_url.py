from common_data import common_value
from other.Commonlib import upload


class Test_url():
    def regit(self):
        """接口测试：注册"""
        url = "http://192.168.17.50:2090/home/control/userRegister"
        file = {"file": open(common_value.SHUIDAN, "rb")}
        data = {
            "userLoginId": "xxx123897",
            "password": "123456",
            "repeatPassword": "123456",
            "contactPerson": "1",
            "phoneNumber": "12345678910",
            "company": "1",
            "companyAddress": "1",
            "email": "146@qq.com",
            "businessLicensePicture": file
        }

        upload(url, file, data)

    def import_excel(self):
        """舱单模板表格导入"""
        url = "http://192.168.17.50:4528/excelimport/update/excelFullImport"
        file = {"file": open(common_value.EXC_IMPORT, "rb")}
        data = {"file": file, "userLoginId": "customer1",
                "CID": "100002",
                "TYPE": "3"}
        upload(url=url,
               file=file,
               data=data)

    def import_edi(self):
        """导入舱单报文模板文件"""
        url = "http://192.168.17.50:4528/ediAnalyze/shipbilledi"
        file = {"file": open(common_value.CANGDANFILE, "rb")}
        data = {
            "upfile": file,
            "ACCOUNTNAME": "customer1",
            "enctype": "multipart/form-data"
        }
        upload(url=url, file=file, data=data)

    def sub_im(self):
        """上传批量订阅模板文件"""
        url = 'http://192.168.17.50:4528/excelimport/billnodeinfo'
        file = {"file": open(common_value.SUBFILE, "rb")}
        data = {
            "file": file,
            "userLoginId": "customer1"
        }
        upload(url=url, file=file, data=data)
