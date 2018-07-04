# 统计函数的执行次数
def set_func(func):
    num = [0]   # 闭包中外函数中的变量指向的引用不可变,所以定义一个可变列表
    def call_func():
        func()
        num[0] += 1
        print("执行次数",num[0])
    return call_func

# 待测试方法
@set_func
def test():
    pass

test()
test()
test()

