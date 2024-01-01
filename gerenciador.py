from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import sqlite3

claro = "#f5f7fc"
escuro = "#2c455c"

dict_cores = {"corPadrao": claro, "lilas": "#746fff", "roxo": "#5e5bc9", "verde": "#00c6ab"}

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Gerson Pinturas")
        self.janela.geometry("1200x670")
        self.janela.configure(bg=dict_cores["corPadrao"])
        self.janela.resizable(width=False, height=False)
        
        self.icone = PhotoImage(file="PEOO\Projeto-PEOO\imagens\icone.png")
        self.janela.iconphoto(False, self.icone)

        self.saldo = 0.00

        self.conexao = sqlite3.connect("estoqueDeTintas.db")
        self.sql = self.conexao.cursor()


        # BARRA LATERAL (AINDA FALTA ADICIONAR FUNCIONALIDADE PARA TROCA DE TEMA)

        self.barraLateral = Frame(self.janela, 
                                   width=260,
                                   height=670,
                                   bg=dict_cores["roxo"])
        self.barraLateral.place(x=0, y=0)

        self.img_perfilOriginal = Image.open("PEOO\Projeto-PEOO\imagens\perfil.jpg")
        self.img_perfilAlterada = self.img_perfilOriginal.resize((150, 170))
        self.img_perfil = ImageTk.PhotoImage(self.img_perfilAlterada)

        self.icone_perfil = Label(self.barraLateral,
                                  image=self.img_perfil)
        self.icone_perfil.place(x=50, y=50)
        self.nome_usuario = Label(self.barraLateral,
                                  text="Sr. Gerson 'Coringa'",
                                  bg=dict_cores["roxo"],
                                  fg=claro)
        self.nome_usuario.place(x=70, y=230)

        self.fonte1 = font.Font(family="Tw Cen MT", size=16, weight="normal", slant="roman", underline=False)
        
        self.btn_modoTintas = Button(self.barraLateral,
                                     bg=dict_cores["roxo"],
                                     fg=claro,
                                     text="Gerenciar Tintas",
                                     font=self.fonte1,
                                     borderwidth=0,
                                     command=self.ativarModoTintas)
        self.btn_modoTintas.place(x=55, y=320)

        self.btn_modoFinanceiro = Button(self.barraLateral,
                                        bg=dict_cores["roxo"],
                                        fg=claro,
                                        text="Controle Financeiro",
                                        font=self.fonte1,
                                        borderwidth=0,
                                        command=self.ativarModoFinanceiro)
        self.btn_modoFinanceiro.place(x=45, y=380)


        #CONTEÚDO PRINCIPAL

        self.mainContainer = Frame(self.janela,
                                   width=940,
                                   height=670,
                                   bg=dict_cores["corPadrao"]
                                   )
        self.mainContainer.place(x=260, y=0)

        self.background_img = ImageTk.PhotoImage(Image.open("PEOO\Projeto-PEOO\imagens\img-background.jpg"))
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
                                    fg="black",
                                    width=60)
        self.entryAdicionarCor1.place(x=240, y=140)

        self.btnAdicionarCor = Button(self.containerTintas,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Escolher tom da cor")
        self.btnAdicionarCor.place(x=490, y=200)

        # PARA EXCLUIR UMA COR

        self.labelModoCor2 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="EXCLUIR COR JÁ EXISTENTE")
        self.labelModoCor2.place(x=100, y=250)

        self.labelExcluirCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA COR:")
        self.labelExcluirCor1.place(x=100, y=280)

        self.entryExcluirCor = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryExcluirCor.place(x=240, y=280)

        self.btnExcluirCor = Button(self.containerTintas,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Excluir cor")
        self.btnExcluirCor.place(x=500, y=310)

        # PARA LISTAR COR

        self.labelModoCor3 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="LISTAR CORES")
        self.labelModoCor3.place(x=100, y=350)

        self.labelListarCor1 = Label(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA COR:")
        self.labelListarCor1.place(x=100, y=380)

        self.entryListarCor1 = Entry(self.containerTintas,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryListarCor1.place(x=240, y=410)

        self.btnListarCor = Button(self.containerTintas,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Listar cor")
        self.btnListarCor.place(x=500, y=440)
        
        self.mostradorTintas = Label(self.containerTintas,
                               bg=dict_cores["corPadrao"],
                               fg=dict_cores["roxo"],
                               width=100,
                               height=5,
                               anchor="w",
                               text="Cor inserida com sucesso")
        self.mostradorTintas.place(x=100, y=520)
        


    def ativarModoFinanceiro(self):

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
                                    fg="black",
                                    width=60)
        self.entryAdicionarValor.place(x=240, y=160)

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
                                    fg=dict_cores["verde"],
                                    text="RETIRAR VALOR DO SALDO")
        self.labelModoFinanceiro2.place(x=100, y=270)

        self.labelRetirarValor = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="VALOR A RETIRAR:")
        self.labelRetirarValor.place(x=100, y=300)

        self.entryRetirarValor = Entry(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryRetirarValor.place(x=240, y=300)

        self.btnRetirarValor = Button(self.containerFinanceiro,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Retirar valor",
                                      command=self.retirarValor)
        self.btnRetirarValor.place(x=500, y=330)

        # EXIBINDO SALDO

        self.labelModoFinanceiro3 = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="SALDO ATUAL DA LOJA")
        self.labelModoFinanceiro3.place(x=100, y=370)

        self.labelSaldo = Label(self.containerFinanceiro,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text=f"R$ {self.saldo}")
        self.labelSaldo.place(x=250, y=370)

        self.mostradorFinanceiro = Label(self.containerFinanceiro,
                               bg=dict_cores["corPadrao"],
                               fg=dict_cores["roxo"],
                               width=100,
                               height=5,
                               anchor="w",
                               text="")
        self.mostradorFinanceiro.place(x=100, y=520)


    def adicionarValor(self):
        self.saldo += float(self.entryAdicionarValor.get())
        self.labelSaldo["text"] = f"R$ {self.saldo:.2f}"
        self.mostradorFinanceiro["text"] = "VALOR ADICIONADO COM SUCESSO"
        # Adicionar sleep


    def retirarValor(self):
        self.saldo -= float(self.entryRetirarValor.get())
        self.labelSaldo["text"] = f"R$ {self.saldo:.2f}"
        self.mostradorFinanceiro["text"] = "VALOR RETIRADO COM SUCESSO"
        # Adicionar sleep





aplicacao = App()