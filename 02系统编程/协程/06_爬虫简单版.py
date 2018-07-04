from urllib.request import *  # url库


# 1.输入一个网址打开一个网页的对象
# 2.读取内容
# 3.把内容存入


def main():
    """把一个图片写入"""
    # 得到请求的对象
    
    
    
    request_url = urlopen(
        "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3865973564,2810423211&fm=27&gp=0.jpg")
    
    # 读
    content = request_url.read()
    
    # 写
    with open("./python14/1.jpg", "wb") as f:
        f.write(content)


if __name__ == '__main__':
    main()
