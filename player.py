import sys
import socket, select, string, sys
import thread
import time ,random

HOST = (sys.argv[1])
PORT = int(sys.argv[2])


dest = (HOST, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(dest)
class Mensagem():
    def __init__(self):
        self.msg = 0
        # thread.start_new_thread(self.recebe, tuple([1,2]))

    def envia(self,msg):
        #thread.start_new_thread(m.recebe, tuple([1,2]))
        #self.msg = raw_input('digite\n')
        self.msg = msg
        if int(msg) < 5:
            tcp.send (str(self.msg))
        else:
            tcp.send (str(self.msg))

    def recebe(self):
        while True:
            self.msg = tcp.recv(64)
            if self.msg:
                return (self.msg)


m = Mensagem()
while True:
    m.msg = tcp.recv(2)
    if m.msg == "-1":
        break

time.sleep(2)
m.envia(random.randrange(10))

time.sleep(2)
m.envia(random.randrange(10))

time.sleep(2)
m.envia(random.randrange(10))

time.sleep(1)
m.envia(-1)

time.sleep(1)
a = (1222+random.randrange(10))
print a,"______"
m.envia(a)
m.msg = tcp.recv(64)
b = m.recebe()
print a,"*******",b
if a > int(b):
    print "venci"
if a < int(b):
    print "nao venci"
if a == int(b):
    print "empate"
