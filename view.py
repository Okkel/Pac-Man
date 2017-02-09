# -*- coding: utf-8 -*-
#
import sys
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

# ini = Iniciar()
#Criando a Classe do Programa
class InterfaceRedes():
    def __init__(self):


        self.box = Gtk.HBox(False, 0)
        self.box.set_border_width(2)

        self.window = Gtk.Window()
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())
        self.window.set_title("Conectar ao servidor do PacMan")
        self.window.set_border_width(10)

        self.label_ip = Gtk.Label("IP")
        self.ip_entry = Gtk.Entry()
        self.ip_entry.set_text("localhost")

        self.label_porta = Gtk.Label("Porta")
        self.porta_entry = Gtk.Entry()

        self.button_conectar = Gtk.Button("Conectar")
        self.button_conectar.connect("clicked", self.conectar)


        self.box.add(self.label_ip)
        self.box.add(self.ip_entry)

        self.box.add(self.label_porta)
        self.box.add(self.porta_entry)

        self.box.add(self.button_conectar)

        self.window.add(self.box)

        self.window.show_all()
        #self.builder = Gtk.Builder()
        #self.builder.add_from_file("InterfaceRedes.glade")

        #self.ip = self.porta = 0
        #self.window = self.builder.get_object("window1")
        #self.window.set_title("Conectar PacMan")
        #self.entryIP = self.builder.get_object("entryIP")
        #self.entryPorta = self.builder.get_object("entryPorta")
        #self.btnConectar = self.builder.get_object("Btconectar")

        #self.window.show()

#        self.btnConectar.connect_signals('clicked',self.conectar)
        #self.builder.connect_signals({"Gtk_main_quit": Gtk.main_quit,
                            #Sinal da janela principal, conectada a função
                            #do Gtk que fecha o  programa
        #                   "on_Btconecatar_clicked": self.conectar,#quando o botao login e clicado chama a funcao login
        #                        })

        Gtk.main()
# escrever num arquivo ip porta
    def conectar(self, widget):
        self.ip = self.ip_entry.get_text()
        self.porta  = self.porta_entry.get_text()

        self.window.hide()
        Gtk.main_quit()
#        self.window.destroy()
#        self.ip = ip
#        self.porta = porta
        #print 'ip/porta',self.ip,'/',self.porta



        # ini.run(ip,porta)
        # self.window.hide()
        #arq = open('connect.txt', 'w')
        #texto =(ip +' ' +porta)
        #arq.write(texto)
        #arq.close()
        #sys.exit(0)

        # arq = open('/tmp/lista.txt', 'r')
        # texto = arq.read()
        # print(texto)
        # arq.close()
        return
