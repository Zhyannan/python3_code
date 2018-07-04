# input() 只能用在主进程中
import multiprocessing


def write():
	input()  # 只能用在主进程


def main():
	"""bug"""
	multiprocessing.Process(target=write).start()


if __name__ == '__main__':
	main()


