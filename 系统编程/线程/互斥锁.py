import threading

g_num = 0

def num1():
    global g_num
    for i in range(500000):
        lock1.acquire()
        g_num += 1
        lock1.release()


def num2():
    global g_num
    for i in range(500000):
        lock1.acquire()
        g_num += 1
        lock1.release()


lock1 = threading.Lock()
lock2 = threading.Lock()

t1 = threading.Thread(target=num1)
t2 = threading.Thread(target=num2)
t1.start()
t2.start()
print("程序运行完全局变量值为：%d"%g_num)


