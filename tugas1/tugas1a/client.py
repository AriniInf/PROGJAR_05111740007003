import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    file = open("progjar.txt","rb")
    data = file.read(1024)
    print("sending file....")
    
    while True:
        if not data:
            break
        sock.send(data)
    print("file sent")
    file.close()
    
finally:
    print("closing")
    sock.close()
