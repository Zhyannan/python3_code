# conding=utf-8
"""
步骤1：浏览器首先向服务器发送HTTP请求
方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
路径：/full/url/path；
域名：由Host头指定：Host: www.sina.com
以及其他相关的Header；
如果是POST，那么请求还包括一个Body，包含用户数据

步骤2：服务器向浏览器返回HTTP响应，响应包括：
响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
响应类型：由Content-Type指定；
以及其他相关的Header；
通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
"""
import socket

"""浏览器就是一个客户端，因为它发送请求给HTTP服务器（也就是web服务器），web服务器返回响应给客户端。"""


def handle_client(client):
    """为一个客户端服务"""
    # 获取客户端(浏览器)请求数据
    request_data = client.recv(1024).decode("utf-8")
    print("***** client_request_data *****")
    # str.splitlines([keepends])
    # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，参数 keepends 默认为 False，不包含换行符，如果为 True，则保留换行符。
    request_header_lines = request_data.splitlines()
    # 打印客户端请求数据
    for line in request_header_lines:
        print(line)
    
    # 构造响应数据（header）
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源成功响应，OK是说明
    response_headers += "\r\n"  # 用一个空行与body进行隔开
    # 组织内容（body）
    response_body = "hello world"
    
    # 向客户端(浏览器)返回响应信息
    response = response_headers + response_body
    client.send(response.encode("utf-8"))
    # 打印服务器响应数据
    print("***** server_response_data *****")
    response_lines = response.splitlines()
    for response_line in response_lines:
        print(response_line)
    # 服务器发送完响应后，关闭连接。（HTTP是一个无状态的连接）下一次再连接，服务器不会知道是否是上一次的用户
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
