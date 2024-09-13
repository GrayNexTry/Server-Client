import socketserver
import numpy as np
import cv2

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        
        header = data[:8]
        payload = data[8:]
        
        # Извлечение заголовка
        packet_seq = int.from_bytes(header[:4], 'big')
        packet_num = int.from_bytes(header[4:6], 'big')
        total_packets = int.from_bytes(header[6:8], 'big')
        
        if packet_seq not in buffer:
            buffer[packet_seq] = [None] * total_packets

        buffer[packet_seq][packet_num] = payload

        if all(part is not None for part in buffer[packet_seq]):
            # Сборка пакетов
            frame_data = b''.join(buffer[packet_seq])
            frame = np.frombuffer(frame_data, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            if frame is not None:
                cv2.imshow('RESULT', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    s.server_close()

            del buffer[packet_seq]

if __name__ == "__main__":
    HOST, PORT = 'localhost', 50005
    
    
    clients = []
    buffer = {}
    
    with socketserver.UDPServer((HOST, PORT), UDPHandler) as s:
        s.serve_forever()

    