import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save('screenshot.png') # 파일로 저장

# pyautogui.mouseInfo()
# 21,21 31,31,31 #1F1F1F

pixel = pyautogui.pixel(21,21)
print(pixel)

# print(pyautogui.pixelMatchesColor(28,18, (34, 167, 242)))
# print(pyautogui.pixelMatchesColor(28,18, pixel))
print(pyautogui.pixelMatchesColor(28,18, (34, 167, 243)))
