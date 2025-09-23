from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

# 번호 영어 수학
# 번호 (국어) 영어 수학

# ws.move_range('B1:C11', rows=0, cols=1) # B1부터 C11까지를 통째로 열을 오른쪽으로 한칸 옮긴다.
# ws['B1'].value ='국어'


# 번호 수학 영어
ws.move_range('C1:C11', rows=5, cols=-1)

wb.save('sample_korean.xlsx')