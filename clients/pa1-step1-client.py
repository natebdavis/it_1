# Step 1: Minimal Client (starter)
import socket

HOST = "127.0.0.1"
PORT = 50007

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: connect to (HOST, PORT)
print("local endpoint:", c.getsockname())
print("server endpoint:", c.getpeername())

# TODO: receive up to 100 bytes, decode, and print

c.close()
