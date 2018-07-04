# 复制文件夹
# 1.创建一个文件夹
# 2. 要被复制的文件夹进行遍历
# 3. 循环复制到别一个文件夹中

# 线程要做什么,做耗时的,复制
import multiprocessing
import os

from shutil import rmtree


def copy_file(file_before, file_after):
	"""复制文件"""
	# 1.读取文件内容
	with open(file_before, 'rb') as f:
		content = f.read()
	# 2.新文件中写入内容
	with open(file_after, 'wb') as f:
		f.write(content)

	# 打一下进程
	print(multiprocessing.current_process().name)


def main():
	"""复制文件夹"""
	# 创建文件 夹
	# 创建文件 夹前判断是否存在,如果存在,那么删除
	if os.path.exists("./python14_备份"):  # 这个判断是否存在
		# 删除夹文件夹
		rmtree("./python14_备份")  # 删除文件夹,是文件夹中有内容的

	# 删除以后创建
	os.mkdir("./python14_备份")

	# 得到文件夹的内容
	files_list = os.listdir("./python14")

	# 循环复制到别一个文件
	for file_name in files_list:
		# 复制文件
		file_before = "./python14/%s" % file_name  # 复制前的文件路径
		file_after = "./python14_备份/%s" % file_name  # 复制后的文件路径
		# 开始复制
		# copy_file(file_before, file_after)  # 看代码中的函数快捷键 ctrl_B
		# 创建一个线程
		multiprocessing.Process(target=copy_file, args=(file_before, file_after)).start()


if __name__ == '__main__':
	main()
