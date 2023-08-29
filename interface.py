from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import multiprocessing
from tkinter import messagebox


class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Felix's Bot")    

        # Carrega o ícone e converte para formato Tkinter suportado
        icon = Image.open("imgs\icone.ico")  # Substitua pelo caminho correto
        icon = icon.resize((32, 32))  # Ajuste o tamanho do ícone conforme necessário
        self.icon = ImageTk.PhotoImage(icon)

        self.janela.iconphoto(True, self.icon)


    # Configurar expansão das colunas e linhas
        janela.columnconfigure(0, weight=1)
        janela.columnconfigure(1, weight=1)
        janela.columnconfigure(2, weight=1)
        janela.rowconfigure(0, weight=1)
        janela.rowconfigure(1, weight=1)
        janela.rowconfigure(2, weight=1)
        janela.rowconfigure(3, weight=1)
        janela.rowconfigure(4, weight=1)

        texto_orientação = Label(janela,
        text="Clique em Start para começar o bot\n Stop para parar \n Close para fechar.")
        texto_orientação.grid(column=0, row=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        texto_orientação.config(font=("Arial", 16), anchor="center")

        texto_aviso = Label(janela, text="LEMBRE DE SEGUIR A INTERFACE DO OTPOKEMON\n IGUAL A IMAGEM 'TELA.PNG'")
        texto_aviso.grid(column=0, row=1, columnspan=3, padx=10, pady=1, sticky="nsew")
        texto_aviso.config(font=("Arial", 10), fg="red", anchor="center")

        # Resto do seu código de configuração dos botões
        start_anticaptcha = Button(janela, text="Start AntiCaptcha", command=self.start_anticaptcha)
        start_anticaptcha.grid(column=0, row=2, padx=10, pady=10, sticky="nsew")

        start_pokechange_btn = Button(janela, text="Iniciar Pokechange")
        start_pokechange_btn.grid(column=1, row=2, padx=10, pady=10, sticky="nsew")
        
        start_antiafk_btn = Button(janela, text="Iniciar Anti-AFK")
        start_antiafk_btn.grid(column=2, row=2, padx=10, pady=10, sticky="nsew")

        btn_stop_captcha = Button(janela, text="Stop Anticaptcha", command=self.stop_anticaptcha)
        btn_stop_captcha.grid(column=0, row=3, padx=10, pady=10, sticky="nsew")

        btn_stop_pokechange = Button(janela, text="Stop Poke-Change")
        btn_stop_pokechange.grid(column=1, row=3, padx=10, pady=10, sticky="nsew")

        btn_stop_antiafk = Button(janela, text="Stop Anti-AFK")
        btn_stop_antiafk.grid(column=2, row=3, padx=10, pady=10, sticky="nsew")

        btn_close = Button(janela, text="Close", command=self.close_interface)
        btn_close.grid(column=0, row=4, padx=10, pady=10, columnspan=3, sticky="nsew")

        self.running = False  # Variável para controlar a execução do bot

######################################CONFIG DE BOTOES#####################################################   



    def start_anticaptcha(self):
        global process, anticaptcha_running
        if not anticaptcha_running:
            process = multiprocessing.Process(target=anticaptcha, args=(keep_running, tirar_foto, rotacionar_foto, procurar_imagem, play_audio))
            process.start()
            anticaptcha_running = True
    
    def stop_anticaptcha(self):
        global process, anticaptcha_running
        if anticaptcha_running:
            keep_running.value = 0
            process.join()
            anticaptcha_running = False

        def close_interface(self):
            if messagebox.askokcancel("Fechar", "Deseja fechar o programa?"):
                # Coloque aqui o código para parar qualquer processo em andamento, como AntiCaptcha
                self.janela.destroy()  # Fecha a interface
