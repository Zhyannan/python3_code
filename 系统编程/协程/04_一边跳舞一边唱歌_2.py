import gevent  # 协程库


# 一边唱歌,一边跳舞

def dance():
	while True:
		print("跳舞")
		# 睡一会,但是一定要用协程的睡
		gevent.sleep(1)


def song():
	while True:
		print("唱歌")
		gevent.sleep(1)


def main():
	"""使用协程去运行我们跳舞与唱歌"""
	dance_spawn = gevent.spawn(dance)

	song_spawn = gevent.spawn(song)


	# join一定要写在我们全都添加完以后
	dance_spawn.join()  # 等一下,一定要处理
	song_spawn.join()  # 两个都等


if __name__ == '__main__':
	main()
