import socket
import _thread

messageBuffer = " "

def start_server(port):
    IP = '127.0.0.1'
    PORT = port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen()
    return s

def connect_to_next_node(nextPort):
    print("Pritisni ""ENTER"" za start!")
    input()
    ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ns.connect(('127.0.0.1', nextPort))
    return ns

def send_messages(ns):
    global messageBuffer
    while True:
        messageBuffer = input("Enter a message: ")
        ns.sendall(str.encode(messageBuffer))

def pass_messages(ps, ns):
    #previous socket, next socket
    global messageBuffer
    while True:
        Message = ps.recv(1024).decode()
        if Message == messageBuffer:
            print("Stara poruka primljena, END!")
        else:
            print(Message)
            ns.sendall(str.encode(Message))

port = int(input("Unesi svoj port: "))
nextPort = int(input("Unesi port sljedeceg: "))
s = start_server(port)
ns = connect_to_next_node(nextPort)
_thread.start_new_thread(send_messages,(ns, ))

while True:
    ps, adr = s.accept()
    pass_messages(ps, ns)
    

    
    
   