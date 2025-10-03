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
    # TODO: send line (encode)
    # TODO: receive reply and print

c.close()
