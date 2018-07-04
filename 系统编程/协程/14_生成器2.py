# 生成器是一种特殊的迭代器

def test():
	for temp in range(10):
		yield temp  # 他就是一个input() 一个函数return改成yield就是生成器了

print(test())


for temp in test():
	print(temp)