import socketserver

class MyUDPHandlers(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        
        split_data = data.decode().split('|')
        
        # Конект к чату, **JOIN|USERNAME
        if data.decode().startswith('**JOIN'):
            
            if self.client_address not in members.keys() and split_data[1] not in members.values():
                members.update({self.client_address : split_data[1]})
                socket.sendto(f"{PREFIX} Вы авторизовались в чате {HOST}".encode( ), self.client_address)
                print(members)
                
                
                for i in members.keys():
                    if i != self.client_address:
                        socket.sendto(f"{PREFIX} Новый пользователь {members[self.client_address]} подключен".encode(), i)
                
            elif self.client_address in members.keys():
                socket.sendto(f"{PREFIX} Вы уже подключались к серверу, ваш ник {members[self.client_address]}".encode( ), self.client_address)
            elif self.client_address not in members.keys() and split_data[1] in members.values():
                
                print(f"{self.client_address} попробовал занять занятый ник {split_data[1]}")
                socket.sendto(f"{PREFIX} Ник {split_data[1]} уже занят".encode( ), self.client_address)
                
        if data.decode().startswith('**SEND'):
            
            if self.client_address not in members.keys():
                socket.sendto("{PREFIX} Вы не авторизованы".encode(), self.client_address)
            else:
                
                print(f"{members[self.client_address]}:{self.client_address} -> {split_data[1]}")
                for i in members.keys():
                    if i != self.client_address:
                        socket.sendto(f"{members[self.client_address]}: {split_data[1]}".encode(), i)
                
        
        
HOST, PORT = '192.168.1.8', 50005

PREFIX = "СЕРВЕР:"

members = {}
with socketserver.UDPServer((HOST, PORT), MyUDPHandlers) as server:
    server.serve_forever()
    
    
# while True:
#     data, addr = server.recvfrom(1024)
    
#     # ------------------------------------------ #
#     #     INDEX           [0]     [1]     [2]   #
#     # data.decode() = **command|username|param #
#     event =  data.decode().split("|")
#     # ------------------------------------------ #
#     if event[0] == '**ping':
#             server.sendto('1'.encode(), addr)
        
    
#     if event[0] == '**join':
#         if addr not in members.values():
#             members.update({addr : event[1]}) 
#             server.sendto(f"{PREFIX} Вы авторизовались в чате, сервера {HOST}:{PORT}".encode(), addr)
#             print(f"{event[1]}:{addr} авторизовался")
            
#             for i in members.keys():
#                 if i != addr:
#                     server.sendto(f"{PREFIX} Новый пользователь {event[1]} подключен".encode(), i)
                    
#         elif:
#             print(f"{addr} попробовал занять занятый ник {event[1]}")
#             server.sendto(f"{PREFIX} Никнейм {event[1]} занят".encode(), addr)
    
#     if event[0] == '**send':
#         if not addr in members:
#             server.sendto("{PREFIX} Вы не авторизованы".encode(), addr)
#         else:
#             print(f"{event[1]}:{addr} -> {event[2]}")
#             for i in members.keys():
#                 if i != addr:
#                     server.sendto(f"{event[1]}: {event[2]}".encode(), i)