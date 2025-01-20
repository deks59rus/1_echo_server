import socket
import threading

def handle_client(data, addr):
    print(f"Received message from {addr}: {data.decode('utf-8')}")
    response = f"Server received: {data.decode('utf-8')}"
    sock.sendto(response.encode('utf-8'), addr)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 12345
sock.bind(('', port))
print(f"Chat server is running on port {port}")

clients = set()

while True:
    data, addr = sock.recvfrom(1024)
    if addr not in clients:
        clients.add(addr)
    threading.Thread(target=handle_client, args=(data, addr)).start()
