from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()

time.sleep(1)
browser.get('https://shopping.naver.com/ns/home')

wait = WebDriverWait(browser, 10)

# '무선 마우스' 입력
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div[2]/div/div[2]/div[1]/form/div/div/div/div/input').send_keys('무선 마우스')

# 2) '검색' 버튼을 텍스트로 찾고(버튼 자체), 클릭 가능 대기
search_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='검색']]"))
)

# 3) 일반 클릭 → 안 되면 JS로 우회 클릭
try:
    search_btn.click()
except Exception:
    browser.execute_script("arguments[0].scrollIntoView({block:'center'});", search_btn)
    browser.execute_script("arguments[0].click();", search_btn)

# 스크롤
# 지정한 위치로 스크롤 내리기
time.sleep(30)
browser.execute_script('window.scrollTo(0, 1080)') # 1920 *1080 (모니터 해상도에 따라 설정할 것)

# 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')


# 이번에는 정말 끝까지 스크롤을 계속내려서 마지막이 뜰때까지 내려가는 것
# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면
        break # 반복문 탈출(모든 스크롤 동작 완료)

    prev_height = curr_height






# 현재 문서 높이

time.sleep(100)