# 크롬에서 내가 원하는 파일 다운로드 하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options

# 다운로드 경로 설정(이거 설치안하면 다운로드에 디폴트 경로로 그냥 다운로드가 진행됨. )
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory': r'C:\Users\USER\Desktop\RPA_project\RPA_Study\RPA_WEB', # : 저장할 '절대경로' (반드시 존재하는 폴더 권장)
                                                 'download.prompt_for_download': False,     # : 다운로드 위치 묻는 창(프롬프트) 표시 여부 -> False로 꺼야 자동 저장
                                                'download.directory_upgrade': True,        # : 과거에 사용하던 다운로드 경로 대신 '지금 지정한 경로'를 우선 사용
                                                'safebrowsing.enabled': True   })           #  : 일부 파일이 차단되어 멈추는 상황 방지(기본 True지만 명시)

# chrome 드라이버 실행 옵션을 적용해서 내가 원하는 경로로 다운받게 지정하는거 가능
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

# iframe안에 있어서 iframe안으로 들어가야함. 
browser.switch_to.frame('iframeResult')

# 내가 다운받고자하는 버튼 컴포넌트를 찾는다.
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click() # 클릭한다.

time.sleep(5) # 5초뒤에 끈다. 
browser.quit()