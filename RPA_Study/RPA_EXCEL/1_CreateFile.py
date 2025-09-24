from openpyxl import Workbook

wb = Workbook() # 새 워크북을 생성
ws  = wb.active # 현재 활성화된 sheet 가져오기

ws.title = 'project1' # sheet의 이름을 변경
wb.save('sample.xlsx') # 파일 저장
wb.close() # 파일 닫기