import socket
socket_server = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_STREAM
)
host = '127.0.0.1'
port = 12346
socket_server.bind((host,port))
socket_server.listen(10)
while True:
    conn,ipaddress = socket_server.accept()
    data = conn.recv(1024).decode()

    socket_server.close()
        
