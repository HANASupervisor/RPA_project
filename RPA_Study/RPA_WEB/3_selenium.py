from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 크롬 드라이버 실행 
# 크롬브라우저와 다르게 드라이버는 자동화코드가 실행된다.
service = Service(executable_path=r'../../chromedriver.exe')
browser = webdriver.Chrome(service=service)

# 드라이버에서 다음 홈페이지 접속한다.
browser.get('https://www.daum.net/')

# 다음 홈페이지에서 검색창에 해당하는 버튼을 클릭한다. 
elem = browser.find_element(By.XPATH, '//*[@id="q"]')
elem.click()

# 검색할 멘트 작성한다.
elem.send_keys('python')

# 엔터쳐서 검색한다.
elem.send_keys(Keys.ENTER)

# 방법 1. 5초 뒤에 스크린샷을 찍는다.
# time.sleep(5)

# 방법 2. URL이 변경되면 스크린샷을 찍는다. 
WebDriverWait(browser, 10).until(EC.url_contains('search'))

# 스크린샷 찍기
browser.save_screenshot('python.png')


# 10초뒤에 창 닫는다. 
time.sleep(10)

# # # daum 홈페이지 호출
# browser.get('https://daum.com')