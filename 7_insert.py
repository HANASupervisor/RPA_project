# 엑셀 파일에서 우클릭해서 삽입눌러서 행과 행사이에 간격만드는 코드
from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

# ws.insert_rows(8) # 8번째 줄이 비워짐
# ws.insert_rows(8,5) # 이렇게하면 8번째 위치에 5줄 추가됨.
# ws. insert_cols(2,3)

wb.save('sample.xlsx')
