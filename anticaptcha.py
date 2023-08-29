import pyautogui as pg
import pygame as p
from PIL import Image
import multiprocessing
from interface import Interface

IMG_SUPERIOR = [(901, 506), (963, 506), (1036, 506)]
IMG_INFERIOR = [(907, 566), (961, 568), (1034, 573)]
DESAFIO_REGIAO = (850, 528, 218, 78)
BOTAO_CONFIRMAR = (1008, 619)
BOTAO_PLAY = (1344, 750)


keep_running = multiprocessing.Value('i', 1)  # 1 indicates keep running, 0 indicates stop
process = None
anticaptcha_running = False
pokechange_running = False
antiafk_running = False

def anticaptcha(keep_running, tirar_foto, rotacionar_foto, procurar_imagem, play_audio):
    while keep_running.value:
        captcha_na_tela = procurar_imagem('imgs/inicio_captcha.png', 0.8)
        print(captcha_na_tela)
        imagem_encontrada = []
        imagem_nao_encontrada = []

        if captcha_na_tela != None:
            audio_file = "audio\alarme.mp3"  # Substitua pelo caminho do seu arquivo de áudio
            play_audio(audio_file)
            pg.moveTo(BOTAO_PLAY)
            pg.click()
            for posicao in IMG_SUPERIOR:
                imagem_carregada = tirar_foto(posicao)
                imagem_procurada = False
                for grau in range(361):
                    imagem_rotacionada = rotacionar_foto(imagem_carregada, grau)
                    box = procurar_imagem(imagem_rotacionada, 0.8, my_region=DESAFIO_REGIAO)
                    if box:
                        print('BOX - IMAGEM ENCONTRADA', box)
                        x, y = pg.center(box)
                        imagem_encontrada.append([posicao, (x, y)])
                        imagem_procurada = True
                        break
                if not imagem_procurada:
                    imagem_nao_encontrada.append(posicao)
            for posicao in imagem_encontrada:
                pg.moveTo(posicao[0])
                pg.click()
                pg.sleep(0.5)
                pg.moveTo(posicao[1])
                pg.click()
                pg.sleep(0.5)
            if len(imagem_nao_encontrada) > 0:
                for posicao in imagem_nao_encontrada:
                    pg.moveTo(posicao)
                    pg.click()
                    pg.sleep(0.5)
                    for tentativa in IMG_INFERIOR:
                        pg.moveTo(tentativa)
                        pg.click()
                        pg.sleep(0.5)
            pg.moveTo(BOTAO_CONFIRMAR)
            pg.click()
            pg.sleep(2)
            pg.moveTo(BOTAO_PLAY)
            pg.click()        

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