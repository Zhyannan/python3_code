# conding=utf-8
"""
客户端发送的
GET / HTTP/1.1   # 域名后面的部分就是路径，默认是‘／’
Host: localhost:7788
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

GET /favicon.ico HTTP/1.   # 收藏夹图标
Host: localhost:7788
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://localhost:7788/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
"""
import re
import socket

# 配置服务器,设置静态文件根目录
DOCUMENTS_ROOT_DIR = "./html"


def handle_client(client):
    """为一个客户端服务"""
    
    request_data = client.recv(1024).decode("utf-8")
    print("***** client_request_data *****")
    # str.splitlines([keepends])
    # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，参数 keepends 默认为 False，不包含换行符，如果为 True，则保留换行符。
    request_header_lines = request_data.splitlines()
    for line in request_header_lines:
        print(line)
    
    # 解析请求报文---> GET / HTTP/1.1
    request_start_line = request_header_lines[0]
    # 提取用户请求文件名
    file_name = re.match("\w+\s+(/[^ ]*)\s", request_start_line).group(1)
    print("file name is ====>%s" % file_name)
    
    # 如果没有指定访问哪个页面。例如index.html
    
    if file_name == "/":
        file_name = DOCUMENTS_ROOT_DIR + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT_DIR + file_name
    
    try:
        # 打开文件，读取数据
        f = open(file_name, "rb")
    except IOError:
        response_headers = "HTTP/1.1 404 not found\r\n"
        response_headers += "\r\n"
        response_body = bytes("---sorry,file not found---", "utf-8")
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"
        response_body = f.read()
        f.close()
    finally:
        # 因为头信息是字符串拼接的，不能与以二进制打开的body一起发送，故分开发送
        client.send(response_headers.encode("utf-8"))
        client.send(response_body)
        # 打印服务器返回数据
        print("***** server_response_data *****")
        server_response_lines = response_headers + response_body.decode("utf-8")
        response_lines = server_response_lines.splitlines()
        for response_line in response_lines:
            print(response_line)
        client.close()


def main():
    """作为程序的主控制入口"""
    # 创建服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 复用端口，固定写法
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 服务器需要绑定端口
    server_socket.bind(("", 7788))
    # 监听客户端链接请求
    server_socket.listen(128)
    while True:
        # 创建新的客户端
        client, client_addr = server_socket.accept()
        print("=" * 40)
        print("用户:【%s,%s】连接上了" % client_addr)
        # 为客户端服务
        handle_client(client)


if __name__ == '__main__':
    main()
