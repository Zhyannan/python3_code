# coding=utf-8
import multiprocessing
import os

"""
Process对象的初始化参数为
Process(group=None, target=None, name=None, args=(), kwargs={})，
其中group参数必须为None（为了与threading.Thread的兼容），
target指向可调用对象（该对象在新的子进程中运行），
name是为该子进程命的名字（默认是Proess-1,Process-2, …这样），
args是被调用对象的位置参数的元组列表，
kwargs是被调用对象的关键字参数。
"""
# 子线程要进行的代码
def run_proc(name):
    print("子进程运行中，name=%s，pid=%d..." % (name, os.getppid()))


if __name__ == '__main__':
    print("父进程 %d." % os.getpid())
    p = multiprocessing.Process(target=run_proc, args=("test",))
    print("子进程将要执行")
    p.start()
    p.join()
    print("子进程已结束")
