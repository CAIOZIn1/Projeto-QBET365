from tkinter import messagebox
from tkinter import *
import pymysql
from tkinter import ttk

class Janela_principal:
    def _init_(self):
        '''
        Comando para executar todas as funções do
        início da janela
        :return:
        '''

        #Nomes das def's.
        self.janela()
        self. frames()
        self.continuar_janela()

    def janela(self):
        '''
        Valores e configurações da janela
        :return:
        '''

        # Front-end.
        self.janela = Tk()
        self.janela.geometry('900x600')
        self.janela.resizable(width=False, height=False)

    def frames(self):
        '''
        Frames da janela 1
        :return:
        '''

        # Frames da janela principal
        self.frame_inicial = Frame(self.janela, bg='white', width=900, height=600, background='black')
        self.frame_inicial.place(x=0, y=0)
        self.frame_inicial.propagate(False)

        self.frame_informações = Frame(self.frame_inicial, bg='white', width=600, height=400)
        self.frame_informações.place(x=150, y=100)
        self.frame_informações.propagate(False)

        self.frase_inicial = Label(self.frame_informações, text='O que deseja fazer? :)',
                                   font=("Comic Sans MS", 15), bg='white')
        self.frase_inicial.pack(padx=110, pady=180)

        self.botao_começar = ttk.Button(self.frame_informações, text='Cadastrar', style='Accent.TButton',
                                        command=lambda: Cadastrar.pagina_atual(self))
        self.botao_começar.place(x=100, y=260)

        self.botao_alterar = ttk.Button(self.frame_informações, text='Alterar', style='Accent.TButton',
                                        command=lambda: Alterar.pagina_atual(self))
        self.botao_alterar.place(x=200, y=260)

        self.botao_apagar = ttk.Button(self.frame_informações, text='Apagar', style='Accent.TButton',
                                        command=lambda: Apagar.pagina_atual(self))
        self.botao_apagar.place(x=300, y=260)

        self.botao_inspecionar = ttk.Button(self.frame_informações, text='Inspecionar', style='Accent.TButton',
                                        command=lambda: Inspecionar.pagina_atual(self))
        self.botao_inspecionar.place(x=400, y=260)

    def continuar_janela(self):
        '''
        Função para executar sempre a janela
        :return:
        '''

        # Essa def foi feita com o único intuito de continuar a janela =).
        self.janela.mainloop()

class Cadastrar:
    def pagina_atual(self):
        '''
        Essa def foi usada com intuito de executar as funções primordias para a
        execução do comando de cadastrar.
        :return:
        '''

        # Def que executa o comando no banco de dados
        def cadastrar():
            try:
                '''
                Serve para executar o comando dentro do banco de dados.
                :return: 
                '''

                self.resposta_entrada1 = self.entrada1.get().lower()
                self.resposta_entrada2 = self.entrada2.get().lower()
                self.resposta_entrada3 = self.entrada3.get().lower()
                self.resposta_entrada4 = self.entrada4.get().lower()

                self.conexao = pymysql.connect(
                host='localhost',
                user='root',
                passwd='sesisenai'
                )

                self.cursor = self.conexao.cursor()

                self.cursor.execute('create database if not exists caio;')
                self.cursor.execute('''use caio''')

                self.cursor.execute('''create table if not exists cadastro(
                ID int not null PRIMARY KEY AUTO_INCREMENT,
                nome varchar(20) not null unique,
                telefone1 char(11)not null,
                telefone2 char(11),
                telefone3 char(11))''')

                self.cursor.execute(f'''insert into cadastro (nome,telefone1, telefone2, telefone3) values ('{self.resposta_entrada1}','{self.resposta_entrada2}','{self.resposta_entrada3}', '{self.resposta_entrada4}')''')
                self.conexao.commit()

                messagebox.showinfo('Sucess', 'O indivíduo foi cadastrado com sucesso!')

                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')

            except:
                messagebox.showerror('Erro', 'Não foi possível realizar o cadastro =(')

        self.frame_inicial.destroy()

        # Frames de início
        self.frame_principal = Frame(self.janela, bg='white', width=900, height=600, background='black')
        self.frame_principal.place(x=0, y=0)
        self.frame_principal.propagate(False)

        self.frame_pagina_atual = Frame(self.frame_principal, bg='white', width=1000, height=80, background='white',
                            highlightbackground='red', highlightthickness=2)
        self.frame_pagina_atual.place(x=-40, y=40)
        self.frame_pagina_atual.propagate(False)

        self.frame_informação_das_defs = Frame(self.frame_principal, bg='white', width=800, height=360, background='white',
                            highlightbackground='red', highlightthickness=3)
        self.frame_informação_das_defs.place(x=50, y=190)
        self.frame_informação_das_defs.propagate(False)

        # Botões
        self.botao_cadastrar = ttk.Button(self.frame_informação_das_defs, text='Cadastrar', style='Accent.TButton',
                                          command=cadastrar)
        self.botao_cadastrar.place(x=370, y=316)

        # Frases
        self.cadastrar = Label(self.frame_pagina_atual, text='CADASTRAR', font='Arial 20', bg='white')
        self.cadastrar.pack(pady=20)

        self.nome = Label(self.frame_informação_das_defs, text='NOME:', bg='white')
        self.nome.place(x=390, y=10)

        self.telefone1 = Label(self.frame_informação_das_defs, text='Telefone 1:', bg='white')
        self.telefone1.place(x=380, y=90)

        self.telefone2 = Label(self.frame_informação_das_defs, text='Telefone 2:', bg='white')
        self.telefone2.place(x=380, y=170)

        self.telefone3 = Label(self.frame_informação_das_defs, text='Telefone 3:', bg='white')
        self.telefone3.place(x=380, y=240)

        # Entradas
        v1 = StringVar()
        self.entrada1 = ttk.Entry(self.frame_informação_das_defs, textvariable=v1)
        self.entrada1.place(x=160, y=40, width=500, height=30)

        v2 = StringVar()
        self.entrada2 = ttk.Entry(self.frame_informação_das_defs, textvariable=v2)
        self.entrada2.place(x=160, y=120, width=500, height=30)

        v3 = StringVar()
        self.entrada3 = ttk.Entry(self.frame_informação_das_defs, textvariable=v3)
        self.entrada3.place(x=160, y=200, width=500, height=30)

        v4 = StringVar()
        self.entrada4 = ttk.Entry(self.frame_informação_das_defs, textvariable=v4)
        self.entrada4.place(x=160, y=270, width=500, height=30)

        # Botão de voltar
        self.back_button = Button(self.frame_pagina_atual, text='⇦', border=2,
                                  command=lambda: Janela_principal.frames(self))
        self.back_button.place(x=60, y=20, width=40, height=40)

class Alterar:
    def pagina_atual(self):
        '''
        Essa def foi usada com intuito de executar as funções primordias para a execução do
        de alterar um dado no SGBD.
        :return:
        '''

        # Def para executar os comandos dentro do banco de dados
        def alterar():
            '''
            Comandos referentes a alteração em um banco de dados.
            :return:
            '''
            try:
                self.resposta_entrada1 = self.entrada1.get().lower()
                self.resposta_entrada2 = self.entrada2.get().lower()
                self.resposta_entrada3 = self.entrada3.get().lower()
                self.resposta_entrada4 = self.entrada4.get().lower()
                self.resposta_entrada5 = self.entrada5.get().lower()

                self.conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    passwd='sesisenai'
                )

                self.cursor = self.conexao.cursor()

                self.cursor.execute('create database if not exists caio;')
                self.cursor.execute('''use caio''')

                self.cursor.execute(f'''update cadastro set nome='{self.resposta_entrada1}', telefone1='{self.resposta_entrada2}', telefone2='{self.resposta_entrada3}', telefone3='{self.resposta_entrada4}' where nome='{self.resposta_entrada5}' ''')
                self.conexao.commit()

                messagebox.showinfo('Sucess', 'Os dados do perfil referente foram atualizados!')
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')
                v5.set('')
            except:
                messagebox.showerror('Erro', 'Não foi possível realizar a alteração =(')

        self.frame_inicial.destroy()

        # Frames iniciais

        self.frame_principal = Frame(self.janela, bg='white', width=900, height=600, background='black')
        self.frame_principal.place(x=0, y=0)
        self.frame_principal.propagate(False)

        self.frame_pagina_atual = Frame(self.frame_principal, bg='white', width=1000, height=80, background='white',
                            highlightbackground='red', highlightthickness=2)
        self.frame_pagina_atual.place(x=-40, y=40)
        self.frame_pagina_atual.propagate(False)

        self.frame_informação_das_defs = Frame(self.frame_principal, bg='white', width=800, height=360, background='white',
                            highlightbackground='red', highlightthickness=3)
        self.frame_informação_das_defs.place(x=50, y=190)
        self.frame_informação_das_defs.propagate(False)

        # Labels
        self.cadastrar = Label(self.frame_pagina_atual, text='ALTERAR', font='Arial 20', bg='white')
        self.cadastrar.pack(pady=20)

        self.nome = Label(self.frame_informação_das_defs, text='NOME:', bg='white')
        self.nome.place(x=390, y=5)

        self.telefone1 = Label(self.frame_informação_das_defs, text='Telefone 1:', bg='white')
        self.telefone1.place(x=380, y=70)

        self.telefone2 = Label(self.frame_informação_das_defs, text='Telefone 2:', bg='white')
        self.telefone2.place(x=380, y=140)

        self.telefone3 = Label(self.frame_informação_das_defs, text='Telefone 3:', bg='white')
        self.telefone3.place(x=380, y=210)

        self.telefone3 = Label(self.frame_informação_das_defs, text='alterar qual nome:', bg='white')
        self.telefone3.place(x=361, y=270)

        # Entradas

        v1 = StringVar()
        self.entrada1 = ttk.Entry(self.frame_informação_das_defs, textvariable=v1)
        self.entrada1.place(x=160, y=30, width=500, height=30)

        v2 = StringVar()
        self.entrada2 = ttk.Entry(self.frame_informação_das_defs, textvariable=v2)
        self.entrada2.place(x=160, y=100, width=500, height=30)

        v3 = StringVar()
        self.entrada3 = ttk.Entry(self.frame_informação_das_defs, textvariable=v3)
        self.entrada3.place(x=160, y=170, width=500, height=30)

        v4 = StringVar()
        self.entrada4 = ttk.Entry(self.frame_informação_das_defs, textvariable=v4)
        self.entrada4.place(x=160, y=235, width=500, height=30)

        v5 = StringVar()
        self.entrada5 = ttk.Entry(self.frame_informação_das_defs, textvariable=v5)
        self.entrada5.place(x=160, y=300, width=500, height=30)

        # Botão

        self.botao_alterar = ttk.Button(self.frame_informação_das_defs, text='Alterar',
                                        style='Accent.TButton',command=alterar)
        self.botao_alterar.place(x=700, y=303)

        # Botão de voltar

        self.back_button = Button(self.frame_pagina_atual, text='⇦', border=2,
                                  command=lambda: Janela_principal.frames(self))
        self.back_button.place(x=60, y=20, width=40, height=40)

class Apagar:
    def pagina_atual(self):
        '''
        Essa def foi usada com intuito de executar as funções primordias para a execução do comando de apagar.
        :return:
        '''

        # Def com a função de apagar algum dado dentro do banco de dados
        def apagar():
            '''
            Esta executa os comandos feitos dentro do banco de dados, no caso, comando de apagar.
            :return:
            '''
            try:
                self.resposta_entrada6 = self.entrada6.get().lower()

                self.conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    passwd='sesisenai'
                )

                self.cursor = self.conexao.cursor()

                self.cursor.execute('create database if not exists caio;')
                self.cursor.execute('''use caio''')

                self.cursor.execute(f'''delete from cadastro where nome='{self.resposta_entrada6}' ''')
                self.conexao.commit()

                messagebox.showinfo('Sucess', 'Os dados do indivíduo foram apagados!')

                v1.set('')
            except:
                messagebox.showerror('Erro', 'Infelizmente não foi possível apagar o dado =(')

        self.frame_inicial.destroy()

        # Frames inicias

        self.frame_principal = Frame(self.janela, bg='white', width=900, height=600, background='black')
        self.frame_principal.place(x=0, y=0)
        self.frame_principal.propagate(False)

        self.frame_pagina_atual = Frame(self.frame_principal, bg='white', width=1000, height=80, background='white',
                            highlightbackground='red', highlightthickness=2)
        self.frame_pagina_atual.place(x=-40, y=40)
        self.frame_pagina_atual.propagate(False)

        self.frame_informação_das_defs = Frame(self.frame_principal, bg='white', width=800, height=360,
                            background='white',highlightbackground='red', highlightthickness=3)
        self.frame_informação_das_defs.place(x=50, y=190)
        self.frame_informação_das_defs.propagate(False)

        self.cadastrar = Label(self.frame_pagina_atual, text='APAGAR', font='Arial 20', bg='white')
        self.cadastrar.pack(pady=20)

        self.nome = Label(self.frame_informação_das_defs, text='Apagar qual nome:', bg='white')
        self.nome.place(x=360, y=20)

        v1 = StringVar()
        self.entrada6 = ttk.Entry(self.frame_informação_das_defs, textvariable=v1)
        self.entrada6.place(x=160, y=60, width=500, height=30)

        self.botao_telefone= ttk.Button(self.frame_informação_das_defs, text='Apagar', style='Accent.TButton',
                                        command=apagar)
        self.botao_telefone.place(x=370, y=316)

        # Botão de voltar
        self.back_button = Button(self.frame_pagina_atual, text='⇦', border=2,
                                  command=lambda: Janela_principal.frames(self))
        self.back_button.place(x=60, y=20, width=40, height=40)

class Inspecionar:
    def pagina_atual(self):
        '''
        Essa def foi usada com intuito de executar as funções primordias para a execução do comando de inpecionar.  No caso, esta mostrará os dados
        do banco de dados.
        :return:
        '''

        self.conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd=''
        )

        self.cursor = self.conexao.cursor()

        self.cursor.execute('create database if not exists caio;')
        self.cursor.execute('''use caio''')

        self.cursor.execute('''create table if not exists cadastro(
                    ID int not null PRIMARY KEY AUTO_INCREMENT,
                    nome varchar(20) not null unique,
                    telefone1 char(11)not null,
                    telefone2 char(11),
                    telefone3 char(11))''')

        self.cursor.execute(f'''select * from cadastro''')
        dados = self.cursor.fetchall()

        self.conexao.commit()

        self.frame_inicial.destroy()

        # FRAMES INICIAIS
        self.frame_principal = Frame(self.janela, bg='white', width=900, height=600,
                                     background='black')
        self.frame_principal.place(x=0, y=0)

        self.frame_pagina_atual = Frame(self.frame_principal, bg='white', width=1000, height=80, background='white',
                                        highlightbackground='red', highlightthickness=2)
        self.frame_pagina_atual.place(x=-40, y=40)
        self.frame_pagina_atual.propagate(False)

        self.frame_informação_das_defs = Frame(self.frame_principal, bg='white', width=800, height=360,
                                               background='white', highlightbackground='red', highlightthickness=3)
        self.frame_informação_das_defs.propagate(False)
        self.frame_informação_das_defs.place(x=50, y=190)

        self.inspecionar = Label(self.frame_pagina_atual, text='INSPECIONAR', font='Arial 20', bg='white')
        self.inspecionar.pack(pady=20)

        # Botão de voltar
        self.back_button = Button(self.frame_pagina_atual, text='⇦', border=2,
                                  command=lambda: Janela_principal.frames(self))
        self.back_button.place(x=60, y=20, width=40, height=40)

        # Treeview
        self.tabela = ttk.Treeview(self.frame_informação_das_defs, height=360)

        self.tabela['columns'] = ('Name', 'Telefone 1', 'Telefone 2', 'Telefone 3')

        self.tabela.column('#0', anchor=W, width=160)
        self.tabela.column('Name', anchor=W, width=160)
        self.tabela.column('Telefone 1', anchor=W, width=160)
        self.tabela.column('Telefone 2', anchor=W, width=160)
        self.tabela.column('Telefone 3', anchor=W, width=160)


        self.tabela.heading('#0', text='ID', anchor=W)
        self.tabela.heading('Name', text='Nome', anchor=W)
        self.tabela.heading('Telefone 1', text='Telefone 1', anchor=W)
        self.tabela.heading('Telefone 2', text='Telefone 2', anchor=W)
        self.tabela.heading('Telefone 3', text='Telefone 3', anchor=W)
        x = 0
        for i in dados:

            self.tabela.insert(parent='',  index='end', iid=x, text=f'{i[0]}',
                                values=(f'{i[1]}', f'{i[2]}', f'{i[3]}', f'{i[4]}'))
            x = + 1

        self.tabela.pack()

Janela_principal()
