from time import sleep

import keyboard
import pyautogui
from pynput.mouse import Controller, Button


# pyautogui.mouseInfo()

#Route du donjon (kanto)
route = [
    "right",
    "right",
    "up",
    "left",
    "up",
    "right",
    "up",
    "left",
    "up",
    "right",
    # "up",
    "left",
    "left",
    "left",
    "left",
    # "left",
    "down",
    "right",
    "right",
    # "right",
    "down",
    "left",
    "left",
    # "left",
    "down",
    "right",
    "right",
    # "right",
    "down",
    "left",
    "left",
    # "left",
    "down",
    "right",
    "right"
]

#Route du donjon (johto)
route_j = [
    "right",
    "right",
    "up",
    "left",
    "up",
    "right",
    "up",
    "left",
    "up",
    "right",
    "up",
    "left",
    "left",
    "left",
    "left",
    "left",
    "down",
    "right",
    "right",
    "right",
    "down",
    "left",
    "left",
    "left",
    "down",
    "right",
    "right",
    "right",
    "down",
    "left",
    "left",
    "left",
    "down",
    "right",
    "right"
]

route_h = [
    "left",
    "left",
    "left",
    "up",
    "up",
    "up",
    "up",
    "up",
    "up",
    "right",
    "down",
    "down",
    "down",
    "down",
    "down",
    "right",
    "up",
    "up",
    "up",
    "up",
    "up",
    "right",
    "down",
    "down",
    "down",
    "down",
    "down",
    "right",
    "up",
    "up",
    "up",
    "up",
    "up",
    "right",
    "down",
    "down",
    "down",
    "down",
    "down",
    "right",
    "up",
    "up",
    "up",
    "up",
    "up",
    "right",
    "down",
    "down",
    "down",
    "down",
    "down",
    "down",
    "left"
    "left"
]
i=0
flag = True

def stop_script():
    global flag
    flag = False
    print("Arrêt du script demandé...")

keyboard.on_press_key("num 0", lambda _: stop_script())
mouse = Controller()

#Lancement du donjon
route_selected = route_h
map = 'assets/fond_donjon_cave_cristaux.png'
pyautogui.moveTo(457,204)
pyautogui.click()

pyautogui.moveTo(623,261)

while flag:
    try:
        empty_room = pyautogui.locateOnScreen(map, confidence=0.95)
        if empty_room is not None:
            mouse.click(Button.left)
            pyautogui.press(route_selected[i])
            i+=1
            sleep(0.2)
    except:
        for _ in range(10):
            mouse.click(Button.left)
            sleep(0.005)

    # verif ici :434,189
    # couleur 92,184,92
    # 439,191
    if pyautogui.pixel(443,192) == (92,184,92):
        print("Fin du dj")
        pyautogui.moveTo(457, 204)
        pyautogui.click()
        pyautogui.moveTo(623, 261)
        i = 0
    else:
        print("Pas de fin")
        pass