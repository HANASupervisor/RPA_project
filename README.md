# RPA_project
여기서는 개인적으로 공부하고 도전한 RPA 프로젝트를 올립니다.

## 학습목표
엑셀자동화, 문서자동화, flow자동화등 자동화에 관한 공부를 진행합니다.


## 폴더 구조
RPA_PROJECT/
├─ RPA_RealProject/   # 실사용/프로덕션용 RPA 코드
├─ RPA_Study/         # 학습/실습 예제 코드 및 샘플 파일
├─ venv/              # 파이썬 가상환경(보통 .gitignore로 제외)
├─ .gitignore         # Git 무시 규칙
└─ README.md          # 프로젝트 소개 문서





## 1~10: 엑셀 자동화 테크닉

| No. | 주제 | 핵심 내용 | 관련 파일 |
|---:|---|---|---|
| 01 | 워크북 생성·저장 | `Workbook()` 생성, 시트 활성화, `save()`/`close()` | - |
| 02 | 시트 관리 | 시트 추가/이름변경/순서변경/복사/삭제 (`create_sheet`, `ws.title`) | - |
| 03 | 셀 읽기·쓰기 | 단일/범위 셀 접근, 값 입력·가져오기, 반복문으로 대량 처리 | - |
| 04 | 서식 지정 | 너비/높이, 정렬, 폰트/채우기/테두리, 숫자서식 | - |
| 05 | 수식·집계 | `=SUM`, `=AVERAGE` 등 수식 입력, 수식 재계산 주의점 | - |
| 06 | 데이터 검색·필터링 | 특정 값/패턴 찾기, 범위 스캔, 조건부 추출 | `RPA_Study/6_search.py` |
| 07 | 삽입(Insert) | 행/열/범위 삽입, 셀 이동 없이 공간 만들기 (`insert_rows/columns`) | `RPA_Study/7_insert.py` |
| 08 | 삭제(Delete) | 행/열/범위 삭제, 불필요 시트·데이터 정리 (`delete_rows/columns`) | `RPA_Study/8_delete.py` |
| 09 | 범위 이동(Move) | 영역 이동·복사, 시프트 처리 (`move_range`) | `RPA_Study/9_move.py` |
| 10 | 차트 자동화 | 라인차트 등 생성/데이터 바인딩/축·제목 설정 | `RPA_Study/10_chart.py` |

### 예제 데이터
- `RPA_Study/sample*.xlsx` : 각 스크립트에서 사용하는 샘플 파일 모음

### 실행 방법
```bash
# 의존성 설치
pip install -r RPA_Study/requirements.txt

# 예: 6번 검색 예제 실행
python RPA_Study/6_search.py

# 예: 10번 차트 자동화 실행
python RPA_Study/10_chart.py