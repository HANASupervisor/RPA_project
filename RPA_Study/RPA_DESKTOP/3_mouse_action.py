import pyautogui

# 파일명을 클릭하게 해보자 
pyautogui.sleep(10) # 10초 대기
# print(pyautogui.position()) # 내 현자 마우스의 위치를 찾는다. 



# Point(x=75, y=18): 이 좌표가 File의 위치임. 
# pyautogui.click(75,18, duration=1)



# 위함수를 보면 click 함수가 있는데 
# 이 click함수는 mouseDown(), mouseUp() 이라는 2가지 함수를 합친 것이다.
# pyautogui.click(clicks=500) # 500번 클릭하기 그래서 위에 sleep함수랑 같이써서 그림판에 3초동안 500번 클릭하는거 가능 
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.doubleClick()


# # 그럼 (200, 200)에서 (300, 300)으로 선을 그어보자
# pyautogui.moveTo(1000, 1000)
# pyautogui.mouseDown()
# pyautogui.move(1200, 1200, duration=10)
# pyautogui.mouseUp()


# pyautogui.rightClick()# 마우스 우클릭
# pyautogui.middleClick() #마우스 휠을 조절할수 있음. 


# 마우스로 드래그앤 드랍으로 창을 움직여보자
# print(pyautogui.position())
# pyautogui.moveTo(1198,593)
# pyautogui.drag(100, 0)
# 이렇게하면 마우스이동만하고 창이 움직이지않는것처럼 보인다. 너무빨라서 그런거임. 그래서 이문제를 해결하기위해서는 duration을 적용한다. 


# duration 적용한 버전 
# pyautogui.moveTo(1198,593)
# pyautogui.drag(200, 0, duration=3)
# 이러면 제대로 적용되어서 메모장이 제대로 이동하는 것을 확인할 수 있다. 

# 절대좌표로 움직이는 것도 보여줄수 있다. 
# pyautogui.dragTo(1598,593, duration=6)



pyautogui.scroll(-800) # 양수이면 위방향으로, 음수이면 아래방향으로 300만큼 스크롤