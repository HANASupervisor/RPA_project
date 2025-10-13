# 자동화를 하다보면 파일을 다룰일이 많음
# 텍스트파일에 이름정보를 넣어서 
# 각각한줄씩읽어와서 자동화 수행
import os
# print(os.getcwd()) # 현재 디렉토리
# os.chdir('RPA_Study')
# print(os.getcwd()) # 현재 디렉토리

# os.chdir('..') # 상위 디렉토리로 이동
# print(os.getcwd()) # 현재 디렉토리
# os.chdir('../..')
# print(os.getcwd()) # 현재 디렉토리
# os.chdir('c:/')
# print(os.getcwd()) # 현재 디렉토리

# 절대 경로로 파일경로를 만들어야하는 경우도 있음
file_path = os.path.join(os.getcwd(), 'requirements.txt') # 현재 내 경로 + my_file.txt
print(file_path)


# # 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r'C:\Users\USER\Desktop\RPA_project\my_file.txt'))

# 파일 정보 가져오기
import time
import datetime

# playbutton.png파일로 접근하기위한 경로 이동
print(os.getcwd())
os.chdir('RPA_Study/RPA_EXCEL/')
print(os.getcwd())

# 파일의 생성 날짜
ctime = os.path.getctime('problem1.xlsx') # playbutton이 만들어진 시간정보
print(ctime) # 이거 시간 못알아보겠으니까 알아볼수있는 포맷으로 변환한다
print(datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S')) # fromtimestamp, strftime함수 써서 알아 볼수 있는 포맷으로 변환

# 파일의 수정날짜
mtime = os.path.getmtime('problem1.xlsx')
print(datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d %H:%M:%S')) # fromtimestamp, strftime함수 써서 알아 볼수 있는 포맷으로 변환

# 파일의 마지막 접근 날짜
atime = os.path.getatime('problem1.xlsx')
print(datetime.datetime.fromtimestamp(atime).strftime('%Y%m%d %H:%M:%S')) # fromtimestamp, strftime함수 써서 알아 볼수 있는 포맷으로 변환

# 파일 크기
size = os.path.getsize(file_path)
print(size) # 바이트 단위로 파일 크기 가져오기