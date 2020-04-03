import pyautogui
import time
import schedule

time.sleep(1)

# L_pos = pyautogui.position()

# try:
#     while True:
#         N_pos = pyautogui.position()
#         if L_pos != N_pos:
#             print(N_pos)
#             L_pos = N_pos
# except KeyboardInterrupt:
#     print('\nExit')



# new_pos = pyautogui.locateOnScreen('h.png')

# goto_pos = pyautogui.center(new_pos)

# pyautogui.moveTo(goto_pos)

# pyautogui.click()
try:
    while True:

        pyautogui.scroll(-999999999)
        pyautogui.scroll(-999999999)
        pyautogui.scroll(-999999999)
        pyautogui.scroll(-999999999)
        
        pyautogui.moveTo(x= 336, y= 782)

        pyautogui.click()
        
        time.sleep(1)
        
        pyautogui.typewrite('py mouse.py')

        pyautogui.press('enter')

        pyautogui.moveTo(x= 195, y= 68)

        pyautogui.click()

except KeyboardInterrupt:

    print('\nExit')





# schedule.every().second.do(get_scroll)
# schedule.every().second.do(get_location)
# schedule.every().second.do(get_scroll2)




# try:
#     while True:  
#         schedule.run_pending()
#         time.sleep(1)

# except KeyboardInterrupt:
#     print('\nExit')
     

            