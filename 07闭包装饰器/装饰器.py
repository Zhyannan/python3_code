from time import ctime, sleep


def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        func()

    return wrapped_func   #装饰后，内部函数wrapped_func被引用，所以外部函数的func变量并没有释放


@timefun  # foo作为参数赋值给func，foo接收指向timefunc返回的wrapped_func
def foo():  # 调用foo(),等价于调用wrapped_func()
    print("I am foo")


foo()
sleep(2)
foo()
class A:
    pass


print(object.__new__(A))

