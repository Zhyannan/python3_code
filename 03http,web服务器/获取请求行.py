import re
#
# # s = "GET / HTTP/1.1"
# # a = re.match("\w+\s+(/[^\s]*)",s)
# # print(a)
# import time
#
# t1 = time.ctime()
# print(t1)

file_name = ".html/login.html/s?name=zhangsan&pwd=123456"
login_info = re.search(r"(name=[a-zA-Z0-9-_]+)&(pwd=[\d]+)", file_name).group()
print(login_info)