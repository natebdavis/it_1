# Step 3: Protocol + Transform Client (starter)
import socket

HOST = "127.0.0.1"
PORT = 50007

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

while True:
    line = input("Enter a line (or QUIT): ")
    if line == "QUIT":
        break
    # send line (+ newline) to server
    c.sendall(f'{line}\n'.encode())
    # receive reply from server
    reply = c.recv(100).decode()
    print(f"sent={line} recv={reply}")

c.close()
