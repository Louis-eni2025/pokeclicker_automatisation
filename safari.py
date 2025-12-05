from time import sleep
import keyboard
import pyautogui
from pynput.mouse import Controller, Button



mouse = Controller()
# 490,219
mouse.position = (490,219)
mouse.click(Button.left, 1)
#

flag = True

def stop_script():
    global flag
    flag = False
    print("Arrêt du script demandé...")

# Enregistrer le listener (s'active à n'importe quel moment)
keyboard.on_press_key("num 0", lambda _: stop_script())

while flag:
    print("-----------")
    try:
        player_left = pyautogui.locateOnScreen('assets/dresseur_gauche.png', confidence=0.8)
        if player_left:
            pyautogui.press("right")
            sleep(0.2)
    except:
        pass


    try:
        player_right = pyautogui.locateOnScreen('assets/dresseur_droit.png', confidence=0.8)
        if player_right:
            pyautogui.press("left")
            sleep(0.2)
    except:
        pass

    if pyautogui.pixel(580, 603) == (223, 105, 26):
        print("Pokemon apparait")
        sleep(0.2)

        # try:
        #     scarabrute = pyautogui.locateOnScreen('assets/scarabrute.png', confidence=0.8)
        #     print("Scarabrute trouve")
        #     flag = False
        #     pyautogui.press("c")
        #     exit()
        # except ImageNotFoundException as e:
        #     print("Scarabrute pas trouvé")
        # except Exception as e:
        #     print(f"Erreur détaillée: {type(e).__name__}: {str(e)}")
        print("Pokeball go")
        pyautogui.press("c")
        # try:
        #     tauros = pyautogui.locateOnScreen('assets/tauros.png', confidence=0.8)
        #     print("Tauros trouve")
        #     tauros_vu += 1
        #     # flag = False
        #     print("Pokeball go")
        #     pyautogui.press("c")
        # except ImageNotFoundException as e:
        #     print("Tauros pas trouvé")
        #     print("Pokemon OSEF")
        #     pyautogui.press('f')
        #     print("On se casse")
        # except Exception as e:
        #     print(f"Erreur détaillée: {type(e).__name__}: {str(e)}")
        #
        # pokemon_vu += 1
        # print(f"Tauros vus: {tauros_vu}/{pokemon_vu}")
        try:
            debut_contest = pyautogui.locateOnScreen('assets/bug_catching_contest.png', confidence=0.8)
            mouse.position = (debut_contest.x, debut_contest.y)
            mouse.click(Button.left, 1)
        except:
            print("Toujours en cours")


