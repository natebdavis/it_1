# Step 1: Minimal Server (starter)
import socket

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# allow quick restarts with SO_REUSEADDR
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind to all interfaces on PORT
s.bind((HOST, PORT))
# listen with backlog 1
s.listen(1)
print("[S] listening on", s.getsockname())

conn, addr = s.accept()
print("[S] accepted connection from", addr)
# send greeting to client
conn.sendall(b'hello from the server')

conn.close()
s.close()
