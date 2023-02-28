import socket

socket_device = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_STREAM
)
port = 12346
host = '127.0.0.1'
socket_device.connect((host,port))
socket_device.setblocking(0)
# 1 = blocking
# 0 = non-blocking
data_send_to_server = b"hi server !"
try:
    socket_device.send(data_send_to_server)
except Exception as e:
    print("error : {}".format(e))
