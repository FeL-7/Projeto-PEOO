from tkinter import Tk, font

root = Tk()

# Obtém uma lista de fontes disponíveis no sistema
fontes_disponiveis = font.families()

# Imprime a lista de fontes
print(fontes_disponiveis)

root.mainloop()
