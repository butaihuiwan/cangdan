import yagmail

# 链接邮箱服务器
yag = yagmail.SMTP(user="tangpeng@uni-log.com.cn", password="Hello1234", host='smtp.mxhichina.com', port='465')

# 邮箱正文
body = '这是自动测试邮件,无需回复'

# 发送邮件
yag.send(to='925747399@qq.com', subject='工作文件', contents=[body, r"D:\ceshi\代码\cangdan-test\suit\img"])
print('1')
