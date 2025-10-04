import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('server socket created')

    s.bind((HOST, PORT))
    print(f'socket bound to {HOST}:{PORT}')

    s.listen()
    print('server listening for client')

    conn, addr = s.accept()
    print(f'accepted connection from {addr}')

    greeting = 'hello'.encode('utf-8')
    conn.sendall(greeting)
    print('sent greeting to client')