from multiprocessing import Queue, Process
import time
from random import random
from socket import socket


def write(q):
    for value in ["A", "B", "C"]:
        q.put(value)
        time.sleep(random())


def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("get %s from queue." % value)
            time.sleep(random())
        else:
            break
            


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 等待pw结束
    pw.join()
    
    # 启动子进程pr，读取
    pr.start()
    pr.join()
