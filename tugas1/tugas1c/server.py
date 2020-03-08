import sys
import socket
import threading
ports = [31000, 31001, 31002]
def socket_thread(port):
    # Handle connection from a client: Receive the data in small chunks and retransmit it
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('127.0.0.1', port)
    print(f"starting up on {server_address}")
    sock.bind(server_address)

    sock.listen(1)

    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    
    print(f"Handle connection from {client_address}")
    while True:
        data = connection.recv(32)
        print(f"[On Port {port}] received {data}")
        if data:
            print("[On Port {port}] sending back data")
            connection.sendall(data)
        else:
            pass
        break
        
    connection.close()

# Listen for incoming connections
threads = []
for port in ports:    
    t = threading.Thread(target=socket_thread, args=(port,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('Exit')