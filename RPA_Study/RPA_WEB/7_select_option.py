#  drop down option에서 설정하는 기능 자동화
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# chrome 드라이버 실행
browser = webdriver.Chrome()

# chrome드라이버에서 옵션있는 곳 선택해서 넘어가기
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

# frame 전환
browser.switch_to.frame('iframeResult')

# option 3번째꺼 찾아
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]')

# option중에 text가 opel인거 고르게 하는 방식으로 찾을수도 있음.
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()='Opel']')

# 텍스트 값이 부분 일치하는 항목 선택하는 방법 'Op'라는 단어가 들어간걸 모두찾음. 단 대소문자구분안해서 'op' 찾게하면 에러 발생함.
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Op")]')

# 3번째꺼 클릭해
elem.click()

time.sleep(5)
