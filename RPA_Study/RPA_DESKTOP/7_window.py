# 프로그램 실행시킬때 프로그램 키고 해당 프로그램 전체화면 아닐경우 나타나는 위치가 제각각인데 
# 이걸 윈도우를 이용해서 프로그램의 위치를 받아오고 해당 좌표를 기반으로
# 어플리케이션 자동화가 가능하다. 

import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표정보

# pyautogui.click(fw.left + 10, fw.top + 20)


# # 이거 코드 실행되고있는 모든 코드 다 볼수 있음.
# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기
#     # print(w.title)


# for w in pyautogui.getWindowsWithTitle('제목 없음'):
#     print(w) # 모든 윈도우 가져오기


w = pyautogui.getWindowsWithTitle('제목 없음')[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화(맨 앞으로 가져오기)

if w.isMaximized == False: # 최대화 되지 않았다면
    w.maximize() # 최대화

# if w.isMinimized == False: # 최소화 되지 않았다면
#     w.minimize() # 최소화
pyautogui.sleep(2)

w.restore() # 화면 원래대로 복구시키기

pyautogui.sleep(2)

w.close() # 윈도우 닫기