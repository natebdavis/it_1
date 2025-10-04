# Step 3: Protocol + Transform Server (starter)
import socket

PORT = 50007

def transform(s: str) -> str:
    # reverse string and swap case
    return s[::-1].swapcase()

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
    text = data.decode()
    reply = transform(text)
    # send reply + newline
    conn.sendall(f'{reply}\n'.encode())

conn.close()
s.close()
