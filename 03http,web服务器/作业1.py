"""写一个静态服务器，显示固定页面，页面内容为hello world"""
from socket import *


def deal_client(client):
    # 接收请求体数据
    request_data = client.recv(1024).decode("utf-8")
    print(request_data)
    
    # 编辑响应头数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_body = "hello world"
    response = response_start_line + "\r\n" + response_body
    # 发送响应数据
    client.send(response.encode("utf-8"))
    # 关闭套接字
    client.close()


def main():
    # 创建服务器套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 复用端口
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定
    server_socket.bind(("", 7788))  # 注意bind里面放一个元组
    # 监听
    server_socket.listen(128)
    while True:
        # 创建新的客户端
        client, client_addr = server_socket.accept()
        deal_client(client)


if __name__ == '__main__':
    main()
