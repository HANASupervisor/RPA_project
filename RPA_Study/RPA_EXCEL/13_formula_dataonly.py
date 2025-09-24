from openpyxl import load_workbook
wb = load_workbook('sample_formula.xlsx', data_only=True) 
# data_only option이 없으면 12에 저장된 함수자체를 가져옴
# 하지만 data_only함수 넣으면 숫자 제대로 불러옴.

ws = wb.active

# 수식이 아닌 실제 데이터를 가지고 옴.
# evaluate 되지않은 상태의 데이터는 None이라고 표시됨.
# 이 말 쉽게 설명함. openpyxl에 엑셀 함수 집어넣어놨으면 data_only옵션 없으면 함수뜨고
# 옵션있으면 데이터를 불러오는데 함수가 들어가있기때문에 들어있는값은 없으니까 None뜸. 
# 하지만 이때 엑셀 들어가서 다시 저장하고 들어오면 이게 엑셀에서 저장버튼누를때 함수가 호출되면서 값이 저장되기때문에
# 그이후 파이썬에서 코드 돌리면 제대로 숫자가 긁히는 것을 알 수 있다. 


for row in ws.values:
    for cell in row:
        print(cell)