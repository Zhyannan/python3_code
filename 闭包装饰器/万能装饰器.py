# 函数几种情况:
# 1.无参,无返回
# 2.无参,有返回
# 3.有参,无返回
# 4.有参,有返回

# 装饰前的test是由func指向
# 装饰后的test其实是call_fun
print("******1.无参数，无返回*****")


def set_fun(func):
    def call_fun():
        print("权限")
        func()

    return call_fun


@set_fun
def test():
    print('test')


test()

# 装饰前的test是由func指向
# 装饰后的test其实是call_fun
# 装饰器的功能只是添加额外的功能，不会改变原先函数的值和调用
print('*****2.无参数，有返回值*****')


def set_fun(func):
    def call_fun():
        print('权限')
        return func()

    return call_fun


@set_fun  # test = set_fun(test)
def test():
    return 100


print(test())  # test()是call_fun(),print(test())就是打印test的返回值

print("*****3.有参数，无返回值*****")


def set_fun(func):
    def call_fun(args):
        print("权限")
        func(args)

    return call_fun


@set_fun
def test(args):
    print(args)


test(123)

print("*****4.有参数，有返回值*****")


def set_fun(func):
    def call_fun(args):
        print("权限")
        return func(args)  # 等价于return 200（test的返回值）

    return call_fun


@set_fun
def test(args):
    return 200, args


print(test(300))  # print(call_fun(300))

print("*****万能装饰器*****")
def set_fun(func):
    def call_fun(*args, **kwargs):
        print('要添加的功能')
        return func(*args, **kwargs)
    return call_fun


@set_fun
def test(*args, **kwargs):
    print(args)
    print(kwargs)
    return 400


b = test(123,200, a=10)
print(b)
