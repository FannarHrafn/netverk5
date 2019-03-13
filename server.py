import socket, threading

class ClientThread(threading.Thread): # inheritar threading.Thread
    def __init__(self,clientAddress,clientsocket): # init fall tekur a moti address a client og socket hja client
        threading.Thread.__init__(self) # kallar a init fallid i threading.Thread klasanum
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress) # prentar ip address og port
    def run(self): #overwrite-ar run fallið í threading.Thread
        print ("Connection from : ", clientAddress) # prentar ip address og port
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048) #naer i data sem client sendir
            msg = data.decode() #decode-ar message
            if msg=='bye': #ef client sendir bye tha haettir serverinn i loopunni
              break
            print ("from client:", msg) # prentar message sem client senti
            self.csocket.send(bytes(msg,'UTF-8')) # sendir msg aftur til client
        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # byr til TCP/IP socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # socket.SO_REUSEADDR leyfir clientum ad nota sama address
server.bind((LOCALHOST, PORT)) # bindir socket við localhost og port
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept() # samthykkir connection fra client sem skilar nyju socket object og address a client
    newthread = ClientThread(clientAddress, clientsock) # byr til thread
    newthread.start() # keyrir thread
