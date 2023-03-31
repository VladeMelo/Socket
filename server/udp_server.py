import socket

IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 1024
PORT = 9999

def decode(str):
    return str.decode('utf-8')

def encode(str):
    return str.encode('utf-8')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65507)

server.bind((IP_ADDRESS, PORT))

# message, address = server.recvfrom(BUFFER_SIZE)
# print(decode(message))
# server.sendto(encode('Hello Client!'), address)


# espera por dados vindos do cliente
while True:
    # recebe os dados e o endereço do cliente
    data, address = server.recvfrom(1024)
    
    with open("server/teste2.txt", "wb") as f:
        f.write(data)
        
    print(f"Arquivo recebido do cliente {address[0]}:{address[1]} e salvo como 'teste2'")
    
    with open("server/teste2.txt", "rb") as f:
        data = f.read()
        
    server.sendto(data, address)
    print(f"Arquivo enviado de volta para o cliente {address[0]}:{address[1]}")