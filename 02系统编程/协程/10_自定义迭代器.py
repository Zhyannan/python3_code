# 自定义迭代器

from collections import Iterable


class MyList(object):
    def __iter__(self):  # 可迭代对象,返回一个可迭代对象,返回自己
        return self
    
    def __next__(self):  # 迭代的时候取值
        return "123"


my_list = MyList()

print(isinstance(my_list, Iterable))

for temp in my_list:
    print(temp)
