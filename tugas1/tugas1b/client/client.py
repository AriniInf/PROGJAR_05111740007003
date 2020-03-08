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
    message = 'progjar.txt'
    print(f"sending request")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    file = open("receive.txt","wb")
    
    while True:    
        if amount_received < amount_expected:  
            data = sock.recv(1024)        
            amount_received += len(data)
            file.write(data) 
            print("file received")   
        else:
            break
    file.close()
    
finally:
    print("closing")
    sock.close()
