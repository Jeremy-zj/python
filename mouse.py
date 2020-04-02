import pyautogui
import time

L_pos = pyautogui.position()

try:
    while True:
        N_pos = pyautogui.position()
        if L_pos != N_pos:
            print(N_pos)
            L_pos = N_pos
except KeyboardInterrupt:
    print('\nExit')


# def get_location():
#     new_pos = pyautogui.locateOnScreen('h.png')

#     goto_pos = pyautogui.center(new_pos)

#     pyautogui.moveTo(goto_pos)

#     pyautogui.click()

# get_location()