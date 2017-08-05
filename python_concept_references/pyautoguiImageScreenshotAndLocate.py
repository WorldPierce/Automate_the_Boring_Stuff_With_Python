import pyautogui

pyautogui.screenshot('c:\\screenshot.png') # returns pil object saves image file

pyautogui.locateOnScreen('c:\\image.png') # returns x,y, coords of where image is on screen

pyautogui.locateCenterOnScreen() # returns center of image you want
# then you can click at these coords
# images must be pixel perfect


