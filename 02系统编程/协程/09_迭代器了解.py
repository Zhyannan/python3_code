# Python中的迭代器
# 只要能被我们for...in ...就是迭代器
a = [1, 2, 3]

for temp in a:
	print(temp)

a = "abc"
for temp in a:
	print(temp)

# isinstance() # 这个是判断类型

# 迭代器必须是可以迭代的对象,可以被迭代(遍历)
