import threading
import socket
import sys

def handlering(socket: socket.socket):
    while True:
        try:
            data = socket.recvfrom(1024)
            message = data[0].decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Ошибка при получении данных: {e}")
            break

def user_input(socket: socket.socket):
    while True:
        message = input()
        if message:
            try:
                socket.sendto(f"**SEND|{message}".encode('utf-8'), server_address)
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
                break

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

connect = input("Введите (ip:port): ")
try:
    ip, port = connect.strip().split(':')
    server_address = (ip, int(port))
except ValueError:
    print("Неправильный формат IP-адреса или порта.")
    sys.exit()

username = input("Введите username: ").strip()
if not username:
    print("Имя пользователя не может быть пустым.")
    sys.exit()

try:
    client.sendto(f"**JOIN|{username}".encode('utf-8'), server_address)
except Exception as e:
    print(f"Ошибка при подключении к серверу: {e}")
    sys.exit()

inp = threading.Thread(target=user_input, args=(client,))
handler = threading.Thread(target=handlering, args=(client,))

inp.start()
handler.start()
