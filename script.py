from time import sleep
import keyboard
import pyautogui
pyautogui.moveTo(795, 280)
flag = True
# pyautogui.mouseInfo()

while flag:
    if keyboard.is_pressed("num 0"):
        flag = False

    # try:
    #     close_button = pyautogui.locateOnScreen("assets/close.png", region=(500, 140, 600, 600))
    #     if close_button is not None:
    #         pyautogui.click(close_button)
    #         flag = False
    # except Exception:
    #     pass


    pyautogui.click(clicks=20, interval=0.005)
