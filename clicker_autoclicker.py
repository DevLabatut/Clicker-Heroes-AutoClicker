import pyautogui
import time
import keyboard

def main():
    running = True

    def toggle_running():
        nonlocal running
        running = not running
        if running:
            print("Automação ativada: Continuando a clicar.")
        else:
            print("Automação desativada: Pausado.")
            
    keyboard.add_hotkey('F2', toggle_running)

    print("Automação começará em 5 segundos...")
    time.sleep(5)
    print("Pressione F2 para pausar/continuar a automação.")

    try:
        while True:
            if running:
                pyautogui.click()
                time.sleep(0.01)
            else:
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("Automação interrompida pelo usuário.")

if __name__ == "__main__":
    main()
