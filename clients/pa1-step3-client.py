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
    # TODO: send line (+ newline) to server
    # TODO: receive reply from server
    reply = "???"  # placeholder until implemented
    print(f"sent={line} recv={reply}")

c.close()
