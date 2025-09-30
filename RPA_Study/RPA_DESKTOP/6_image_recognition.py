import pyautogui

# file_menu = pyautogui.locateOnScreen('file_menu.png')
# print(file_menu)

playbutton = pyautogui.locateOnScreen('playbutton.png')
pyautogui.moveTo(playbutton)

# checkbox가 여러개이고 거기서 여러개를 선택하게끔 하고싶을때 locateAllOnScreen 함수를 이용한다. 
# for i in pyautogui.locateAllOnScreen('checkbox.png'):
#     print(i)
#     pyautogui.click(i, duration = 0.25)