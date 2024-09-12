import threading
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Введите (ip:port)", end=' ')
connect = str(input())

ip, port = connect.split(':')
server_address = (ip, int(port))


print("Введите username:", end=' ')
username = str(input())

client.sendto(f"**JOIN|{username}".encode(), server_address)

def handlering(socket: socket.socket):
    while True:
        data = client.recvfrom(1024)
        print(data[0].decode())
        
def user_input(socket: socket.socket):
    while True:
        message = input()
        if message:
            client.sendto(f"**SEND|{message}".encode(), server_address)


inp = threading.Thread(target=user_input, args=(client, ))
handler = threading.Thread(target=handlering, args=(client, ))

inp.start()
handler.start()

# import threading

# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# print("Введите (ip:port)", end=' ')
# connect = str(input())

# ip, port = connect.split(':')
# server_address = (ip, int(port))


# print("Введите username:", end=' ')
# username = str(input())

# client.sendto(f"**join|{username}".encode(), server_address)

# def handlering(socket: socket.socket):
#     while True:
#         data = client.recvfrom(1024)
#         print(data[0].decode())
        
# def user_input(socket: socket.socket):
#     while True:
#         message = input()
#         if message:
#             client.sendto(f"**send|{username}|{message}".encode(), server_address)


# inp = threading.Thread(target=user_input, args=(client, ))
# handler = threading.Thread(target=handlering, args=(client, ))

# inp.start()
# handler.start()