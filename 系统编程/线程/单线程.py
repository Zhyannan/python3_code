# coding=utf-8
import threading

import time

g_num = 0


def sum_num1(n):
    global g_num
    for i in range(n):
        lock.acquire()
        g_num += 1
        lock.release()
 
        
def sum_num2(n):
    global g_num
    for i in range(n):
        lock.acquire()
        g_num += 1
        lock.release()


lock = threading.Lock()
t1 = threading.Thread(target=sum_num1, args=(1000000,))
t2 = threading.Thread(target=sum_num2, args=(1000000,))
t1.start()
t2.start()
while len(threading.enumerate()) != 1:
    time.sleep(1)
print(g_num)


