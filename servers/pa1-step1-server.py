# Step 1: Minimal Server (starter)
import socket

PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: allow quick restarts with SO_REUSEADDR
# TODO: bind to all interfaces on PORT
# TODO: listen with backlog 1
print("[S] listening on", s.getsockname())

conn, addr = s.accept()
print("[S] accepted connection from", addr)
# TODO: send greeting to client

conn.close()
s.close()
