from time import sleep
import keyboard
from pynput.mouse import Controller, Button

mouse = Controller()
mouse.position = (793, 266)
flag = True
def stop_script():
    global flag
    flag = False
    print("Arrêt du script demandé...")

# Enregistrer le listener (s'active à n'importe quel moment)
keyboard.on_press_key("num 0", lambda _: stop_script())


while flag:
    mouse.click(Button.left)
    sleep(0.005)