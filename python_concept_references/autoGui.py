import pyautogui # install pyautogui

width, height = pyautogui.size() # returns screen res

pyautogui.position() # returns mouse position

pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10, duration=1.5) # drags mouse to position

pyautogui.moveRel(200, 0) # move 200 pixels to the right
pyautogui.moveRel(0, -100) # move mouse up 100 pixels relative top current position

pyautogui.click(339,38) # click this position
pyautogui.doubleClick() # double click at current position

pyautogui.dragRel(300, 0) # drags mouse from current postion


pyautogui.displayMousePosition() # only works in terminal, tells you your mouse coordinates while you drag
