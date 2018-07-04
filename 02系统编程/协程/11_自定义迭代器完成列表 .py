# 自定义迭代器

from collections import Iterable


# 我们迭代器一初始化就有一个列表


class MyList(object):
    # 初始化的时候就有列表
    def __init__(self):
        use_list = [1, 2, 3, 4, 5]
        self.use_list = use_list  # 初始化的时候有一个列表了
        self.count = 0  # 列表的第一个索引
    
    def __iter__(self):  # 可迭代对象,返回一个可迭代对象,返回自己
        return self
    
    def __next__(self):  # 迭代的时候取值
        # 如果我们的个数已经到底了,那么我们手动的去抛出异常
        if self.count < len(self.use_list):
            # 调用的时候加1
            value = self.use_list[self.count]
            self.count += 1
            return value  # 怎么让我们的迭代器停下来,使用异常
        else:
            # 超出了
            raise StopIteration  # 停止迭代


my_list = MyList()

print(isinstance(my_list, Iterable))

for temp in my_list:
    print(temp)
