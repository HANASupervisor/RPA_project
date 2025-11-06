import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element(By.XPATH,'//*[@id="vehicle1"]')


if elem.is_selected() == False:
    print('선택 안되어있으니 선택해라')
    elem.click()
else:
    print('선택이 되어있으니 아무것도하지마라')


time.sleep(5)

browser.quit()