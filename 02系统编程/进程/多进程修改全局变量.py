# coding=utf-8
import os
import time

# 多进程中，每个进程中所有数据（包括全局变量）都各自拥有一份，互不影响
num = 0
pid = os.fork()
if pid < 0:
    print("fork调用失败")
elif pid == 0:
    num += 1
    print("我是子进程，num=%d" % num)
else:
    time.sleep(1)
    num += 1
    print("我是父进程，num=%d" % num)
