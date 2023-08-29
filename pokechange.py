import pyautogui as pg
import time
import pygame as p

# Defina as coordenadas do ponto onde você deseja clicar
poke_1 = [(31, 202), (131, 208), (86, 207), (182, 206), (265, 204)]
# , (226, 207), (182, 204), (265, 204)

# Defina o intervalo em segundos entre os cliques
interval_seconds = 3


def procurar_imagem(caminho_da_imagem, my_confidence, my_region=None):
    box = pg.locateOnScreen(caminho_da_imagem, confidence=my_confidence, region=my_region)
    if box:
        return box
    return None


def play_audio(file_path):
    p.mixer.init()
    p.mixer.music.load(file_path)
    p.mixer.music.play()


def pokechange():
    try:
        index = 0  # Índice da coordenada atual na lista
        while True:
            captcha_na_tela = procurar_imagem('imgs/inicio_captcha.png', 0.8)
            print(captcha_na_tela)
            # se o captcha aparece
            if captcha_na_tela is not None:
                time.sleep(60)
            # Obtenha as coordenadas atuais
            x_coordinate, y_coordinate = poke_1[index]

            # Mova o cursor para as coordenadas atuais
            pg.moveTo(x_coordinate, y_coordinate)

            # clique no local
            pg.click()
            # intervalo especificado
            time.sleep(interval_seconds)
            # Atualize o índice para a próxima coordenada
            index = (index + 1) % len(poke_1)
    except:
        print('erro')