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
    except ConnectionResetError:
            sys.exit("Conexão encerrada")


def send(msg):

    message = msg.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)


def connect():
    name = input('Qual seu nome? ')
    print(f"Bem vindo, {name}")
    try:
        while True:
            thread = threading.Thread(target=listen_msg)
            thread.start()
            msg = input(">> ")

            if msg == DISCONNECT_MESSAGE:
                print(f"Tchau {name}!")
                send(msg+name)
                break
            
            elif len(msg) > 0 and msg != '\n':
                send(f"{name} disse: {msg}")

            
    except ConnectionResetError:
        sys.exit("Conexão encerrada")

    except KeyboardInterrupt:
        send(DISCONNECT_MESSAGE)
        sys.exit("\nConexão interrompida")


connect()