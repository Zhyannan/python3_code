# 队列
import multiprocessing

# 队列定义三个,如果不写就是内存大小,不建议
queue = multiprocessing.Queue(3)
# 放
queue.put("123")
queue.put("123")
queue.put("123")
# queue.put("123")
print(queue.qsize())  # 个数,取了就没了

# 取
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
