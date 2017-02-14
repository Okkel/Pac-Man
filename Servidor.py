import socket, select , sys
import os
import thread

PORT = int(sys.argv[1])

HOST = ''              # Endereco IP do Servidor
PORT = PORT           # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(2)

class Conexao():
    # def __init__(self,ip,cliente):
        # self.ip = ip
        # self.cliente = cliente

    def conectado(self, con, cliente ,user):
        print 'Conectado por', cliente


        print 'Aguardando conexao com o adversario'
        while True:
            if len(CONNECTION_LIST) > 1 :

                k = CONNECTION_LIST.keys()
                for key in k:
                    if(key != user):
                        CONNECTION_LIST[key].sendall("-1")
                break
        try:
            while True:
                msg = CONNECTION_LIST[user].recv(2)
                # if int(msg) > 0 and int(msg)  < 5 :
                if msg != "-1" :
                    # con.send('recebida')
                    print cliente,'diz \n',msg

                    k = CONNECTION_LIST.keys()

                    for key in k:
                        if(key != user):
                            CONNECTION_LIST[key].sendall(msg)

                elif msg == "-1":
                    for key in k:
                        # print 'chegou akiiiiii'
                        if(key != user):
                            #print 'Player ',user,' Placar: ',msg
                            CONNECTION_LIST[key].sendall("-1")
                    msg = CONNECTION_LIST[user].recv(64)
                    if msg:
                        #self.placar(user,int(msg))
                        #print p1,'---*******-----'
                        #time.sleep(1)
                        # print 'chegou aki'
                        k = CONNECTION_LIST.keys()
                        for key in k:
                            # print 'chegou akiiiiii'
                            if(key != user):
                                print 'Player ',user,' Placar: ',msg
                                CONNECTION_LIST[key].sendall(msg)
                        # sys.exit()
                        break
        except:
            if msg == '-1':
                print "fail"
                sys.exit()
            else:
                print msg,'.....'
                # sys.exit()
                sys.exit()
        # print 'Placar: ',msg

c = Conexao()
user = 0

CONNECTION_LIST = {}
# CONNECTION_LIST.append(tcp)
while True:

    con, cliente = tcp.accept()
    CONNECTION_LIST[user] = con
    thread.start_new_thread(c.conectado, tuple([con, cliente ,user]))
    user+=1


tcp.close()
