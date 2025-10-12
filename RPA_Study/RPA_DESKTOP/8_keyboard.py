# 어떤 프로그램을 키고 거기에 키보드로 입력하는것도 가능하다.
# 메모장 키고 글자 넣는것을 한번 해보자

import pyautogui

# for w in pyautogui.getAllWindows():
#     # print(w) # 모든 윈도우 가져오기
#     print(w.title)

w = pyautogui.getWindowsWithTitle('메모장')[0]
w.activate()

# pyautogui.write('123456789', interval=0.3)
# pyautogui.write('forrest gump', interval=0.5)
# 하지만 pyautogui의 경우 한글이 지원되지않는 치명적인 문제가 존재. 이문제는 추후에 해결법 추가해서 올리겠음. 

# pyautogui.write(['t', 'e', 's', 't', 'left', 'left', 'right', 'l', 'a', 'enter'], interval=0.25)
# 상단의 write에 left, right등의 옵션은 automate the boring stuff python

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown('shift') # shift key 누른상태에서
# pyautogui.press('4') # 숫자 4를 입력하고
# pyautogui.keyUp('shift') # shift key 뗀상태로 복구


# 조합키(Hot key)
# 전체 선택
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('a')
# pyautogui.keyUp('a') # press('a')
# pyautogui.keyUp('ctrl')


# 간편한 조합키
# pyautogui.hotkey('ctrl', 'alt', 'shift', 'a')
# ctrl 누르고 > alt 누르고 > shift 누르고 > A누르고 > A떼고 > shift 떼고 > alt떼고 > ctrl 떼고
# pyautogui.hotkey('ctrl', 'a')



# 이제 마지막으로 한글을 되게끔 해보자
import pyperclip
pyperclip.copy('포레스트 검프')
pyautogui.hotkey('ctrl', 'v')



# 이렇게 함수써서 작성하는거 가능
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

my_write('포레스트 검프')

# 자동화 프로그램 종료
# window: ctrl + alt + del
# mac: cmd + shift + option + q