import random
"""随机生成注册99种用户名，邮箱号"""

num = [i for i in range(1, 100)]
data = random.sample(num,99)
len = len(data)
print(len)
if len > 0:
    for i in data:
        username = "xxx" + str(i)
        email = str(i) + "@qq.com"
        data = username + "," + email + "\n"
        with open('./reg_data.txt', "a+") as e:
            e.write(data)
            len -= 1

