import socket, threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!SAIR"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def listen_msg():
    msg_len = client.recv(HEADER).decode(FORMAT)
    print(msg_len)
    if msg_len:
        msg_len = int(msg_len)
        msg = client.recv(msg_len).decode(FORMAT)
        print(msg)

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

        
        #input()

connect()