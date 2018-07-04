# 统计函数的执行次数

def set_func(func):
    num = 0  # 闭包中外函数中的变量指向的引用不可变

    def call_func():
        func()   # 执行函数
        nonlocal num  # 使用nonlocal 访问修改外部函数变量
        num += 1    # 记录执行次数
        print("执行次数", num)

    return call_func


# 待测试方法
@set_func
def test():
    pass


test()
test()
test()
