from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，最多接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())
q.put("消息3")
print(q.full())

try:
    q.put("消息4",True,2)
except:
    print("消息队列已满，现有消息数量：%s"%q.qsize())
    

try:
    q.put_nowait("消息4")
except:
    print("消息队列已满，现有消息数量：%s" % q.qsize())
    

# 推荐的方式，先判断消息队列是否已满，再写入
if not q.full():
    q.put_nowait("消息4")
    
# 读取消息时，先判断消息队列是否为空，在读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())