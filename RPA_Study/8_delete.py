from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active


# 삭제
# ws.delete_rows(8) # 8번째 줄에 있는 7번학생 데이터
# ws.delete_rows(8,3) # 8번째 줄부터 아래로 3개 지우기

# ws.delete_cols(2) # 2번째 열 B에 있는것을 삭제
ws.delete_cols(2, 2) # 2번째 열부터 2개를 삭제한다.
wb.save('sample_delete.xlsx')

