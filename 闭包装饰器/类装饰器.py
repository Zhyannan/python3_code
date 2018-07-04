class SetFun(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("功能")
        self.func()  # 实例加()，自动触发call方法，调用函数


@SetFun  # test=SetFun(test)  # 加类装饰器，相当于把test当做参数传给类，所以要定义__init__方法
def test():
    print('test')


test()  # 实例对象加()，自动调用__call__方法，所以要定义__call__，不然报错
