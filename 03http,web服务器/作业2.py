"""写一个服务器显示不需要的页面，页面内容为"你访问的链接不翼而飞了"""
import re
from socket import *

DOCUMENTS_ROOT_DIR = "./html"


def deal_client(client):
    # 接收请求体数据
    request_data = client.recv(1024).decode("utf-8")
    request_data_lines = request_data.splitlines()
    for request_data_line in request_data_lines:
        print(request_data_line)
    
    # 获取客户端请求地址,GET / HTTP/1.1
    file_name = re.match("^\w+\s+(/[^\s]*)", request_data_lines[0]).group(1)
    
    if "/" == file_name:
        file_name = DOCUMENTS_ROOT_DIR + "/" + "index.html"
    else:
        file_name = DOCUMENTS_ROOT_DIR + file_name
    
    try:
        f = open(file_name,"rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = "你访问的链接不翼而飞了"
        response = response_start_line + "\r\n" + response_body
    else:
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_body = f.read().decode("utf-8")
        response = response_start_line + "\r\n" + response_body
        
    # 发送响应数据
    client.send(response.encode("gbk"))
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
