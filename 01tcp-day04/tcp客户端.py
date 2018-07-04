from socket import *

def main():

    # 创建tcp客户端套接字
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 输入服务器ip/port
    ser_ip = input("请输入服务器ip：")
    ser_port = int(input("请输入服务器port："))

    # 链接服务器
    tcp_client_socket.connect((ser_ip, ser_port))

    # 发送数据
    send_msg = input("请输入要发送的数据：")
    tcp_client_socket.send(send_msg.encode("utf-8"))

    # 接收数据
    print(".....正在接收数据.....")
    recv_data = tcp_client_socket.recv(1024)
    print('接收到的数据：%s' % recv_data.decode("utf-8"))

    # 关闭客户端套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()

