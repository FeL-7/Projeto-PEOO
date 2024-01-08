from time import sleep
from tkinter import *
from tkinter import font
from tkinter import colorchooser
from PIL import ImageTk, Image
import sqlite3
import pickle


"""Projeto finalizado"""


"""
claro = "#f5f7fc"
escuro = "#232833"
"""

cores_tema = ["#f5f7fc", "#232833"]

dict_cores = {"corPadrao": cores_tema[0], "lilas": "#746fff", "roxo": "#5e5bc9", "verde": "#00c6ab", "fgEntry": "#000000", "vermelho": "#eb0626", "laranja": "#eeaa74"}

class App:
    def __init__(self):

        print("INICIANDO APLICAÇÃO EM:")
        for i in range (3, 0, -1):
            print(i)
            sleep(1)

        self.janela = Tk()
        self.janela.title("Gerson Pinturas")
        self.janela.geometry("1200x670")
        self.janela.configure(bg=dict_cores["corPadrao"])
        self.janela.resizable(width=False, height=False)
        
        self.icone = PhotoImage(file="imagens\icone.png")
        self.janela.iconphoto(False, self.icone)

        self.temaAtual = "claro"

        self.modoAtual = ""

        self.saldo = 0.00
        
        # Certifique-se de que as fontes estão instaladas

        try:

            self.fonte1 = font.Font(family="Sora", size=16, weight="normal", slant="roman", underline=False)

            self.fonte2 = font.Font(family="Jost", size=16, weight="normal", slant="roman", underline=False)

            self.fonte3 = font.Font(family="Jost", size=12, weight="normal", slant="roman", underline=False)

        except TclError:
            print("Fontes não instaladas")

        try:

            self.conexao = sqlite3.connect("estoqueDeTintas.db")
            self.sql = self.conexao.cursor()

            self.sql.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cores';")
            self.tabela = self.sql.fetchone()

            if not self.tabela:
                self.sql.execute("CREATE TABLE cores (nome, hexcode)")
                self.conexao.commit()


        except ConnectionError:
            print("Ocorreu um erro durante a conexão")


        # BARRA LATERAL

        self.barraLateral = Frame(self.janela, 
                                   width=260,
                                   height=670,
                                   bg=dict_cores["roxo"])
        self.barraLateral.place(x=0, y=0)

        try:

            self.img_perfilOriginal = Image.open("imagens\perfil.jpg")
            self.img_perfilAlterada = self.img_perfilOriginal.resize((150, 170))
            self.img_perfil = ImageTk.PhotoImage(self.img_perfilAlterada)

        except FileNotFoundError:
            print("Arquivo não encontrado. Por favor, verifique o caminho inserido.")

        self.icone_perfil = Label(self.barraLateral,
                                  image=self.img_perfil)
        self.icone_perfil.place(x=50, y=50)

        self.nome_usuario = Label(self.barraLateral,
                                  text="Sr. Gerson",
                                  bg=dict_cores["roxo"],
                                  fg=cores_tema[0],
                                  font=self.fonte1)
        self.nome_usuario.place(x=70, y=230)
        
        self.btn_modoTintas = Button(self.barraLateral,
                                     bg=dict_cores["roxo"],
                                     fg=cores_tema[0],
                                     text="Gerenciar Tintas",
                                     font=self.fonte2,
                                     borderwidth=0,
                                     command=self.ativarModoTintas)
        self.btn_modoTintas.place(x=55, y=320)

        self.btn_modoFinanceiro = Button(self.barraLateral,
                                        bg=dict_cores["roxo"],
                                        fg=cores_tema[0],
                                        text="Controle Financeiro",
                                        font=self.fonte2,
                                        borderwidth=0,
                                        command=self.ativarModoFinanceiro)
        self.btn_modoFinanceiro.place(x=45, y=380)

        try:

            self.img_trocarTema = PhotoImage(file="imagens\mudar_tema.png").subsample(12)

        except FileNotFoundError:
            print("Arquivo não encontrado. Por favor, verifique o caminho inserido.")

        self.btn_trocarTema = Button(self.barraLateral,
                                     bg=dict_cores["roxo"],
                                     fg=cores_tema[0],
                                     borderwidth=0,
                                     image=self.img_trocarTema,
                                     command=self.mudarTema)
        self.btn_trocarTema.place(x=20, y=600)


        #CONTEÚDO PRINCIPAL

        self.mainContainer = Frame(self.janela,
                                   width=940,
                                   height=670,
                                   bg=dict_cores["corPadrao"]
                                   )
        self.mainContainer.place(x=260, y=0)

        try:
            self.background_img = ImageTk.PhotoImage(Image.open("imagens\img-background.jpg"))
            self.background = Label(self.mainContainer,
                                    width=940,
                                    height=670,
                                    bg=dict_cores["corPadrao"],
                                    image=self.background_img
                                    )
            self.background.place(x=-3, y=-1)
        except FileNotFoundError:
            print("Arquivo não encontrado. Por favor, verifique o caminho inserido.")
        

        # RODAPÉ

        self.rodape = Frame(self.janela,
                            width=940,
                            height=40,
                            bg=dict_cores["lilas"])
        self.rodape.place(x=260,y=630)


        # AO ENCERRAR FECHAR A JANELA
        self.janela.protocol("WM_DELETE_WINDOW", self.agradecimento)

        self.janela.mainloop()

    # MÉTODOS ABAIXO

    # MÉTODOS PARA CRIAÇÃO DE TELAS (MODO TINTAS E MODO FINANCEIRO)


    def ativarModoTintas(self):

        self.modoAtual = "tintas"

        self.containerTintas = Frame(self.mainContainer,
                                   width=940,
                                   height=670,
                                   bg=dict_cores["corPadrao"]
                                   )
        self.containerTintas.place(x=0, y=0)

        self.tituloTintas = Label(self.containerTintas,
                                  bg=dict_cores["corPadrao"],
                                  fg=dict_cores["roxo"],
                                  font=self.fonte2,
                                  text="ESTOQUE DE TINTAS")
        self.tituloTintas.place(x=50, y=30)


        # PARA ADICIONAR UMA COR

        self.labelModoCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="Adicionar nova cor")
        self.labelModoCor1.place(x=100, y=110)

        self.labelAdicionarCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="Nome da nova cor:")
        self.labelAdicionarCor1.place(x=100, y=140)

        self.entryAdicionarCor1 = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
                                    font=self.fonte3,
                                    width=41,
                                    borderwidth=0)
        self.entryAdicionarCor1.place(x=240, y=140)

        self.linha1 = Frame(self.containerTintas,
                            bg=dict_cores["verde"],
                            height=1,
                            width=250)
        self.linha1.place(x=240, y=160)

        self.btnAdicionarCor = Button(self.containerTintas,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Escolher tom da cor",
                                      font=self.fonte3,
                                      command=self.adicionarCor)
        self.btnAdicionarCor.place(x=490, y=200)

        # PARA EXCLUIR UMA COR

        self.labelModoCor2 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    font=self.fonte3,
                                    text="Excluir cor já existente")
        self.labelModoCor2.place(x=100, y=250)

        self.labelExcluirCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    font=self.fonte3,
                                    text="Nome da cor:")
        self.labelExcluirCor1.place(x=100, y=280)

        self.entryExcluirCor = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
                                    font=self.fonte3,
                                    borderwidth=0,
                                    width=41)
        self.entryExcluirCor.place(x=205, y=280)

        self.linha2 = Frame(self.containerTintas,
                            bg=dict_cores["vermelho"],
                            height=1,
                            width=250)
        self.linha2.place(x=205, y=300)

        self.btnExcluirCor = Button(self.containerTintas,
                                      bg=dict_cores["vermelho"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Excluir cor",
                                      font=self.fonte3,
                                      command=self.excluirCor)
        self.btnExcluirCor.place(x=500, y=310)

        # PARA LISTAR COR

        self.labelModoCor3 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="Exibir cor")
        self.labelModoCor3.place(x=100, y=350)

        self.labelExibirCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="Nome da cor:")
        self.labelExibirCor1.place(x=100, y=380)

        self.entryExibirCor1 = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
                                    borderwidth=0,
                                    font=self.fonte3,
                                    width=41)
        self.entryExibirCor1.place(x=210, y=380)

        self.linha3 = Frame(self.containerTintas,
                            bg=dict_cores["verde"],
                            height=1,
                            width=250)
        self.linha3.place(x=210, y=400)

        self.btnExibirCor = Button(self.containerTintas,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      font=self.fonte3,
                                      text="Exibir cor",
                                      command=self.exibirCor)
        self.btnExibirCor.place(x=500, y=440)
        
        self.mostradorTintas = Label(self.containerTintas,
                               bg=dict_cores["corPadrao"],
                               fg=dict_cores["roxo"],
                               width=85,
                               font=self.fonte3,
                               height=5,
                               anchor="w",
                               text="")
        self.mostradorTintas.place(x=80, y=500)

        self.btnSerializar = Button(self.containerTintas,
                                    bg=dict_cores["laranja"],
                                    fg="white",
                                    font=self.fonte3,
                                    text="Serializar dados",
                                    borderwidth=0,
                                    command=self.serializar)
        self.btnSerializar.place(x=760, y=20)


    def ativarModoFinanceiro(self):

        self.modoAtual = "financeiro"

        self.containerFinanceiro = Frame(self.mainContainer,
                                   width=940,
                                   height=670,
                                   bg=dict_cores["corPadrao"]
                                   )
        self.containerFinanceiro.place(x=0, y=0)

        self.tituloFinanceiro = Label(self.containerFinanceiro,
                                      bg=dict_cores["corPadrao"],
                                      font=self.fonte2,
                                      fg=dict_cores["roxo"],
                                      text="CONTROLE FINANCEIRO")
        self.tituloFinanceiro.place(x=50, y=30)

        # ADICIONANDO AO SALDO

        self.labelModoFinanceiro1 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="Acrescentar novo valor ao saldo")
        self.labelModoFinanceiro1.place(x=100, y=130)

        self.labelAdicionarValor = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="Valor a acrescentar:")
        self.labelAdicionarValor.place(x=100, y=160)

        self.entryAdicionarValor = Entry(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
                                    borderwidth=0,
                                    font=self.fonte3,
                                    width=41)
        self.entryAdicionarValor.place(x=245, y=160)

        self.linha4 = Frame(self.containerFinanceiro,
                            bg=dict_cores["verde"],
                            height=1,
                            width=250)
        self.linha4.place(x=245, y=180)

        self.btnAdicionarValor = Button(self.containerFinanceiro,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Adicionar valor",
                                      font=self.fonte3,
                                      command=self.adicionarValor)
        self.btnAdicionarValor.place(x=490, y=220)

        # RETIRANDO DO SALDO

        self.labelModoFinanceiro2 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    font=self.fonte3,
                                    text="Retirar valor do saldo")
        self.labelModoFinanceiro2.place(x=100, y=270)

        self.labelRetirarValor = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    font=self.fonte3,
                                    text="Valor a retirar:")
        self.labelRetirarValor.place(x=100, y=300)

        self.entryRetirarValor = Entry(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    font=self.fonte3,
                                    fg=dict_cores["fgEntry"],
                                    borderwidth=0,
                                    width=41)
        self.entryRetirarValor.place(x=210, y=300)

        self.linha5 = Frame(self.containerFinanceiro,
                            bg=dict_cores["vermelho"],
                            height=1,
                            width=250)
        self.linha5.place(x=210, y=320)

        self.btnRetirarValor = Button(self.containerFinanceiro,
                                      bg=dict_cores["vermelho"],
                                      font=self.fonte3,
                                      fg="white",
                                      borderwidth=0,
                                      text="Retirar valor",
                                      command=self.retirarValor)
        self.btnRetirarValor.place(x=500, y=380)

        # EXIBINDO SALDO

        self.labelModoFinanceiro3 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text="SALDO ATUAL DA LOJA")
        self.labelModoFinanceiro3.place(x=100, y=430)

        self.labelSaldo = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    font=self.fonte3,
                                    text=f"R$ {self.saldo}")
        self.labelSaldo.place(x=275, y=430)

        self.mostradorFinanceiro = Label(self.containerFinanceiro,
                               bg=dict_cores["corPadrao"],
                               fg=dict_cores["roxo"],
                               width=100,
                               font=self.fonte3,
                               height=5,
                               anchor="w",
                               text="")
        self.mostradorFinanceiro.place(x=100, y=520)


    # MÉTODOS GERAIS


    def serializar(self):
        self.sql.execute("SELECT * FROM cores")
        self.dadosCores = self.sql.fetchall()

        self.arq = open('coresSerializadas.txt', 'wb')

        for cor in self.dadosCores:
            pickle.dump(cor, self.arq)

        self.arq.close()

        self.mostradorTintas["bg"] = dict_cores["corPadrao"]
        self.mostradorTintas["text"] = "Serialização realizada com sucesso"
        self.janela.after(3000, self.apagar_msgTintas)


    def mudarTema(self):

        if self.temaAtual == "claro":
            dict_cores["corPadrao"] = cores_tema[1]
            dict_cores["fgEntry"] = "#ffffff"
            self.temaAtual = "escuro"

        else:
            dict_cores["corPadrao"] = cores_tema[0]
            dict_cores["fgEntry"] = "#000000"
            self.temaAtual = "claro"

        if self.modoAtual == "tintas":

            self.ativarModoTintas()

        elif self.modoAtual == "financeiro":

            self.ativarModoFinanceiro()


    # MÉTODOS PARA O MODO COR


    def adicionarCor(self):
        self.nomeCor = str(self.entryAdicionarCor1.get()).upper()
        self.tomCor = colorchooser.askcolor()[1]

        try:
            self.sql.execute(f"INSERT INTO cores (nome, hexcode) VALUES ('{self.nomeCor}', '{self.tomCor}')")
            self.conexao.commit()

            self.mostradorTintas["bg"] = dict_cores["corPadrao"]
            self.mostradorTintas["text"] = "Cor inserida com sucesso"
            self.janela.after(3000, self.apagar_msgTintas)

        except sqlite3.OperationalError:
            self.mostradorTintas["text"] = "Ocorreu um problema durante a inserção no banco de dados."
            self.janela.after(3000, self.apagar_msgTintas)


    def excluirCor(self):
        try:

            self.sql.execute(f"SELECT nome FROM cores WHERE nome = '{str(self.entryExcluirCor.get().upper())}'")

            self.item = self.sql.fetchone()

            if self.item:
                self.nomeCor = str(self.entryExcluirCor.get()).upper()

                self.sql.execute(f"DELETE FROM cores WHERE nome = '{self.nomeCor}'")
                self.conexao.commit()

                self.mostradorTintas["bg"] = dict_cores["corPadrao"]
                self.mostradorTintas["text"] = "Cor excluída com sucesso"
                self.janela.after(3000, self.apagar_msgTintas)
            else:
                self.mostradorTintas["bg"] = dict_cores["corPadrao"]
                self.mostradorTintas["text"] = "Cor não encontrada no banco de dados"
                self.janela.after(3000, self.apagar_msgTintas)

        except sqlite3.OperationalError:
            self.mostradorTintas["text"] = "Ocorreu um problema durante a exclusão no banco de dados."
            self.janela.after(3000, self.apagar_msgTintas)


    def exibirCor(self):
        try:

            self.sql.execute(f"SELECT hexcode FROM cores WHERE nome = '{str(self.entryExibirCor1.get().upper())}'")

            self.cor = self.sql.fetchone()

            if self.cor:
                self.mostradorTintas["bg"] = self.cor


                self.labelNomeCor = Label(self.mostradorTintas,
                                          font=self.fonte3,
                                        anchor="center")
                self.labelNomeCor.place(x=10, y=10)

                
                self.sql.execute(f"SELECT nome FROM cores WHERE nome = '{str(self.entryExibirCor1.get().upper())}'")

                self.nomeCor = self.sql.fetchone()

                self.labelNomeCor["text"] = self.nomeCor
                self.labelNomeCor["bg"] = "#ffffff"
                self.labelNomeCor["fg"] = "#000000"
            else:
                self.mostradorTintas["bg"] = dict_cores["corPadrao"]
                self.mostradorTintas["text"] = "Cor não encontrada no banco de dados"
                self.janela.after(3000, self.apagar_msgTintas)

        except sqlite3.OperationalError:
            self.mostradorTintas["text"] = "Ocorreu um problema durante a exibição."
            self.janela.after(3000, self.apagar_msgTintas)

        except TclError:
            self.mostradorTintas["bg"] = dict_cores["corPadrao"]
            self.mostradorTintas["text"] = "Hexadecimal inválido"
            self.janela.after(3000, self.apagar_msgTintas)


    # MÉETODOS PARA O MODO FINANCEIRO


    def adicionarValor(self):
        try:

            self.saldo += float(self.entryAdicionarValor.get())
            self.labelSaldo["text"] = f"R$ {self.saldo:.2f}"

            if self.saldo < 0:
                self.labelSaldo["fg"] = dict_cores["vermelho"]
            else:
                self.labelSaldo["fg"] = dict_cores["verde"]

            self.mostradorFinanceiro["text"] = "Valor adicionado com sucesso"
            self.janela.after(3000, self.apagar_msgFinanceiro)
            
        except ValueError:
            self.mostradorFinanceiro["text"] = "Insira apenas números"
            self.janela.after(3000, self.apagar_msgFinanceiro)


    def retirarValor(self):
        try:
            self.saldo -= float(self.entryRetirarValor.get())
            self.labelSaldo["text"] = f"R$ {self.saldo:.2f}"
            if self.saldo < 0:
                self.labelSaldo["fg"] = dict_cores["vermelho"]
            else:
                self.labelSaldo["fg"] = dict_cores["verde"]

            self.mostradorFinanceiro["text"] = "Valor retirado com sucesso"
            self.janela.after(3000, self.apagar_msgFinanceiro)

        except ValueError:
            self.mostradorFinanceiro["text"] = "Insira apenas números"
            self.janela.after(3000, self.apagar_msgFinanceiro)


    # MÉTODOS AUXILIARES


    def apagar_msgTintas(self):
        self.mostradorTintas["text"] = ''


    def apagar_msgFinanceiro(self):
        self.mostradorFinanceiro["text"] = ''


    def agradecimento(self):
        self.janela.destroy()

        self.cont = 3
        print("ENCERRANDO APLICAÇÃO EM")
        while self.cont >= 1:
            sleep(1)
            print(self.cont)
            self.cont-=1
        sleep(2)
        print("Obrigado por utilizar nossos serviços!")


try:

    aplicacao = App()

except AttributeError:
    print("Atributo ausente.")
    