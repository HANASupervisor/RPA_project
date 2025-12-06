# ===============================
# 🎉 자동 명절 인사 이메일 발송 프로그램
#  - 네이버 SMTP 서버를 이용해 이메일 발송
#  - 클라우드/서버/PC 스케줄러에서 매일 실행하면
#    설날/추석 날짜에 자동으로 인사 메일을 보내줌
# ===============================

import os
from datetime import date, datetime
import time
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv 
import random  

# -------------------------------
# 📌 한국어 시간 표현(예: "5시 00분 00초")
# -------------------------------
def format_korean_time(hour: int, minute: int, second: int = 0)-> str:
    '''24시간제 hour, minute를 5시 00분 00초 형식의 문자열로 변환'''
    display_hour = hour
    if hour > 12:
        display_hour = hour - 12
    return f"{display_hour}시 {minute:02d}분 {second:02d}초"

## 이함수를 실행시키려고하는 시간대를 설정하는 함수 이거 설정해줘야함.
# ⚠️ 실행 전 확인! 반드시 시간 설정 변경할 것
# 지금은 17시 정각에 쏘는걸로 되어있음
TARGET_HOUR = 17
TARGET_MINUTE = 0
TARGET_TIME_KO = format_korean_time(TARGET_HOUR, TARGET_MINUTE)
# ⚠️ 실행 전 확인! 설날 / 추석 모드 설정
# 설날에 보낼 때: IS_NEW_YEAR = True
# 추석(한가위)에 보낼 때: IS_NEW_YEAR = False
IS_NEW_YEAR = True  # 👉 필요할 때 True/False 바꿔서 실행

HOLIDAY_NAME = "설날" if IS_NEW_YEAR else "추석"


# -------------------------------
# 📌 네이버 SMTP 서버 정보
# -------------------------------
# smtp.naver.com : 네이버 메일을 외부 프로그램에서 보낼 수 있게 해주는 서버 주소
# 포트 587 : TLS 기반 보안 연결에 사용하는 기본 포트
SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 587

# -------------------------------
# 📌 환경변수에서 계정 정보 읽기
# -------------------------------
# NAVER_EMAIL  : 보내는 사람 이메일 주소
# NAVER_PASS   : 네이버 앱 비밀번호 (일반 비번 X)
#   ※ 보안 지키기 위해 코드에 계정/비밀번호를 직접 적지 않고
#      OS 환경변수에서 가져오는 방식으로 처리
load_dotenv()

NAVER_EMAIL = os.environ['NAVER_EMAIL']
NAVER_PASSWORD = os.environ['NAVER_PASS']

# .env에 값이 없으면 에러를 내게끔 한다. 
if not NAVER_EMAIL or not NAVER_PASSWORD:
    raise RuntimeError("NAVER_EMAIL 또는 NAVER_PASS 환경변수가 설정되지 않았습니다.")


# -------------------------------
# 📌 이메일을 받을 사람 목록
# -------------------------------
# 여기에 "명절 인사 받을 사람들의 이메일 주소"를 넣으면 됨.
# 원하는 만큼 자유롭게 추가 가능.
# ====================================================
# ⚠️ 실행 전 확인! 그룹별 메일 수신자 & 문구 설정 영역
# ====================================================
GROUPS = [
    {
        "name": "교수님들",
        "recipients": [
            # "prof1@naver.com",
            # "prof2@naver.com",
        ],
        # 설날용 멘트 후보들
        "messages_new_year": [
            {
                "subject": "교수님, 새해 복 많이 받으십시오.",
                "body": f"{TARGET_TIME_KO}에 맞춰 새해 인사드립니다.\n"
                        f"지난 한 해 지도해 주심에 진심으로 감사드립니다. "
                        f"{HOLIDAY_NAME} 연휴 동안 편안한 쉼 되시고, 새해에도 건강과 평안이 함께하시길 기원드립니다.",
            },
            {
                "subject": "교수님, 희망 가득한 설 연휴 되십시오.",
                "body": f"{TARGET_TIME_KO}에 인사 올립니다.\n"
                        f"새해에는 교수님께서 계획하시는 일마다 좋은 결실이 함께하시길 바라며, "
                        f"늘 건강하시고 행복한 한 해 되시기를 기원드립니다.",
            },
            {
                "subject": "교수님, 설을 맞아 감사 인사드립니다.",
                "body": f"{TARGET_TIME_KO}에 감사의 마음을 전합니다.\n"
                        f"항상 많이 배우고 있습니다. "
                        f"{HOLIDAY_NAME} 연휴 잘 보내시고, 새해에도 잘 부탁드립니다.",
            },
        ],
        # 추석(한가위)용 멘트 후보들
        "messages_chuseok": [
            {
                "subject": "교수님, 풍성한 한가위 되십시오.",
                "body": f"{TARGET_TIME_KO}에 맞춰 한가위 인사드립니다.\n"
                        f"가족분들과 함께 건강하고 풍요로운 명절 보내시길 바랍니다.",
            },
            {
                "subject": "교수님, 즐거운 추석 연휴 보내고 계신가요?",
                "body": f"{TARGET_TIME_KO}에 감사 인사 올립니다.\n"
                        f"편안한 연휴 되시고, 하시는 일마다 좋은 결실이 함께하시길 기원드립니다.",
            },
            {
                "subject": "교수님, 한가위를 맞아 인사드립니다.",
                "body": f"{TARGET_TIME_KO}에 인사드립니다.\n"
                        f"늘 지도해 주심에 감사드리며, 풍성하고 따뜻한 명절 보내십시오.",
            },
        ],
    },
    {
        "name": "선생님들",
        "recipients": [
            # "teacher1@naver.com",
        ],
        "messages_new_year": [
            {
                "subject": "선생님, 새해 복 많이 받으십시오. 동북고 000입니다.",
                "body": f"{TARGET_TIME_KO}에 새해 인사드립니다.\n"
                        f"항상 가르침 감사드리며, {HOLIDAY_NAME} 연휴 동안 편안한 쉼 가지시길 바랍니다.",
            },
            {
                "subject": "선생님, 설 연휴 잘 보내고 계신가요?",
                "body": f"{TARGET_TIME_KO}에 안부 인사드립니다.\n"
                        f"새해에는 더욱 건강하시고, 기쁜 일들만 가득하시기를 기원합니다.",
            },
            {
                "subject": "선생님, 새해를 맞아 인사드립니다.",
                "body": f"{TARGET_TIME_KO}에 감사의 마음을 전합니다.\n"
                        f"가르쳐 주신 것 잊지 않고 열심히 살아가겠습니다. "
                        f"즐거운 {HOLIDAY_NAME} 되십시오.",
            },
        ],
        "messages_chuseok": [
            {
                "subject": "선생님, 즐거운 한가위 되십시오. 동북고 000입니다.",
                "body": f"{TARGET_TIME_KO}에 한가위 인사드립니다.\n"
                        f"늘 가르침 감사드리며, 편안하고 즐거운 추석 연휴 보내시길 바랍니다.",
            },
            {
                "subject": "선생님, 추석 연휴 잘 보내고 계신가요?",
                "body": f"{TARGET_TIME_KO}에 안부 전합니다.\n"
                        f"가족분들과 행복한 시간 보내시고, 늘 건강하시길 기원합니다.",
            },
            {
                "subject": "선생님, 풍성한 한가위 되십시오.",
                "body": f"{TARGET_TIME_KO}에 감사의 마음을 담아 인사드립니다.\n"
                        f"배운 것 잊지 않고 잘 간직하겠습니다. 즐거운 명절 되세요.",
            },
        ],
    },
    {
        "name": "형들",
        "recipients": [
            # "hyung1@naver.com",
        ],
        "messages_new_year": [
            {
                "subject": "형, 새해 복 많이 받으세요!",
                "body": f"{TARGET_TIME_KO}에 안부 전해요.\n"
                        f"{HOLIDAY_NAME} 연휴 맛있는 거 많이 드시고, 푹 쉬는 시간 보내셨으면 좋겠어요.",
            },
            {
                "subject": "형, 설 연휴 잘 보내고 있어요?",
                "body": f"{TARGET_TIME_KO}에 연락 드려요.\n"
                        f"올해도 많이 배우고 열심히 하겠습니다. 나중에 한번 밥 같이 먹어요!",
            },
            {
                "subject": "형, 새해 잘 시작하고 계신가요?",
                "body": f"{TARGET_TIME_KO}에 인사 남겨요.\n"
                        f"항상 챙겨주셔서 감사합니다. 새해에도 건강하고 행복하세요!",
            },
        ],
        "messages_chuseok": [
            {
                "subject": "형, 추석 잘 보내고 있어요?",
                "body": f"{TARGET_TIME_KO}에 안부 전해요.\n"
                        f"맛있는 거 많이 드시고, 푹 쉬면서 에너지 충전하는 연휴 되셨으면 좋겠습니다!",
            },
            {
                "subject": "형, 즐거운 한가위 되세요!",
                "body": f"{TARGET_TIME_KO}에 인사 남겨요.\n"
                        f"항상 챙겨주셔서 감사합니다. 이번 명절도 행복 가득하시길 바랄게요 🙂",
            },
            {
                "subject": "형, 명절 잘 보내고 계신가요?",
                "body": f"{TARGET_TIME_KO}에 연락드립니다.\n"
                        f"연휴 끝나고 또 한 번 같이 밥 먹어요! 즐거운 추석 보내세요.",
            },
        ],
    },
    {
        "name": "가족",
        "recipients": [
            # "family1@naver.com",
        ],
        "messages_new_year": [
            {
                "subject": "우리 가족, 새해 복 많이 받으세요.",
                "body": f"{TARGET_TIME_KO}에 인사 전해요.\n"
                        f"항상 고맙고 사랑합니다. 올해도 건강하고 행복하게 지내요 ❤️",
            },
            {
                "subject": "사랑하는 가족에게, 설날 인사 보냅니다.",
                "body": f"{TARGET_TIME_KO}에 마음을 담아 인사해요.\n"
                        f"멀리 있어도 마음은 항상 함께 있어요. 새해에도 더 자주 효도할게요!",
            },
            {
                "subject": "새해에도 잘 부탁해요, 우리 가족.",
                "body": f"{TARGET_TIME_KO}에 인사드립니다.\n"
                        f"지난 한 해 동안 고생 많았고, 올해는 더 많이 웃는 한 해 되길 바라요 😊",
            },
        ],
        "messages_chuseok": [
            {
                "subject": "가족들 모두, 즐거운 한가위 보내세요.",
                "body": f"{TARGET_TIME_KO}에 인사 전해요.\n"
                        f"항상 고맙고 사랑합니다. 건강하고 행복한 명절 보내요 ❤️",
            },
            {
                "subject": "우리 가족, 행복한 추석 보내자!",
                "body": f"{TARGET_TIME_KO}에 인사 남겨요.\n"
                        f"늘 믿어주고 응원해줘서 고마워요. 이번 명절도 웃을 일만 가득하길!",
            },
            {
                "subject": "사랑하는 가족에게 한가위 인사 보냅니다.",
                "body": f"{TARGET_TIME_KO}에 마음을 담아 인사해요.\n"
                        f"함께한 시간들 하나하나 다 소중해요. 많이 사랑합니다 😊",
            },
        ],
    },
]


# -------------------------------
# 📌 실제 이메일을 보내는 함수
# -------------------------------
def send_mail(to_email: str, subject: str, body: str):
    '''
    지정된 이메일 주소(to_email)로,
    제목(subject)과 내용(body)을 담은 메일을 보내는 함수
    '''

    # 이메일 메시지 객체 생성
    msg = EmailMessage()
    msg['From'] = NAVER_EMAIL # 보내는 사람
    msg['To'] = to_email      # 받는 사람
    msg['Subject'] = subject  # 메일 제목
    msg.set_content(body)     # 메일 본문 텍스트

    # SMTP 서버 접속 & 로그인 후 메일 발송
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()                          # TLS(보안 연결) 시작
        smtp.login(NAVER_EMAIL, NAVER_PASSWORD) # 네이버 계정 로그인
        smtp.send_message(msg)                  # 메일 보내기


# -------------------------------
# 📌 조금 빠르면 지정된 시각까지 대기하는 함수
# -------------------------------
def wait_until_target(hour: int, minute: int):
    '''지정된 시각까지 대기'''
    while True:
        now = datetime.now()
        if  now.hour == hour and now.minute == minute:
            return 
        time.sleep(1)


def main():
    print(f"⏳ {TARGET_TIME_KO}까지 대기중... 프로그램을 종료하지마세요")
    wait_until_target(TARGET_HOUR, TARGET_MINUTE)

    messages_key = "messages_new_year" if IS_NEW_YEAR else "messages_chuseok"

    # 그룹별로 돌면서, 각 그룹의 수신자들에게 서로 다른 메일 내용을 발송
    for group in GROUPS:
        name = group['name']
        recipients = group['recipients']

        # 수신자가 비어있으면 스킵(실수 방지용)
        # 비어있다는 멘트만 치고 넘어감
        if not recipients:
            print(f'⚠️ "{name}" 그룹에 수신자가 없어서 건너뜁니다.')
            continue

        messages = group.get(messages_key, [])
        if not messages:
            print(f'⚠️ "{name}" 그룹에 {HOLIDAY_NAME}용 메시지가 없어 건너뜁니다.')
            continue

        print(f"📨 '{name}' 그룹({len(recipients)}명)에게 {HOLIDAY_NAME} 메일 발송 중...")

        # 각 그룹내 인원 조회하면서 하나씩 메일 쏘기
        for r in recipients:
            # 위에서 이미 messages = group.get(messages_key, []) 한 상태라
            # 여기서는 그냥 그 리스트에서 랜덤으로 하나 뽑으면 됩니다.
            msg_template = random.choice(messages)
            subject = msg_template['subject']
            body = msg_template['body']

            send_mail(r, subject=subject, body=body)

if __name__ == "__main__":
    main()

