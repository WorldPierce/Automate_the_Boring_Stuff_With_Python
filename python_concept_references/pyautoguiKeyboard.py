import pyautogui

pyautogui.click(100,100); pyautogui.typewrite('Hello world') #sends key clicks
pyautogui.typewrite('Hello world', interval=0.2)

pyautogui.typewrite(['b', 'a', 'left', 'left']) # left and right will use arrows
pyautogui.KEYBOARD_KEYS # returns list of all keyboard keys you can use like left and right

pyautogui.press('f1') # single key press

pyautogui.hotkey('ctrl', 'o') # used for keyboard shortcuts
