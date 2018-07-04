#被调用py文件代码
#假设文件名为cor.py
from functools import wraps

'''
通过协程实现记录所有函数被调用次数
'''

def coroutine(func):
    @wraps(func)
    def execute_next(*args, **kwargs):
        result = func(*args, **kwargs)
        next(result)
        return result
    return execute_next

@coroutine
def cor(start=0):

    while True:
        tot = yield start
        #yield start #实现功能同
        start += 1

cc = cor()

def total(func):
    @wraps(func)
    def count(*args, **kwargs):
        co = cc.send(1)
        print ('调用次数： %s' % co)
        result = func(*args, **kwargs)
        return result
    return count


#这里是用作统计的函数
#++++++++++++++++++++++++++++++++
@total
def test(x):
    pass

@total
def test2(x):
    pass