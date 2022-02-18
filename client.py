import socket, threading, sys

FORMAT = 'utf-8'
HEADER = 64
MSG_SIZE = 2048
PORT = 5050
DISCONNECT_MESSAGE = "!SAIR"
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = input("Digite o endereço do servidor: ")
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def listen_msg():
    try:
        msg = client.recv(MSG_SIZE).decode(FORMAT)
        print(msg)
    #try:
    #msg_header = client.recv(HEADER).decode(FORMAT)
    # if client.recv(HEADER).decode(FORMAT):
    #     msg_len = client.recv(HEADER).decode(FORMAT)
    #     msg_len = int(msg_len.strip())
    #     msg = client.recv(msg_len).decode(FORMAT)
    #     # if type(msg_len) == str:
    #     #     msg_len = len(msg_len)
    #     #     msg = client.recv(msg_len).decode(FORMAT)
    #     # if type(msg_len) == bytes:
    #     #     msg_len = msg_len.decode(FORMAT)
    #     #     msg = client.recv(msg_len).decode(FORMAT)
    #     # if type(msg_len) == int:
    #     #     msg_len = int(msg_len)
    #     #     msg = client.recv(msg_len).decode(FORMAT)
    #     print(msg)
    # except ValueError:
    #     sys.exit()
    except ConnectionResetError:
            sys.exit("Conexão encerrada")


def send(msg):

    message = msg.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    #print(client.recv(2048).decode(FORMAT))
    
# send("HELLO")
# send(DISCONNECT_MESSAGE)

def connect():
    name = input('Qual seu nome? ')
    print(f"Bem vindo, {name}")
    try:
        while True:
            # if client.recv(2048):
            #     print("msg recebida")
            #     print(client.recv(2048).decode(FORMAT))
            thread = threading.Thread(target=listen_msg)
            thread.start()
            msg = input(">> ")
            #input()
            
            if len(msg) > 0 and msg != '\n':
                send(f"{name} disse: {msg}")

            if msg == DISCONNECT_MESSAGE:
                print(f"Tchau {name}!")
                send(msg+name)
                break
    except ConnectionResetError:
        sys.exit("Conexão encerrada")
        

        
        #input()

connect()