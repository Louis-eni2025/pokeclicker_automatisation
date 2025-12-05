import pyautogui
import time
from pynput.mouse import Controller, Button

print("Détection des mouvements de la souris")
mouse = Controller()


try:
    prev_x, prev_y = pyautogui.position()
    print(f"Position initiale: X={prev_x}, Y={prev_y}")

    while True:
        current_x, current_y = pyautogui.position()

        if current_x != prev_x or current_y != prev_y:
            print("Verrouillage")
            #22,881
            #click
            #22, 645
            #click
            #30, 555
            #click
            # pyautogui.moveTo(22,881)
            mouse.position = (22,881)
            mouse.click(Button.left)
            mouse.position = (22, 645)
            mouse.click(Button.left)
            mouse.position = (30, 555)
            mouse.click(Button.left)
            

            exit()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nDétection arrêtée")
    print(f"Position finale: X={current_x}, Y={current_y}")