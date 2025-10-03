# Step 2: Echo Loop Server (starter)
import socket

PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", PORT))
s.listen(1)
print("[S] listening on", s.getsockname())

conn, addr = s.accept()
print("[S] accepted connection from", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    # TODO: echo it back with conn.sendall()

conn.close()
s.close()
