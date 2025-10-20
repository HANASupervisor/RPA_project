# Quiz: 아래 동작을 자동으로 수행하는 프로그램을 작성하시오.

# 1. 그림판 실행(단축키: win + r, 입력값: mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
# - 입력 글자: "참 잘했어요."

# 3. 5초 대기 후 그림판 종료
#  이때, 저저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함. 



# Quiz: 아래 동작을 자동으로 수행하는 프로그램을 작성하시오.
import pyautogui
import pyperclip
# 1. 그림판 실행(단축키: win + r, 입력값: mspaint) 및 최대화
pyautogui.keyDown('win')
pyautogui.keyDown('r')
pyautogui.keyUp('r')
pyautogui.keyUp('win')
pyautogui.write('mspaint')
# 위와같이 keydown keyup써서 해도되고 그냥 hotkey로 간단하게 해결해도가능
pyautogui.hotkey('enter')
pyautogui.sleep(1)


# 화면 최대화
windows = pyautogui.getAllWindows()
cands = [w for w in windows if w.title and ('그림판' in w.title or 'paint' in w.title.lower())]



draw_page = cands[0]
draw_page.activate()
try:
    draw_page.maximize()
except:
    pass

if not draw_page.isMaximized:
    draw_page.maximize()

pyautogui.sleep(0.5)

# 마우스 화면 중앙으로 이동 
cx = draw_page.left + draw_page.width // 2
cy = draw_page.top + int(draw_page.height * 0.55)  # 리본 아래 안전지대


# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
# - 입력 글자: "참 잘했어요."
pyautogui.hotkey('t') # 글자쓰기위해 단축키 클릭
pyautogui.sleep(2) # 2초뒤에 마우스 가운데로 글쓰기위해 이동
pyautogui.moveTo(cx, cy)
pyautogui.click() #가운데로 이동된 상태에서 클릭
pyautogui.sleep(2)
pyperclip.copy('참 잘했어요.') # 2초뒤에 참잘했어요 문구 복붙
pyautogui.hotkey('ctrl', 'v')



# 3. 5초 대기 후 그림판 종료
#  이때, 저저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함. 
pyautogui.sleep(5)
x= 1900; y= 26
pyautogui.moveTo(x,y)
pyautogui.click()
# pyautogui.hotkey('ctrl', 's')
# pyautogui.sleep(3)
# pyautogui.hotkey('alt', 'f4')