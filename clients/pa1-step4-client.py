# Step 4: File I/O Client (starter)
import socket

HOST = "127.0.0.1"
PORT = 50007

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

with open("in-proj.txt") as f:
    for line in f:
        msg = line.strip()  # keep as-is per assignment handout
        # TODO: send msg (+ "\n") to the server
        # TODO: receive the transformed reply from the server
        # decode it back to string
        print(f"sent={msg} recv={reply}")

c.close()
