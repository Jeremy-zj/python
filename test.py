import pyautogui
import time

time.sleep(2)

#position = pyautogui.position()
#print(position)

#new_pos = pyautogui.locateOnScreen('h.png')
    
try:
    while True:
        pyautogui.scroll(-100000000)

        time.sleep(0.05)
         
        if new_pos == pyautogui.locateOnScreen('q.png'):
            goto_pos = pyautogui.center(new_pos)

            pyautogui.moveTo(goto_pos)

            pyautogui.click()

            break             
        else:
            pyautogui.scroll(-100000000)


except KeyboardInterrupt:
    print('\nExit')

#help_pos = pyautogui.locateOnScreen('h.png')

#goto_pos = pyautogui.center(help_pos)

#pyautogui.moveTo(goto_pos)

#pyautogui.click()



#print(help_pos)







#pyautogui.dragTo(1168, 200, button='left')

#pyautogui.mouseDown(button='left',x=700, y=200,duration=1)
#pyautogui.mouseUp(button='left')

#pyautogui.mouseDown(button='left',x=1100, y=200,duration=1)


#pyautogui.dragRel(300, None)

#  移动到(100, 200)位置，然后松开鼠标右键

