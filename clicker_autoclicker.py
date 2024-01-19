import pyautogui
import time

time.sleep(5)

try:
    while True:
        pyautogui.click()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Automação interrompida pelo usuário.")
