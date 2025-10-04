import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('client socket created')

    s.connect((HOST, PORT))
    print(f'connected to server at {HOST}:{PORT}')

    data = s.recv(1024)
    print('recieved data from server')

    greeting = data.decode('utf-8')
    print(f'server sent {greeting}')