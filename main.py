import tkinter as tk
from interface import Interface  # Importa a classe Interface do arquivo interface.py
from tkinter import PhotoImage
from tkinter import messagebox

#from anticaptcha import Anticaptcha # Importa o anticaptcha
#from pokechange import Pokechange # Importa a troca de poke


def main():
    janela = tk.Tk()
    app = Interface(janela)  # Cria uma instância da classe Interface

    

    janela.mainloop()

if __name__ == "__main__":
    main()

