# Step 1: Minimal Client (starter)
import socket

HOST = "127.0.0.1"
PORT = 50007

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to (HOST, PORT)
c.connect((HOST, PORT))
print("local endpoint:", c.getsockname())
print("server endpoint:", c.getpeername())

# receive up to 100 bytes, decode, and print
greeting = c.recv(100).decode()
print(greeting)

c.close()
