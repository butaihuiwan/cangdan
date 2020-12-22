import os

PROJECT_DIRECTORY = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]  # 返回当前文件的项目目录
print(PROJECT_DIRECTORY)

if os.name == "nt":
    PATH = PROJECT_DIRECTORY + '\\venv\\Lib\\site-packages\\BeautifulReport\\template\\template'  # 返回template文件的绝对路径

    CHROMEDRIVER = PROJECT_DIRECTORY + "\\common_data\\chromedriver.exe"  # 指定chromedriver 绝对路径

    IMAGE = PROJECT_DIRECTORY + "\\suit\\img\\"  # 指定截图绝对路径

    AUEXE = PROJECT_DIRECTORY + "\\common_data\\au.exe"  # au.exe  上传文件执行程序文件

    CANGDANFILE = PROJECT_DIRECTORY + "\\common_data\\B单票多箱.txt"  # 导入EDI舱单报文 ,B单票多箱.txt（舱单报文）

    EXC_IMPORT = PROJECT_DIRECTORY + "\\common_data\\导入舱单测试模板文件.xlsx"  #

    SHUIDAN = PROJECT_DIRECTORY + "\\common_data\\水单图片.jpg"  # 上传水单图片

    DOWNLOAD_PATH = PROJECT_DIRECTORY + "\\download_data\\"  # 下载文件路径

    SUBFILE = PROJECT_DIRECTORY + "\\common_data\\批量订阅模板.xlsx"  # 上传批量订阅模板

    download_data = PROJECT_DIRECTORY + "\\download_data"  # 下载文件夹


else:
    PATH = PROJECT_DIRECTORY + '/venv/Lib/site-packages/BeautifulReport/template/template'

    CHROMEDRIVER = '/usr/bin/chromedriver'

    IMAGE = PROJECT_DIRECTORY + "/suit/img/"

    AUEXE = PROJECT_DIRECTORY + "/common_data/au.exe"

    CANGDANFILE = PROJECT_DIRECTORY + "/common_data/B单票多箱.txt"

    EXC_IMPORT = PROJECT_DIRECTORY + "/common_data/导入舱单测试模板文件.xlsx"

    SHUIDAN = PROJECT_DIRECTORY + "/common_data/水单图片.jpg"

    DOWNLOAD_PATH = PROJECT_DIRECTORY + "/download_data/"

    SUBFILE = PROJECT_DIRECTORY + "/common_data/批量订阅模板.xlsx"

    download_data = PROJECT_DIRECTORY + "/download_data"