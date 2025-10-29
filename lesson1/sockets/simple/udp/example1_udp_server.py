import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 6666))

result = sock.recv(4096)
print(result.decode())

sock.close()
