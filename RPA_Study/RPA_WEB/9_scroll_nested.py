from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')

browser.maximize_window()

time.sleep(5)

# 특정 영역까지 스크롤 
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[71]')


# 방법1. ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform() # action chain을통해 elem위치까지 이동하는걸 수행(perform) 해줘

# time.sleep(5)

# browser.quit()

# 방법2. 좌표정보 이용
# xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 쓰지마시오.
# print('type : ', type(xy))
# print('value : ', xy)

# 스크롤을 하지않더라도 해당 페이지랑 위치만 알면 스크롤안해도 클릭하는건 가능하다. 




elem.click()

time.sleep(5)

browser.quit()  