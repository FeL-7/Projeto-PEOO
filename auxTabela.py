import sqlite3

conexao = sqlite3.connect("PEOO\Projeto-PEOO\estoqueDeTintas.db")
sql = conexao.cursor()

sql.execute("CREATE TABLE cores (nome, hexcode)")
