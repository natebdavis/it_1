# Step 2: Echo Loop Client (starter)
import socket

HOST = "127.0.0.1"
PORT = 50007

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

while True:
    line = input("Enter a line (or QUIT): ")
    if line == "QUIT":
        break
    # send line (encode)
    c.sendall(line.encode())
    # receive reply and print
    reply = c.recv(100).decode()
    print(reply)

c.close()
