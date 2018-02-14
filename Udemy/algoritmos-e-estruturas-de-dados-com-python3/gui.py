# Módulo para criar Telas
from tkinter import *

# Cria uma nova janela
window = Tk()

# Seta o título da janela
window.title("Meu Programa")

entry_text = Entry(window, width=30)

entry_text.pack() # Gerenciador de Geometria

entry_text.focus_set()

def click_button():
    print(entry_text.get())

button = Button(window, text="Clique aqui", width=20, command=click_button)
button.pack()

#tamanho do janela
window.geometry("300x150")

window.mainloop()