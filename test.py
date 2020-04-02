import pyautogui
import time
import cv2 as cv
import numpy as np
import mss
import warnings

warnings.filterwarnings("ignore")

time.sleep(2)

#position = pyautogui.posith.png
#print(position)

old_pos = pyautogui.locateOnScreen('h.png')

def get_location():
    new_pos = pyautogui.locateOnScreen('g.png')

    goto_pos = pyautogui.center(new_pos)

    pyautogui.moveTo(goto_pos)

    pyautogui.click()

gu = cv.imread('g.png',0)
#tw, th = gu.shape[::-1]

with mss.mss() as sct:
    monitor = {'top': 0 , 'left': 0, 'width': 1280 , 'height': 800}
    
try:
    while 'Screen capturing':
        #pyautogui.scroll(-100000000)

        #time.sleep(0.05)

        img = np.array(sct.grab(monitor))
 
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        res2 = cv.matchTemplate(img_gray, gu, cv.TM_CCOEFF_NORMED)

        # sift=cv.xfeatures2d.SIFT_create()
        # kp1,des1=sift.detectAndCompute(res2,None)
        # kp2,des2=sift.detectAndCompute(gu,None)

        # #定义FLANN匹配器
        # indexParams=dict(algorithm=0,trees=10)
        # searchParams=dict(checks=50)
        # flann=cv.FlannBasedMatcher(indexParams,searchParams)
        # #使用KNN算法实现图像匹配，并对匹配结果排序
        # matches=flann.knnMatch(des1,des2,k=2)
        # matches=sorted(matches,key=lambda x:x[0].distance)
            
        #get_location()

        # threshold = 0.1
 
        # loc2 = np.where(res2 >= threshold) 

        # for pt in zip(*loc2[::-1]):
        #     cv.rectangle(img, pt, (pt[0] + tw, pt[1] + th), (0, 0, 255), 2)      
        
        get_location()

    else:
        pyautogui.scroll(-100000000)

        time.sleep(0.05)

        #cv.imshow('OpenCV/Numpy normal', img)

        # if cv.waitKey(0) == ord('q'):
        #     cv.destroyAllWindows()
        #     break


except KeyboardInterrupt:
    print('\nExit')







#pyautogui.dragTo(1168, 200, button='left')

#pyautogui.mouseDown(button='left',x=700, y=200,duration=1)

#pyautogui.mouseUp(button='left')

#pyautogui.mouseDown(button='left',x=1100, y=200,duration=1)

#pyautogui.dragRel(300, None)


