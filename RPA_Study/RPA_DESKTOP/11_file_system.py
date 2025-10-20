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
# file_path = os.path.join(os.getcwd(), 'requirements.txt') # 현재 내 경로 + my_file.txt
# print(file_path)


# # 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r'C:\Users\USER\Desktop\RPA_project\my_file.txt'))

# 파일 정보 가져오기
# import time
# import datetime

# # playbutton.png파일로 접근하기위한 경로 이동
# print(os.getcwd())
# os.chdir('RPA_Study/RPA_EXCEL/')
# print(os.getcwd())

# # 파일의 생성 날짜
# ctime = os.path.getctime('problem1.xlsx') # playbutton이 만들어진 시간정보
# print(ctime) # 이거 시간 못알아보겠으니까 알아볼수있는 포맷으로 변환한다
# print(datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S')) # fromtimestamp, strftime함수 써서 알아 볼수 있는 포맷으로 변환

# # 파일의 수정날짜
# mtime = os.path.getmtime('problem1.xlsx')
# print(datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d %H:%M:%S')) # fromtimestamp, strftime함수 써서 알아 볼수 있는 포맷으로 변환

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime('problem1.xlsx')
# print(datetime.datetime.fromtimestamp(atime).strftime('%Y%m%d %H:%M:%S')) # fromtimestamp, strftime함수 써서 알아 볼수 있는 포맷으로 변환

# # 파일 크기
# size = os.path.getsize(file_path)
# print(size) # 바이트 단위로 파일 크기 가져오기



# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir('RPA_Study')) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# # 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk('RPA_Study') # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)


# for root, dirs, files in result:
#     print(root, dirs, files) # 3개의 값을 튜플로 반환


# # 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = '11_file_system.py'
# result = []
# for root, dirs, files in os.walk('.'):
#     if name in files:
#         result.append(os.path.join(root, name))
#         print(result)

# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern = '*.png' # .py로 끝나는 모든 파일
# result = []
# for root, dirs, files in os.walk('.'):
#     # print(files)
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))

# print(result)


# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir('RPA_Study')) # 이거 폴더임? True
# print(os.path.isfile('RPA_Study')) # 이거 파일임? False


# # 만약 지정된 경로에 해당하는 파일/ 폴더가 없다면? False반환함. 
# print(os.path.isdir('RPA_Studyㅇㅇㅇ')) # 이거 폴더임? False
# print(os.path.isfile('RPA_Studyㅇㅇㅇ')) # 이거 파일임? False

# # 그래서 False 뜨면 주어진 경로가 존재하는지를 반드시 확인해봐야함


# # 주어진 경로가 존재하는지 확인
# if os.path.exists('RPA_Study'):
#     print('파일 또는 폴더가 존재합니다.')
# else:
#     print('존재하지 않습니다.')


# # 파일 만들기
# open('new_file.txt', 'a').close() # 빈 파일 생성

# # 파일명 변경하기
# os.rename('new_file.txt', 'new_file_rename.txt')

# # 파일 삭제하기
# os.remove('new_file_rename.txt')

# # 폴더 만들기
# os.mkdir('new_folder') # 현재 경로 기준으로 폴더 생성

# # 만약 절대경로로 만들어주고싶으면 그냥 절대경로 넣으면됨
# os.mkdir('C:RPA_Study/new_folder')

# # 하위 폴더를 가지는 폴더 생성
### os.mkdir('new_folders/a/b/c') # 이렇게하면 하위 폴더를 가지는 폴더 생성 시도 이러면 실패함
# os.makedirs('new_folders/a/b/c') # 이렇게하면 하위 폴더를 가지는 폴더 생성 시도

# 폴더명 변경하기
# os.rename('new_folder', 'new_folder_rename')

# 폴더 지우기
# os.rmdir('new_folder_rename') # rmdir은 폴더안이 지워있을때만 삭제가능
# 그렇다면 폴더안이 비어있지않으면 어떻게 지워야할까?

# 아래 패키지를 이용하자
import shutil
# shutil.rmtree('new_folders') # 폴더 안이 비어있지 않아도 완전 삭제가능
# 모든 파일이 삭제될수 있으므로 주의!!!!!!!!!!!!!!!!


# # 파일 복사하기
# # 어떤 파일을 폴더 안으로 복사하기
# shutil.copy('playbutton.png', 'test_folder') # 원본 파일 경로, 대상 폴더 경로
# # 어떤 파일을 폴더안에 새로운 파일 이름으로 복사하기
# shutil.copy('playbutton.png', 'test_folder/copied_playbutton.png') # 원본 경로, 대상경로
# # copyfile을 쓸경우 디렉토리만하면안되고 안에 파일명까지 다 설정해줘야한다.
# shutil.copyfile('playbutton.png', 'test_folder/copied_playbutton1.png')

# shutil.copy2('playbutton.png', 'test_folder/copied_playbutton2.png')

# copy, copyfile: 메타정보 복사 X
# copy2: 메타정보 복사 O

# 폴더 복사
# shutil.copytree('test_folder', 'test_folder2') # 원본 폴더 경로, 대상 폴더 경로 *** 하위폴더까지 다 포함해서 복사됨

# # 폴더 이동
# shutil.move('test_folder3', 'test_folder')
shutil.move('test_folder_rename', 'test_folder')