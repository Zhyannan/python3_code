"""使用multiprocessing模块中的Queue，
完成子进程中将hello传递到父进程中，父进程打印出来"""
import multiprocessing

import os


def p_m(queue):
    """父进程"""
    info = queue.get()
    print(info)
    print("主进程id：", os.getpid())


def c_m(queue):
    """子进程"""
    queue.put("hello")
    print("子进程id：", os.getpid())
    print("子进程中父进程id:", os.getppid())


def main():
    # 创建队列
    queue = multiprocessing.Queue()
    # 创建子进程
    c_m_p = multiprocessing.Process(target=c_m, args=(queue,))
    c_m_p.start()
    c_m_p.join()
    # 执行父进程
    p_m(queue)


if __name__ == '__main__':
    main()
