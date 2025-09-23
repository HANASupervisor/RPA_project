from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

from openpyxl.chart import BarChart, Reference, LineChart
# bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3) # B2:C11까지의 데이터를 차트로 생성
# bar_chart = BarChart() # 차트의 종류 설정 (Bar, Line, Pie, ...) 
# bar_chart.add_data(bar_value) # 차트 데이터 추가
# ws.add_chart(bar_chart, 'E1') # 차트 넣을 위치 정의

wb.save('sample_chart')
