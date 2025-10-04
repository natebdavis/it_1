# Step 4: File I/O Server (starter)
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

out = open("out-proj.txt", "w")

while True:
    data = conn.recv(1024)
    if not data:
        break
    text = data.decode().strip()  # incoming line (newline removed)
    reply = transform(text)
    out.write(reply + "\n")
    # send reply back to client (with newline)
    conn.sendall(f'{reply}\n'.encode())

out.close()
conn.close()
s.close()
