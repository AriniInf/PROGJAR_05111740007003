import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)


while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()

    print(f"connection from {client_address}")
    file = open("recv.txt","wb")
   
    # Receive the data in small chunks and retransmit it
    amount_received = 0
    while True:
        data = connection.recv(1024)
        amount_received += len(data)
        print("receiving file....")
        #print(f"{data}")
        if data:
            file.write(data)
        else: break

    file.close()
    print('Successfully get the file')
    # Clean up the connection
    connection.close()
