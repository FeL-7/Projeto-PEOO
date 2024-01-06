from tkinter import *
from tkinter import font
from tkinter import colorchooser
from PIL import ImageTk, Image
import sqlite3

"""ESTILIZAR:
FONTE"""


# claro = "#f5f7fc"
# escuro = "#232833"

cores_tema = ["#f5f7fc", "#232833"]

dict_cores = {"corPadrao": cores_tema[0], "lilas": "#746fff", "roxo": "#5e5bc9", "verde": "#00c6ab", "fgEntry": "#000000", "vermelho": "#eb0626"}

class App:
    def __init__(self):
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

        self.conexao = sqlite3.connect("estoqueDeTintas.db")
        self.sql = self.conexao.cursor()


        # BARRA LATERAL

        self.barraLateral = Frame(self.janela, 
                                   width=260,
                                   height=670,
                                   bg=dict_cores["roxo"])
        self.barraLateral.place(x=0, y=0)

        self.img_perfilOriginal = Image.open("imagens\perfil.jpg")
        self.img_perfilAlterada = self.img_perfilOriginal.resize((150, 170))
        self.img_perfil = ImageTk.PhotoImage(self.img_perfilAlterada)

        self.icone_perfil = Label(self.barraLateral,
                                  image=self.img_perfil)
        self.icone_perfil.place(x=50, y=50)
        self.nome_usuario = Label(self.barraLateral,
                                  text="Sr. Gerson 'Coringa'",
                                  bg=dict_cores["roxo"],
                                  fg=cores_tema[0])
        self.nome_usuario.place(x=70, y=230)

        self.fonte1 = font.Font(family="Tw Cen MT", size=16, weight="normal", slant="roman", underline=False)
        
        self.btn_modoTintas = Button(self.barraLateral,
                                     bg=dict_cores["roxo"],
                                     fg=cores_tema[0],
                                     text="Gerenciar Tintas",
                                     font=self.fonte1,
                                     borderwidth=0,
                                     command=self.ativarModoTintas)
        self.btn_modoTintas.place(x=55, y=320)

        self.btn_modoFinanceiro = Button(self.barraLateral,
                                        bg=dict_cores["roxo"],
                                        fg=cores_tema[0],
                                        text="Controle Financeiro",
                                        font=self.fonte1,
                                        borderwidth=0,
                                        command=self.ativarModoFinanceiro)
        self.btn_modoFinanceiro.place(x=45, y=380)

        self.img_trocarTema = PhotoImage(file="imagens\mudar_tema.png").subsample(12)

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

        self.background_img = ImageTk.PhotoImage(Image.open("imagens\img-background.jpg"))
        self.background = Label(self.mainContainer,
                                width=940,
                                height=670,
                                bg=dict_cores["corPadrao"],
                                image=self.background_img
                                )
        self.background.place(x=-3, y=-1)
        

        # RODAPÉ

        self.rodape = Frame(self.janela,
                            width=940,
                            height=40,
                            bg=dict_cores["lilas"])
        self.rodape.place(x=260,y=630)



        self.janela.mainloop()


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
                                  text="ESTOQUE DE TINTAS")
        self.tituloTintas.place(x=50, y=30)


        # PARA ADICIONAR UMA COR

        self.labelModoCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="ADICIONAR NOVA COR")
        self.labelModoCor1.place(x=100, y=110)

        self.labelAdicionarCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA NOVA COR:")
        self.labelAdicionarCor1.place(x=100, y=140)

        self.entryAdicionarCor1 = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
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
                                      command=self.adicionarCor)
        self.btnAdicionarCor.place(x=490, y=200)

        # PARA EXCLUIR UMA COR

        self.labelModoCor2 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    text="EXCLUIR COR JÁ EXISTENTE")
        self.labelModoCor2.place(x=100, y=250)

        self.labelExcluirCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    text="NOME DA COR:")
        self.labelExcluirCor1.place(x=100, y=280)

        self.entryExcluirCor = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
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
                                      command=self.excluirCor)
        self.btnExcluirCor.place(x=500, y=310)

        # PARA LISTAR COR

        self.labelModoCor3 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="EXIBIR COR")
        self.labelModoCor3.place(x=100, y=350)

        self.labelExibirCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA COR:")
        self.labelExibirCor1.place(x=100, y=380)

        self.entryExibirCor1 = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
                                    borderwidth=0,
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
                                      text="Exibir cor",
                                      command=self.exibirCor)
        self.btnExibirCor.place(x=500, y=440)
        
        self.mostradorTintas = Label(self.containerTintas,
                               bg=dict_cores["corPadrao"],
                               fg=dict_cores["roxo"],
                               width=100,
                               height=5,
                               anchor="w",
                               text="")
        self.mostradorTintas.place(x=100, y=520)
        


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
                                      fg=dict_cores["roxo"],
                                      text="CONTROLE FINANCEIRO")
        self.tituloFinanceiro.place(x=50, y=30)

        # ADICIONANDO AO SALDO

        self.labelModoFinanceiro1 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="ACRESCENTAR NOVO VALOR AO SALDO")
        self.labelModoFinanceiro1.place(x=100, y=130)

        self.labelAdicionarValor = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="VALOR A ACRESCENTAR:")
        self.labelAdicionarValor.place(x=100, y=160)

        self.entryAdicionarValor = Entry(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["fgEntry"],
                                    borderwidth=0,
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
                                      command=self.adicionarValor)
        self.btnAdicionarValor.place(x=490, y=220)

        # RETIRANDO DO SALDO

        self.labelModoFinanceiro2 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    text="RETIRAR VALOR DO SALDO")
        self.labelModoFinanceiro2.place(x=100, y=270)

        self.labelRetirarValor = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["vermelho"],
                                    text="VALOR A RETIRAR:")
        self.labelRetirarValor.place(x=100, y=300)

        self.entryRetirarValor = Entry(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
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
                                      fg="white",
                                      borderwidth=0,
                                      text="Retirar valor",
                                      command=self.retirarValor)
        self.btnRetirarValor.place(x=500, y=380)

        # EXIBINDO SALDO

        self.labelModoFinanceiro3 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="SALDO ATUAL DA LOJA")
        self.labelModoFinanceiro3.place(x=100, y=430)

        self.labelSaldo = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text=f"R$ {self.saldo}")
        self.labelSaldo.place(x=250, y=430)

        self.mostradorFinanceiro = Label(self.containerFinanceiro,
                               bg=dict_cores["corPadrao"],
                               fg=dict_cores["roxo"],
                               width=100,
                               height=5,
                               anchor="w",
                               text="")
        self.mostradorFinanceiro.place(x=100, y=520)

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


    def adicionarCor(self):
        self.nomeCor = str(self.entryAdicionarCor1.get()).upper()
        self.tomCor = colorchooser.askcolor()[1]

        self.sql.execute(f"INSERT INTO cores (nome, hexcode) VALUES ('{self.nomeCor}', '{self.tomCor}')")
        self.conexao.commit()

        self.mostradorTintas["bg"] = dict_cores["corPadrao"]
        self.mostradorTintas["text"] = "Cor inserida com sucesso"
        self.janela.after(3000, self.apagar_msgTintas)


    def excluirCor(self):
        self.nomeCor = str(self.entryExcluirCor.get()).upper()

        self.sql.execute(f"DELETE FROM cores WHERE nome = '{self.nomeCor}'")
        self.conexao.commit()

        self.mostradorTintas["bg"] = dict_cores["corPadrao"]
        self.mostradorTintas["text"] = "Cor excluída com sucesso"
        self.janela.after(3000, self.apagar_msgTintas)


    def exibirCor(self):
        self.sql.execute(f"SELECT hexcode FROM cores WHERE nome = '{str(self.entryExibirCor1.get().upper())}'")

        self.cor = self.sql.fetchone()

        self.mostradorTintas["bg"] = self.cor


        self.labelNomeCor = Label(self.mostradorTintas,
                                  anchor="center")
        self.labelNomeCor.place(x=10, y=10)
        
        self.sql.execute(f"SELECT nome FROM cores WHERE nome = '{str(self.entryExibirCor1.get().upper())}'")

        self.nomeCor = self.sql.fetchone()

        self.labelNomeCor["text"] = self.nomeCor
        self.labelNomeCor["bg"] = "white"
        self.labelNomeCor["fg"] = "black"


    def adicionarValor(self):
        self.saldo += float(self.entryAdicionarValor.get())
        self.labelSaldo["text"] = f"R$ {self.saldo:.2f}"
        if self.saldo < 0:
            self.labelSaldo["fg"] = dict_cores["vermelho"]
        else:
            self.labelSaldo["fg"] = dict_cores["verde"]

        self.mostradorFinanceiro["text"] = "VALOR ADICIONADO COM SUCESSO"
        self.janela.after(3000, self.apagar_msgFinanceiro)


    def retirarValor(self):
        self.saldo -= float(self.entryRetirarValor.get())
        self.labelSaldo["text"] = f"R$ {self.saldo:.2f}"
        if self.saldo < 0:
            self.labelSaldo["fg"] = dict_cores["vermelho"]
        else:
            self.labelSaldo["fg"] = dict_cores["verde"]

        self.mostradorFinanceiro["text"] = "VALOR RETIRADO COM SUCESSO"
        self.janela.after(3000, self.apagar_msgFinanceiro)

    def apagar_msgTintas(self):
        self.mostradorTintas["text"] = ''

    def apagar_msgFinanceiro(self):
        self.mostradorFinanceiro["text"] = ''



aplicacao = App()