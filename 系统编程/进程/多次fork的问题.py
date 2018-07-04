# -*-coding=utf-8-*-
import os
import time


pid = os.fork()
if pid == 0:
    print("子进程1")
else:
    print("主进程")

pid = os.fork()
if pid == 0:
    print("子进程2")
else:
    print("主进程")

time.sleep(1)