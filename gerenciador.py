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
        self.background.destroy()

        self.statusTelaModoTintas = "Criada"


        # PARA ADICIONAR UMA COR

        self.labelModoCor1 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="ADICIONAR NOVA COR")
        self.labelModoCor1.place(x=100, y=30)

        self.labelAdicionarCor1 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA NOVA COR:")
        self.labelAdicionarCor1.place(x=100, y=60)

        self.labelAdicionarCor2 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="CÓDIGO (HEXADECIMAL) DA NOVA COR:")
        self.labelAdicionarCor2.place(x=100, y=90)

        self.entryAdicionarCor1 = Entry(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryAdicionarCor1.place(x=240, y=60)

        self.entryAdicionarCor2 = Entry(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryAdicionarCor2.place(x=330, y=90)

        self.btnAdicionarCor = Button(self.mainContainer,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Adicionar cor")
        self.btnAdicionarCor.place(x=490, y=120)

        # PARA EXCLUIR UMA COR

        self.labelModoCor2 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="EXCLUIR COR JÁ EXISTENTE")
        self.labelModoCor2.place(x=100, y=170)

        self.labelExcluirCor1 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA COR:")
        self.labelExcluirCor1.place(x=100, y=200)

        self.entryExcluirCor = Entry(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryExcluirCor.place(x=240, y=200)

        self.btnExcluirCor = Button(self.mainContainer,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Excluir cor")
        self.btnExcluirCor.place(x=500, y=230)

        # PARA LISTAR COR

        self.labelModoCor3 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="LISTAR CORES")
        self.labelModoCor3.place(x=100, y=270)

        self.labelListarCor1 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="NOME DA COR:")
        self.labelListarCor1.place(x=100, y=300)

        self.entryListarCor1 = Entry(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryListarCor1.place(x=240, y=330)

        self.btnListarCor = Button(self.mainContainer,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Listar cor")
        self.btnListarCor.place(x=500, y=360)

        self.elementosModoTintas = [self.labelModoCor1, self.labelModoCor2, self.labelModoCor3, 
                                    self.labelAdicionarCor1, self.entryAdicionarCor2, self.labelAdicionarCor2, 
                                    self.entryAdicionarCor1, self.entryAdicionarCor2, self.btnAdicionarCor, 
                                    self.labelExcluirCor1, self.entryExcluirCor, self.btnExcluirCor, self.labelModoCor3, 
                                    self.labelListarCor1, self.entryListarCor1, self.btnListarCor]


        if self.statusTelaModoFinanceiro == "Criada":
            for i in self.elementosModoFinanceiro:
                i.destroy()

            self.statusTelaModoFinanceiro = "Destruída"
        


    def ativarModoFinanceiro(self):
        self.background.destroy()

        self.statusTelaModoFinanceiro = "Criada"

        if self.statusTelaModoTintas == "Criada":
            for i in self.elementosModoTintas:
                i.destroy()

            self.statusTelaModoTintas = "Destruída"


        # ADICIONANDO AO SALDO

        self.labelModoFinanceiro1 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="ACRESCENTAR NOVO VALOR AO SALDO")
        self.labelModoFinanceiro1.place(x=100, y=30)

        self.labelAdicionarValor = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="VALOR A ACRESCENTAR:")
        self.labelAdicionarValor.place(x=100, y=60)

        self.entryAdicionarValor = Entry(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryAdicionarValor.place(x=240, y=60)

        self.btnAdicionarValor = Button(self.mainContainer,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Adicionar valor")
        self.btnAdicionarValor.place(x=490, y=120)

        # RETIRANDO DO SALDO

        self.labelModoFinanceiro2 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="RETIRAR VALOR DO SALDO")
        self.labelModoFinanceiro2.place(x=100, y=170)

        self.labelRetirarValor = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="VALOR A RETIRAR:")
        self.labelRetirarValor.place(x=100, y=200)

        self.entryRetirarValor = Entry(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg="black",
                                    width=60)
        self.entryRetirarValor.place(x=240, y=200)

        self.btnRetirarValor = Button(self.mainContainer,
                                      bg=dict_cores["verde"],
                                      fg="white",
                                      borderwidth=0,
                                      text="Retirar valor")
        self.btnRetirarValor.place(x=500, y=230)

        # EXIBINDO SALDO

        self.labelModoFinanceiro3 = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="SALDO ATUAL DA LOJA")
        self.labelModoFinanceiro3.place(x=100, y=270)

        self.labelSaldo = Label(self.mainContainer,
                                    bg=dict_cores["corPadrao"],
                                    fg=dict_cores["verde"],
                                    text="R$")
        self.labelSaldo.place(x=250, y=270)

        self.elementosModoFinanceiro = [self.labelModoFinanceiro1, self.labelModoFinanceiro2, self.labelModoFinanceiro3, self.labelAdicionarValor, self.entryAdicionarValor, self.btnAdicionarValor, self.labelRetirarValor, self.entryRetirarValor, self.btnRetirarValor, self.labelSaldo]








aplicacao = App()