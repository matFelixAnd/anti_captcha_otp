import pyautogui
import time
# Tempo de espera entre pressionar 'w' e 's' em segundos


def antiafk():
    while True:
        intervalo_antiafk = 2  # 2 minutos
        # Simula a pressão da tecla 'w'
        pyautogui.press('w')
        time.sleep(intervalo_antiafk)
        # Simula a pressão da tecla 's'
        pyautogui.press('s')
        # Aguarda o intervalo especificado anwtes de repetir o loop
        time.sleep(intervalo_antiafk)
