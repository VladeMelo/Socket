import socket

SERVER_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 1024
PORT = 9999

def decode(str):
    return str.decode('utf-8')

def encode(str):
    return str.encode('utf-8')

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# client.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65507)

# client.sendto(encode('Hello Server!'), (SERVER_ADDRESS, PORT))
# print(decode(client.recvfrom(BUFFER_SIZE)[0]))

with open("client/teste.txt", "rb") as f:
    data = f.read()

client.sendto(data, (SERVER_ADDRESS, PORT))

print(f"Arquivo enviado para o servidor {SERVER_ADDRESS}:{PORT}")

data, address = client.recvfrom(BUFFER_SIZE)

with open("client/teste2.txt", "wb") as f:
    f.write(data)

print("Arquivo recebido de volta do servidor e salvo")

client.close()