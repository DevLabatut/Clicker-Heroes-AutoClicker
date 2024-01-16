import pyautogui
import time

# Tempo de espera antes do início da automação (em segundos)
time.sleep(5)

try:
    while True:
        # Simula um clique do botão esquerdo do mouse
        pyautogui.click()
        # Aguarda um intervalo muito curto antes do próximo clique (em segundos)
        time.sleep(0.001)

except KeyboardInterrupt:
    # Captura a exceção KeyboardInterrupt (Ctrl+C) para encerrar a automação
    print("Automação interrompida pelo usuário.")
