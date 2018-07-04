# coding=utf-8
import threading
import time

def dance():
    for i in range(3):
        print("%d跳舞"%i)
        time.sleep(1)

def sing():
    for i in range(3):
        print("%d唱歌"%i)
        time.sleep(1)


if __name__ == '__main__':
    print("---开始---%s"%time.ctime())
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为：%d"%length)
        if length <= 1:
            break
        time.sleep(3)
    print("---结束---%s"%time.ctime())
