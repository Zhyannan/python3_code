# 生成器是一种特殊的迭代器


# 列表推导式
x = [i for i in range(10)]

print(x)

x = (i for i in range(10))

print(x)

for temp in x:
	print(temp)