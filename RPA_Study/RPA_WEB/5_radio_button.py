import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# chrome드라이버 실행
browser = webdriver.Chrome()

# browser 창크기 최대화
browser.maximize_window()

# chrome드라이버 써서 해당 사이트로 접근
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # frame 전환

# frame안에 들어있는 radio 버튼을 가져온다. 
elem = browser.find_element(By.XPATH,'//*[@id="html"]') 

# 선택이 안되어있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼 선택되어있지않으면
    print('선택 안되어있으니까 선택해야지~')
    elem.click()
else:
    print('선택 되어있으니까 아무것도 하지않기')

time.sleep(5)



