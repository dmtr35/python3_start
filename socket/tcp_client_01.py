import socket

# target_host = "www.google.com"
# target_port = 80
target_host = "127.0.0.1"
target_port = 9999

# создаем обьект сокета (F_INET - стандартные IPv4, STREAM - будет работать по TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключаем клиент
client.connect((target_host, target_port))

# отправляем данные
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# принимаем какие-нибудь данные
response = client.recv(4096)

print("res:", response.decode())
client.close()



