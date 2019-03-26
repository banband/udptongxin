import socket
import ast

xinxi = {"chehao":"黑KY6676","yuyueshijian":"2018-03-14 12:26:25"}

def send_msg(udp_socket):
    dest_ip = '122.157.54.26'
    dest_pore = 7788
    send_data = input("xinxi:")
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_pore))


def recv_msg(udp_socket):
    recv_data =udp_socket.recvfrom(1024)
    #print("%s:%s" %(str(recv_data[1]),recv_data[0].decode("utf-8")))
    ss = recv_data[0].decode("utf-8")
    ss_dict = ast.literal_eval(ss)
    print(ss_dict["chehao"])
    print(ss_dict["jifen"])

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("", 7790))

    while True:
        send_msg(udp_socket)
        recv_msg(udp_socket)

if __name__ == '__main__':
    main()