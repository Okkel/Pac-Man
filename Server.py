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


        print 'Aguardando conexao adversario'
        while True:
            if len(CONNECTION_LIST) > 1 :

                k = CONNECTION_LIST.keys()
                for key in k:
                    if(key != user):
                        CONNECTION_LIST[key].sendall("-1")
                break
        while True:
            msg = CONNECTION_LIST[user].recv(64)
            try:
                if msg <>'-1' and int(msg)  < 5 :
                    # con.send('recebida')
                    print cliente,'diz \n',msg

                    k = CONNECTION_LIST.keys()

                    for key in k:
                        if(key != user):
                            CONNECTION_LIST[key].sendall(msg)

                else:
                    #fazer algo pra receber os 2 placares
                    msg = CONNECTION_LIST[user].recv(64)
                    print 'Placar: ',msg
                    print cliente,'Saiu'
                    k = CONNECTION_LIST.keys()
                    for key in k:
                        if(key != user):
                            # CONNECTION_LIST[key].sendall(str(cliente)+msg)
                            CONNECTION_LIST[key].sendall(msg)
                            # CONNECTION_LIST.pop(user)
                            # CONNECTION_LIST[user].close()
                            # con.close()
                            # thread.exit()
                            # print 'finalizada'
            except:
                    if msg == '-1':
                        print "fail"
                        break
                    else:
                        print '.....'
                    break
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
