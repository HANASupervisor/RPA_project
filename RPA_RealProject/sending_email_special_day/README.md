# 🎉 자동 명절 인사 이메일 발송 프로그램

네이버 SMTP 서버를 이용해 **설날 / 추석 명절 인사 메일을 자동 발송**하는 Python 스크립트입니다.

- 그룹(교수님 / 선생님 / 선배 / 가족 등)별로 **여러 개의 메시지 템플릿**을 설정할 수 있습니다.  
- 각 수신자에게는 해당 그룹 템플릿 중 **랜덤으로 하나의 메시지**가 발송됩니다.  
- `IS_NEW_YEAR` 값을 바꾸면 **설날 모드 / 추석 모드**를 전환할 수 있습니다.

> ⚠️ **중요**  
> 이 프로그램은 “오늘이 명절인지” 자동으로 판단하지 않습니다.  
> 실행 전에 반드시 **사용자가 직접 날짜와 모드(`IS_NEW_YEAR`)를 확인해야 합니다.**

---

## 🗂 목차
1. [프로그램 동작 구조](#program-flow)
2. [사전 준비](#prepare)  
3. [주요 설정 값](#mainSetting)  
4. [수신자 그룹 설정](#Set-up-a-recipient-group)  
5. [실행 방법](#how-to-do)  
6. [중요 유의사항](#important_note)  
7. [스케줄러 자동화](#Scheduler-Automation)  
8. [요약](#summary)  

---

## 📌 1. 프로그램 동작 구조 <a id="program-flow"></a>

프로그램은 다음 순서로 동작합니다.

1. 설정된 시각(`TARGET_HOUR`, `TARGET_MINUTE`)까지 **대기**
2. `IS_NEW_YEAR` 값에 따라 모드 결정
   - `True`  → 설날 메시지(`messages_new_year`)
   - `False` → 추석 메시지(`messages_chuseok`)
3. 각 그룹(`GROUPS`)의 수신자 목록을 순회하며:
   - 해당 그룹의 메시지 리스트에서 `random.choice()`로 **템플릿 1개 선택**
   - 네이버 SMTP 서버를 통해 **메일 발송**

---

## 📁 2. 사전 준비 <a id="prepare"></a>

### 2-1. Python 패키지 설치

```bash
pip install python-dotenv
```

## ✔ 네이버 메일 설정

1. **네이버 메일 → 환경설정**으로 이동  
2. **IMAP/SMTP 사용**을 활성화합니다.  
3. **앱 비밀번호**를 생성합니다.  
   - 일반 로그인 비밀번호가 아니라  
     SMTP용으로 별도로 발급받는 **앱 비밀번호**를 사용해야 합니다.


## ✔ `.env` 파일 생성

프로그램 파일과 동일한 폴더에 **`.env`** 파일을 생성한 뒤, 아래 내용을 작성합니다:

```env
NAVER_EMAIL=your_email@naver.com
NAVER_PASS=your_app_password
```
#main_setting
## ⚙️ 3. 주요 설정 값 설명<a id="mainSetting"></a>

### ▶ 발송 시간 설정
```python
TARGET_HOUR = 17
TARGET_MINUTE = 0
```

IS_NEW_YEAR = True   # 설날 모드 <br>
IS_NEW_YEAR = False  # 추석 모드

HOLIDAY_NAME = "설날" if IS_NEW_YEAR else "추석" <br>

messages_key = "messages_new_year" if IS_NEW_YEAR else "messages_chuseok"


# 👥 4. 수신자 그룹 설정<a id="Set-up-a-recipient-group"></a>
GROUPS 구조 예시
```python
GROUPS = [
    {
        "name": "교수님들",
        "recipients": ["email1@naver.com", "email2@gmail.com"],
        "messages_new_year": [...],
        "messages_chuseok": [...],
    },
]
```

### 키 설명<br>
| Key              | 설명                         |
|------------------|------------------------------|
| name             | 그룹 이름 (콘솔 출력용)      |
| recipients       | 이메일 주소 리스트           |
| messages_new_year| 설날용 메시지 템플릿 리스트 |
| messages_chuseok | 추석용 메시지 템플릿 리스트 |

### 메시지 템플릿 형식
```json
{
    "subject": "메일 제목",
    "body": f"{TARGET_TIME_KO}에 인사드립니다.\n본문 내용...",
}
```

## 각 항목 설명:

| Key    | 설명                     |
|--------|---------------------------|
| subject | 메일 제목                |
| body    | 메일 본문 (`\n` 줄바꿈 지원) |


## 🚀 5. 실행 방법<a id="how-to-do"></a>
### ✔ 실행 전 반드시 체크하세요

1. .env 설정이 올바른가?

2. IS_NEW_YEAR 값이 현재 명절(설/추석)과 맞는가?

3. 발송 시간(TARGET_HOUR, TARGET_MINUTE)이 원하는 시간인가?

4. 수신자 이메일 주소가 정확한가?
<br>

## ✔ 실행 명령어
```bash
python main.py
```

## ✔ 실행 예시 출력
⏳ 5시 00분 00초까지 대기중... 프로그램을 종료하지마세요<br>
📨 '교수님들' 그룹(2명)에게 설날 메일 발송 중...<br>
📨 '선생님들' 그룹(3명)에게 설날 메일 발송 중...

important_note
## ⚠️ 6. 매우 중요한 유의사항 (실수 방지)<a id="important_note"></a>
❗ 1) 프로그램은 “날짜”를 모릅니다

이 스크립트는 오늘이 설날인지 / 추석인지 자동으로 판단하지 않습니다.

예시:

오늘이 평범한 3월 12일인데
IS_NEW_YEAR = True 로 실행하면…

➡️ 설날 인사 메일이 실제 발송됩니다.

👉 사용자가 반드시 직접 날짜를 확인해야 합니다.

## ❗ 2) 테스트 없이 바로 실행 금지

처음 사용할 때는 반드시 테스트 실행을 해야 합니다.

아래처럼 send_mail()을 임시 변경:

```python
def send_mail(to_email, subject, body):
    print("=== [TEST MODE] ===")
    print("TO:", to_email)
    print("SUBJECT:", subject)
    print("BODY:", body)
    print("====================")
```


이 모드에서는 이메일이 발송되지 않고,
콘솔에 내용만 출력됩니다.

테스트 후 반드시 원래 SMTP 버전으로 되돌려야 합니다.

## ❗ 3) 서버 / PC 시간 주의

wait_until_target()는 시스템 시간을 사용합니다.

서버 시간이 한국 시간과 다르면
→ 실제 발송 시각도 달라질 수 있음

## ❗ 4) 네이버 SMTP 발송 제한

네이버는 단시간 과도한 SMTP 발송을 스팸으로 간주할 수 있습니다.

수신자가 많다면:

그룹을 나눠 여러 번 발송하거나

발송 간격을 두기를 권장합니다.

## ⏱ 7. 스케줄러 자동화<a id="Scheduler-Automation"></a>
### ✔ Linux (cron) 예시
```
0 17 10 2 * python3 /path/to/main.py
```

(매년 2월 10일 17:00 실행)

## ✔ Windows (작업 스케줄러)

프로그램: python.exe

인수: main.py 경로

트리거: 특정 날짜/시간

자동화 전 체크 리스트

IS_NEW_YEAR 값이 맞게 설정됨?

이메일 목록 최신 상태인가?

최소 1회 테스트 모드로 검증했는가?

## 📌 8. 요약<a id="summary"></a>

이 프로그램은 설날/추석 자동 인사 메일 발송기

그룹별 랜덤 문구 발송 기능 포함

날짜 인식 기능 없음 → 모든 설정은 사용자가 직접 체크해야 함

설정 실수 시 그대로 실제 메일이 발송됨

👉 따라서 “테스트 → 설정 확인 → 실제 실행” 순서를 반드시 지킬 것.