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
    
    # 定义一个协程列表
    # spawns_list = []
    spawns_list = list()  # 创建一个空的列表
    spawns_list.append(dance_spawn)
    spawns_list.append(song_spawn)
    
    # 给一份名单让我们的主进程等待
    gevent.joinall(spawns_list)


if __name__ == '__main__':
    main()
