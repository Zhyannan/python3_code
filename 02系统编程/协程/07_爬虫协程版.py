from urllib.request import *  # url库

# 1.输入一个网址打开一个网页的对象
# 2.读取内容
# 3.把内容存入
import gevent
from  gevent import monkey

monkey.path_all()  # 打补丁


def down_image(url, file_name):
    print("开始", file_name)
    # 打开网页
    request_url = urlopen(url)
    
    # 读取数据
    content = request_url.read()
    
    # 写入
    with open("./python14/%s.jpg" % file_name, 'wb') as f:
        f.write(content)
    
    print("结束:", file_name)


def main():
    """下载 一群的图片"""
    # 定义一个图片的列表
    images_list = list()
    images_list.append("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3865973564,2810423211&fm=27&gp=0.jpg")
    images_list.append("https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2814129524,3349341830&fm=27&gp=0.jpg")
    images_list.append("https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2294864897,3704283980&fm=27&gp=0.jpg")
    
    # 定义一个协程列表
    spwan_list = list()
    
    i = 0
    # 循环去遍历我们的地址去写入图片
    for url in images_list:
        # 下载图片
        i += 1
        # down_image(url,str(i))
        
        spawn = gevent.spawn(down_image, url, str(i))
        # 加入到列表中
        spwan_list.append(spawn)
    
    # 让我们的主进程等 一下
    gevent.joinall(spwan_list)


if __name__ == '__main__':
    main()
