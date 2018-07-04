import gevent  # 协程库
import time

# 只要协程第一步就要请猴子
from  gevent import monkey

# 打补丁
monkey.patch_all()  # 会把当前程序中所有的耗时全转换成我们gevent中的耗时


# 一边唱歌,一边跳舞

def read():
	while True:
		print("读取")
		time.sleep(1)  # 系统的自动转换成我们gevent.sleep(1)


def copy():
	while True:
		print("复制")
		# gevent.sleep(1)
		time.sleep(1)


def main():
	"""使用协程去运行我们跳舞与唱歌"""
	# gevent.spawn # 我们循环一次用一个协程

	# 定义一个列表
	spawn_list = list()

	spawn = gevent.spawn(copy)
	spawn_list.append(spawn)

	read_spawn = gevent.spawn(read)
	spawn_list.append(read_spawn)

	# 等一下
	gevent.joinall(spawn_list)


if __name__ == '__main__':
	main()
