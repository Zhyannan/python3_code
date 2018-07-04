# 装饰器传参条件
# 1.三个函数嵌套
# 2.第三层（最外层），返回闭包的最外层（第二层）
# 3.第三层必须有参数，没有参数就没必要写第三层了
# 框架设计会用到这个技术
def set_args(url):
    def set_fun(func):
        def call_fun(*args, **kwargs):
            print("地址：", url)
            return func(*args, **kwargs)
        return call_fun
    return set_fun

# 分两步理解
# 1.set_args("www.baidu.com") ---> 将地址传给url，并得到set_fun的引用
# 2.@set_fun ---> test=set_fun(test)=call_fun
# 3.test() ---> call_fun()
@set_args("www.baidu.com")
def test():
    print('test')
test()
