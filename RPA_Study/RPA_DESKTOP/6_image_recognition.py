import pyautogui

# file_menu = pyautogui.locateOnScreen('file_menu.png')
# print(file_menu)

# playbutton = pyautogui.locateOnScreen('playbutton.png')
# pyautogui.moveTo(playbutton)

# checkbox가 여러개이고 거기서 여러개를 선택하게끔 하고싶을때 locateAllOnScreen 함수를 이용한다. 
# for i in pyautogui.locateAllOnScreen('checkbox.png'):
#     print(i)
#     pyautogui.click(i, duration = 0.25)


# 하지만 locateOnScreen이라는 함수를 이용할때 화면 전체를 순차적으로 탐색하면서 찾다보니 처리시간이 오래걸린다는 문제가 발생한다. 
# 그래서 이러한점을 개선하기위한 아이디어 제안한다
# 1. GrayScale로 해서 색깔무시하고 하면 30%정도 개선하는게 가능하다고 공식문서에 나와있음.
# playbutton = pyautogui.locateOnScreen('playbutton.png', grayscale=True)
# pyautogui.moveTo(playbutton)

# 2. 범위 지정해서 찾을 범위를 줄여주면 금방 찾는다.
# playbutton = pyautogui.locateOnScreen('playbutton.png', region=(x,y,width,height))
# pyautogui.moveTo(playbutton)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen('playbutton.png', confidence=0.6)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print('발견 실패')


###########################################################################################
# 위처럼 코딩하면 한번에 발견못하면 바로 문제생김. 그래서 이런경우 while문 돌려서 발견할때까지 탐색한다.
# 1. 계속 기다리기
pyautogui.useImageNotFoundException(False)
# 자동화 대상이 바로 보여지지 않는 경우
file_menu_notepad = None

# 1. 계속 기다리기

while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen(
        'file_menu_notepad.png',
        confidence=0.75,      # 필요시 완화
        grayscale=True        # 필요시 완화
        # ,region=(x, y, w, h) # 가능하면 영역 제한
    )
    if file_menu_notepad is None:
        print('발견 실패')

pyautogui.click(file_menu_notepad)
#########################################################################




################################################################################################
# 2. 일정 시간동안 기다리기(TimeOut)

import time
import sys

timeout = 10 # 10초 대기
start = time.time() # 시작 시간 설정
file_menu_notepad = None
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
    end = time.time() # 종료 시간 설정
    if end - start > timeout: # 지정한 10초를 초과하면
        print('시간 종료')
        sys.exit()

pyautogui.click(file_menu_notepad)

# 매번 위와같이 코드를 짤수는 없음. 유지보수를 위해 함수형태로 만들어야함
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f'[Timeout {timeout}s] Target not found ({img_file}). Terminate program.')
        sys.exit()

my_click('file_menu_notepad.png', 10)

#####################################################################################
# 3.



