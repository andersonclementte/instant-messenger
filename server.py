import socket, threading, sys

FORMAT = 'utf-8'
HEADER = 64
MSG_SIZE = 2048
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!SAIR"

MSG_BUFFER = []
CLIENT_LIST = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def post_msg(msg):
    global MSG_BUFFER
    MSG_BUFFER.append(msg)
    for client in CLIENT_LIST:
        message = msg.encode(FORMAT)
        # msg_len = len(message)
        # send_len = str(msg_len).encode(FORMAT)
        # send_len += b' '*(HEADER - len(send_len))
        # client[0].send(send_len)
        #time.sleep(1)
        client[0].send(message)
    MSG_BUFFER.pop(0)


def handle_client(conn, addr):
    global MSG_BUFFER
    global CLIENT_LIST
    print(f'[NOVA CONEXÃO {addr} conectado]')
    connected = True

    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)

            if DISCONNECT_MESSAGE in msg:
                name = msg[5:]
                for client in CLIENT_LIST:
                    if conn == client[0]:
                        CLIENT_LIST.remove(client)
                post_msg(f"{name} saiu do chat!")
                connected = False



            print(f'[{addr}] {msg}') #printa no servidor
            post_msg(msg)
            #handle_msg(conn) #envia para os outros
            #conn.send("MSg received".encode(FORMAT)) #envia ao cliente
    conn.close()

def start():
    try:
        server.listen()
        print(f"[LISTENING] Endereço do servidor: {SERVER}")
        while True:
            conn, addr = server.accept()
            CLIENT_LIST.append((conn, addr))
            thread = threading.Thread(target=handle_client, args = (conn, addr))
            thread.start()
            print(f'[CONEXÕES ATIVAS] {threading.activeCount()-1}')
    except KeyboardInterrupt:
        server.close()
        sys.exit("\n[EXIT] Servidor encerrado")

print("[INICIANDO] Servidor iniciando...")
start()
