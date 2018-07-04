import socket
import multiprocessing
import re
import mini_web


class WebServer(object):
    """服务器类"""

    def __init__(self):
        """初始化tcp服务器"""
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server_socket.bind(('', 8899))
        # 2.监听
        self.tcp_server_socket.listen(128)

    def run_server(self):
        """完成服务器的控制"""
        while True:
            new_socket, addr = self.tcp_server_socket.accept()
            # 创建进程为这个客户端服务
            multiprocessing.Process(target=self.exec_client, args=new_socket).start()

            new_socket.close()

    def exec_client(self, new_socket):
        """为这个客户端返回数据"""
        # 接收客户端发送过来的数据
        request_data = new_socket.recv(1024).decode('utf-8')
        print(request_data)

        ret = re.match(r"[^/]+(/[^ ]*)", request_data)
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        else:
            print("浏览器复用....")

        # 如果是html文件，则会调用mini_web中的application函数进行返回页面数据
        if file_name.endswith(".html"):
            environ = dict()  # 给mini_web 传参数
            environ['file_name'] = file_name
            # 获取mini_web中的application函数的返回值
            response_body = mini_web.application(environ,self.set_response_headers)
            response_header = 'HTTP/1.1 %s\r\n' % self.status
            response_header += 'Content-Length:%d'% response_body

            response = response_header + '\r\n' + response_body
            new_socket.send(response.encode("utf-8"))

        else:
            # 返回静态数据
            try:
                with open("./static" + file_name, "rb") as f:
                    content = f.read()
            except:
                response_header = "HTTP/1.1 404 Not Found\r\n"
                response_body = "请求的文件不存在！"
                response = response_header + '\r\n' + response_body
                new_socket.send(response.encode('utf-8'))
            else:
                response_header = "HTTP/1.1 404 200 OK\r\n"
                response_body = content.decode("utf-8")
                response = response_header + '\r\n' + response_body
                new_socket.send(response.encode('utf-8'))

        # 关闭套接字
        new_socket.close()

    def set_response_headers(self, status, start_headers):
        self.status = status
        self.start_headers = start_headers


def main():
    server = WebServer()
    server.run_server()


if __name__ == '__main__':
    main()
