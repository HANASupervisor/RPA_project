# iframe은 어떻게 생겼을까?

# <html>
#     <body>
#         <iframe id ='1'>
#             <html>
#                 <body>
#                     <div...>
#                 </body>
#             </html>
#         </iframe>
#         <iframe id ='1'>
#             <html>
#                 <body>
#                     <div...>
#                 </body>
#             </html>
#         </iframe>
#     </body>
# </html>

# //*[@id="html"]
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# chrome드라이버 실행
browser = webdriver.Chrome()

# chrome드라이버 써서 해당 사이트로 접근
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')  

# 브라우저로 해당 주소로 접근(이렇게하면 에러뜸, because iframe)
# elem = browser.find_element(By.XPATH, '//*[@id="html"]')

# 문제 해결시키자 상위 html파일에서 하위html부분을 찾아서 접근
browser.switch_to.frame('iframeResult')

# 접근완료했으면 해당 컴포넌트를 탐색
elem = browser.find_element(By.XPATH, '//*[@id="html"]')

# 해당 컴포넌트 클릭
elem.click()

# 하위프레임으로 들어가서 클릭을 완료했으면 다시 상위프레임으로 빠져나와야함. 
browser.switch_to.default_content()

# 상위프레임에서는 다시 이경로 못찾는거 보여드림 
# elem = browser.find_element(By.XPATH, '//*[@id="html"]')

# elem.click()



time.sleep(5)

browser.quit()