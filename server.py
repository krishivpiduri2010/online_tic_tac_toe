import _thread
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.0.103'
port = 5555

s.bind((server, port))

print('[SERVER_STARTED] Listening')
s.listen()
client_id=0


def threaded_client(client:socket.socket):
    global client_id
    client.send(str(client_id).encode())
    while True:
        try:
            pass
        except:
            break
    client.close()
    client_id-=1


while True:
    client,addr=s.accept()
    print(f'[NEW_CONNECTION] {addr} connected')
    _thread.start_new_thread(threaded_client,(client,))
