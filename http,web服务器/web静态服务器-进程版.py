# conding=utf-8
import re
import socket
import gevent

# 配置服务器,设置静态文件根目录
import multiprocessing

import time

DOCUMENTS_ROOT_DIR = "./html"


class WSGIServer(object):
    def __init__(self):
        # 创建服务器套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 复用端口，固定写法
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 服务器需要绑定端口
        self.server_socket.bind(("", 7788))
    
    def start(self):
        # 监听客户端链接请求
        self.server_socket.listen(128)
        while True:
            # 创建新的套接字，等待客户端连接
            client, client_address = self.server_socket.accept()
            # 打印客户端信息，注意，会打印两份，一份主进程，一份子进程
            print("=" * 40)
            print("用户:【%s,%s】连接上了" % client_address)

            # 创建一个子进程来为浏览器服务
            client_process = multiprocessing.Process(target=self.exec_client, args=(client,))
            client_process.start()

            # 因为子进程已经复制了父进程的套接字等资源，所以父进程调用close不会将他们对应的这个链接关闭的
            # 关闭主进程套接字
            client.close()

            print("=" * 40)
            print("用户:【%s,%s】连接上了" % client_address)
    
    def exec_client(self, client):
        """为一个客户端服务"""
        # 接收请求头
        request_data = client.recv(1024).decode("utf-8")
        print("***** client_request_data *****")
        print(request_data)
        # 解析请求报文---> GET / HTTP/1.1
        # 提取用户请求文件名
        file_name = re.match(r"[^/]+(/[^ ]*)\s", request_data)
        if file_name:
            file_name = file_name.group(1)
            print("file name is ====>%s" % file_name)
        
            # 如果没有指定访问哪个页面。例如index.html
            if file_name == "/":
                file_name = DOCUMENTS_ROOT_DIR + "/index.html"
            else:
                file_name = DOCUMENTS_ROOT_DIR + file_name
        else:
            print("浏览器复用了.....")
        
        try:
            # 打开文件，读取数据
            f = open(file_name, "rb")
        except Exception as error:
            print(error)
            response_headers = "HTTP/1.1 404 not found\r\n"
            response_headers += "\r\n"
            response_body = bytes("---sorry,file not found---", "utf-8")
        else:
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "\r\n"
            response_body = f.read()
            f.close()
        
        # 因为头信息是字符串拼接的，不能与以二进制打开的body一起发送，故分开发送
        client.send(response_headers.encode("utf-8"))
        client.send(response_body)

        # 关闭子进程套接字
        client.close()


def main():
    """作为程序的主控制入口"""
    static_web_server = WSGIServer()
    static_web_server.start()


if __name__ == '__main__':
    main()
