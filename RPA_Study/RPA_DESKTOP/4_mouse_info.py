import pyautogui
# pyautogui.mouseInfo()

# mouseInfo함수써서 자동화과정에서 필요한 버튼이 어느위치에 있는지 확인하는 것이 가능
# 아래는 해당하는 예시임.0 
# 70,34 49,50,50 #3132320
# 위 주소가 File이라는 버튼의 절대경로라 이 위치 입력해서 자동화코드 진행시키면됨. (x, y, R, G, B) # 문자


# 만약 자동화를 하던도중 예기치 못한 에러가 발생해서 중단을 시켜야하는 상황이 온다면?
# 마우스를 화면 4 귀퉁이중 한쪽에 넣으면 된다. 근데 너무 빠르게 자동화되면 마우스가 4귀퉁이로 가지못하고 가운데에서 도는 경우가 있다 그래서 초반세팅을 해줘야하는데 그때
# pyautogui.PAUSE 옵션을 이용하는것이 편리하다.
# pyautogui.FAILSAFE = False # 자동화도중 문제생기면 멈추라는 뜻이긴한데 별로 권장하는 방법은 아님 
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep을 적용
# pyautogui.lmouseInfo()


for i in range(5):
    pyautogui.move(100, 100)