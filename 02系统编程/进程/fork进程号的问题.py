#coding=utf-8
import os


rpid = os.fork()
if rpid < 0:
    print("fork调用失败")
# 子进程永远返回0，父进程返回子进程的id
elif rpid == 0:
    print("我是子进程%s,我的父进程是%s"%(os.getpid(),os.getppid()))
elif rpid > 0:
    print("我是父进程%s，我的子进程是%s"%(os.getpid(),rpid))
	      
print("父子进程都可以执行这里的代码")