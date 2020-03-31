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
