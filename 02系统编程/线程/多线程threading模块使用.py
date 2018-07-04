# coding=utf-8
import time
import threading


def func():
    print("----func----")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=func)
        t.start()   # 多线程并发