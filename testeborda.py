import tkinter as tk

def alterar_borda(entry):
    entry.config(highlightthickness=2, highlightbackground="blue")

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Entrada com Borda Inferior")

# Criar um campo Entry
campo_entry = tk.Entry(janela)

# Colocar o Entry na janela
campo_entry.pack(padx=20, pady=20)

# Botão para alterar a borda
botao_alterar_borda = tk.Button(janela, text="Alterar Borda", command=lambda: alterar_borda(campo_entry))
botao_alterar_borda.pack(pady=10)

# Iniciar o loop principal da janela
janela.mainloop()