import sqlite3
import pickle

"""
- Cores
Adicionar
Consultar
Excluir

-Login e senha
Modificar
Dica

- Relatório do capital
A definir funcionalidades
"""
    
conexao = sqlite3.connect("estoqueDeCores.db")
sql = conexao.cursor()
sql.execute("CREATE TABLE cores (hexcode, nome)")

def adicionar_cor():
    tom_cor = input("Insira o tom da cor [código hexadecimal]: ")
    nome_cor = input("Insira o nome da cor: ")

    sql.execute(f"INSERT INTO cores (hexcode, nome) VALUES ('{tom_cor}', '{nome_cor}')")
    conexao.commit()

def listar_cores():
    sql.execute("SELECT * FROM cores")
    cores = sql.fetchall()

    for cor in cores:
        print(cor)


def excluir_cor():
    cor = input("Insira o NOME da cor que deseja excluir")
    sql.execute(f"DELETE FROM cores WHERE nome = '{cor}'")
    conexao.commit()

def serializar():
    sql.execute("SELECT * FROM cores")
    cores = sql.fetchall()

    arq = open('coresSerializadas.txt', 'wb')
    for cor in cores:
        pickle.dump(cor, arq)


while True:
    opc = input("[1] Adicionar cores\n[2] Listar cores\n[3] Excluir cores\n[4] Serializar")
    opcs_lista = ['1', '2', '3', '4']
    if opc not in opcs_lista:
        break
    elif opc == '1':
        adicionar_cor()
    elif opc == '2':
        listar_cores()
    elif opc == '3':
        excluir_cor()
    elif opc == '4':
        serializar()

conexao.close()
