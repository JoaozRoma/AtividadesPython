from tkinter import *
import mysql.connector
from mysql.connector import Error


main = Tk()

class Func():
    def Conexão(self):
        try:
            global conn
            self.conn = mysql.connector.connect(host='localhost', database='projetosa', user='root', password='')
        except Error as e:
            print("Erro de conexão", e)
    def Login(self):
        self.user = self.lb_codigo_entry.get()
        self.senha = self.lb_codigo_entry2.get()
        self.validar = False
        if not (self.user == '' or self.senha ==''):
            try:
                self.Conexão()
                self.cursor = self.conn.cursor()
                self.cursor.execute('select * from db_user')
                self.records = self.cursor.fetchall()
                for i in self.records:
                    if self.user in i and self.senha in i:
                        self.validar = True
                        return i[3]
                if self.validar == False:
                    print("id nao encontrado")
            except Error as e:
                print("Falha ao login : ", e)
            finally:
                if (self.conn.is_connected()):
                    print("Encerrando")
                    self.conn.close()
                    self.cursor.close()









class App(Func):
    def __init__(self):
        self.Conexão()
        self.main = main
        self.tela()
        self.frames_tela()
        self.labels()
        self.entry()
        self.widgets_frame1()
        self.main.mainloop()
    def tela(self):
        self.main.title("Login")
        self.main.configure(background='#081834')
        self.main.geometry("700x500")
        self.main.resizable(True,True)
        self.main.maxsize(width=900,height=700)
        self.main.minsize(width=400,height=300)
    def frames_tela(self):
        self.frames_tela_1 = Frame(self.main, bd=4, bg='#31343A',
                                   highlightbackground='#61656B', highlightthickness=2)
        self.frames_tela_1.place(relx=0.02,rely=0.02, relwidth=0.96,relheight=0.46)
    def widgets_frame1(self):
        self.bt_telacrud = Button(self.frames_tela_1,text="Logar",command=self.Login)
        self.bt_telacrud.place(relx=0.45,rely=0.65,relwidth=0.10,relheight=0.15)
    def labels(self):
        self.lb_codigo = Label(self.frames_tela_1,text='Nome : ')
        self.lb_codigo.place(relx=0.15,rely=0.20)
        self.lb_codigo2 = Label(self.frames_tela_1, text='Senha : ')
        self.lb_codigo2.place(relx=0.65, rely=0.20)
    def entry(self):
        self.lb_codigo_entry = Entry(self.frames_tela_1)
        self.lb_codigo_entry.place(relx=0.15,rely=0.30)
        self.lb_codigo_entry2 = Entry(self.frames_tela_1)
        self.lb_codigo_entry2.place(relx=0.65, rely=0.30)


App()