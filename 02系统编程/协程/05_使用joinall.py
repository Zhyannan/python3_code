import gevent  # 协程库


# 一边唱歌,一边跳舞

def copy():
    while True:
        print("复制")
        gevent.sleep(1)


def main():
    """使用协程去运行我们跳舞与唱歌"""
    # gevent.spawn # 我们循环一次用一个协程
    
    # 定义一个列表
    spawn_list = list()
    
    for temp in range(10):
        # copy()
        spawn = gevent.spawn(copy)
        spawn_list.append(spawn)
    
    # 等一下
    gevent.joinall(spawn_list)


if __name__ == '__main__':
    main()
