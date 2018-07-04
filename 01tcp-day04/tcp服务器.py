from socket import *


def main():
    # 创建tcp服务器套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 绑定地址
    tcp_server_socket.bind(("",8899))

    # 变成被动套接字
    tcp_server_socket.listen(128)

    while True:
        # 链接
        client_soc,client_addr = tcp_server_socket.accept()
        print("-----正在等待客户端链接-----")

        # 收发数据
        send_data = input("请输入要发送的数据：")
        client_soc.send(send_data.encode("utf-8"))
        print("*****正在等待客户端数据*****")
        recv_data = client_soc.recv(1024)
        print("收到的数据：%s" % recv_data.decode("utf-8"))

        # 关闭客户端套接字
        client_soc.close()


if __name__ == '__main__':
    main()