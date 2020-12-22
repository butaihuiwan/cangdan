import os
import shutil


def del_dir(path):
    """删除指定文件夹
    path: 绝对路径"""
    try:
        url = shutil.rmtree(path)
        print('path 删除完成')
    except:
        print('文件不存在')

    # 新建image 文件夹
    os.mkdir(path)


def del_files(path, type):
    """删除文件夹中指定格式文件
    path: 绝对路径
    type:指定要删除的格式，如：.xlsx 格式文件"""
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(type):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))


def find_filename(path, type):
    """获取文件夹中指定格式的filename"""
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(type):
                return name
