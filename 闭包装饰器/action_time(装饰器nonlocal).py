# 统计函数的执行时间
import time


def set_func(func):
    start_time = time.time()  # 闭包中外函数中的变量指向的引用不可变

    def call_func():
        func()   # 执行函数
        end_time = time.time()    # 记录执行结束时间
        action_time = end_time - start_time
        print("执行时间：", action_time)

    return call_func


# 待测试方法
@set_func
def test():
    time.sleep(1)
    print("test")


test()


