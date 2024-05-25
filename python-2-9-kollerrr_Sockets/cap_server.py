# переводит все в верхний регистр

import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

class CapHndaler(socketserver.StreamRequestHandler): # обрабатывабщий хендлер capitalise

    def handle(self) -> None:

        client = f'{self.client_address} on {threading.current_thread().getName()}' # текущий поток как объект и получение его имени
        print(f'Connected:{client}')

        while True:
            data = self.rfile.readline() # rfile -- reading

            if not data:
                break
            self.wfile.write(data.decode().upper().encode()) # произошло декодирование, перевод в верхний регистр и кодирование
        print(f'Closed: {client}')

with ThreadedTCPServer(('', 59898), CapHndaler) as server:
    print('Server is running...')
    server.serve_forever()