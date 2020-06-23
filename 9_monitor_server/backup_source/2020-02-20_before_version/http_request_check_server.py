from config_info import *
from import_server_module import *
from sched_function import *
#-----
import json
import time
import atexit
import requests
import telegram
import pyautogui
import subprocess
import pyperclip
from datetime import datetime
from slacker import Slacker
from selenium import webdriver
from flask import Flask, make_response
#from flask_apscheduler import APScheduler
from selenium.webdriver.chrome.options import Options
#from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
#=========================================
#↓↓↓↓↓↓↓↓↓↓↓↓ 기본 구동 셋팅 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#=========================================
app = Flask(__name__)   # 플라스크 객체 생성
# options = Options()     # 셀레늄 실행 옵션 설정
# options.add_argument("--start-maximized")
# slack = Slacker(token)  # 슬랙봇 생성
#tm_bot = telegram.Bot(token=tm_token)
#=========================================
#-----------------------------------------
#↓↓↓↓↓↓↓↓↓↓↓↓ 메시지 발송 함수 ↓↓↓↓↓↓↓↓↓↓↓↓
#-----------------------------------------
'''
def time_now():
    return str(datetime.now())[:-7]

def send_kakao_message(message):
    try:
        if kakao_setting == False:
            print("kakao setting value is False")
            return "Do not Send Message"
        PATH = "C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"
        subprocess.Popen(PATH)      # 카카오톡 실행
        pyautogui.moveTo(1790,700)  # 카카오톡 채팅방으로 커서 이동하기
        time.sleep(3)
        pyautogui.doubleClick(x=1790, y=700, button='left', interval=0.3)   # 더블클릭
        pyperclip.copy(message)             # 입력 메시지 복사
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.typewrite('hello world') # 글을 적는 곳의 IME가 한글로 설정되어 있다면 영타로 쳐서 한글입력 가능
        pyautogui.press('enter')
        time.sleep(1)
    except Exception as e:
        print(e)

def send_slack_message(message):
    try:
        # 슬랙 채팅방 셋팅
        if channel_switch is True:
            slack_channel = real_channel
        else:
            slack_channel = test_channel
        slack.chat.post_message(slack_channel, message)
        return "Success to Send Slack Mesasge"
    except Exception as e:
        print(e)
        return "Fail to Send Slack Message"
#========================================
# 성공 시, 실서버 url을 체크하는 루틴 수행
#========================================
def auto_check_browser(url_status, url_info):
    driver = webdriver.Chrome(options=options)
    driver.get(url_info)
    driver.implicitly_wait(3)
    null_sample = ["", " "]
    time.sleep(1)
    if driver.find_element_by_xpath("//div").text == null_sample[0]:
        message = "[" + time_now() + "] " + url_info +" Page Script is None \n cc.<@UL8T21UAK><@UNWSR3FFF><@USD8GCJLV>"
        print(message)
        send_slack_message(message)
        driver.quit()
        return "Page Script is None"

    response_result = driver.find_element_by_xpath("//div/div").text
    #print("response result :", response_result)
    if "Page Not Found" in response_result:
        print("[" + time_now() + "]" + " Page Not Found 문자열이 포함되어 있음")
        driver.quit()
        message = "[" + time_now() + "] " + url_info + " URL Response : " + str(url_status) + " == Page Not Found <!channel>"
        send_slack_message(message)
        #send_kakao_message(message)
        #tm_bot.sendMessage(chat_id=err_channel, text=message)
        return "Page Not Found"

    elif "404 NOT FOUND" in response_result:
        print("[" + time_now() + "]" + " 404 NOT FOUND 문자열이 포함되어 있음")
        driver.quit()
        message = "[" + time_now() + "] " + url_info + " URL Response : " + str(url_status) + " == 404 NOT FOUND <!channel>"
        send_slack_message(message)
        #send_kakao_message(message)
        #tm_bot.sendMessage(chat_id=err_channel, text=message)
        return "404 NOT FOUND"

    else:
        print("[" + time_now() + "]" + " 페이지 정상 로드")
        message = "[" + time_now() + "] " + url_info + " URL Response : " + str(url_status) + " == Page is Alive \n cc.<@UL8T21UAK><@UNWSR3FFF><@USD8GCJLV>"
        send_slack_message(message)
        #send_kakao_message(message)
        #tm_bot.sendMessage(chat_id=run_channel, text=message)
        driver.quit()
        return "Load Success"
#========================================
def url_test_code(url_info):
    url_status = requests.get(url_info, timeout=3).status_code
    if url_status >= 200 and url_status < 300:
        print("[" + time_now() + "]" + " OkDoctor response 200. But we need to double check")
        auto_check_browser(url_status, url_info)        #성공 시, 실제 url 체크하는 함수 실행

    if url_status >= 400 and url_status < 500:
        print("[" + time_now() + "]" + " OkDoctor Fail to Page Load")
        message = "[" + time_now() + "] " + url_info + " URL Response : " + str(url_status) + " == Fail to Page Load <!channel>"
        send_slack_message(message)

    if url_status >= 500:
        print("[" + time_now() + "]" + " Server Error")
        message = "[" + time_now() + "] " + url_info + " URL Response : " + str(url_status) + " == Server Error <!channel>"
        send_slack_message(message)
#========================================
#↓↓↓↓↓↓↓↓↓↓↓↓ API 체크 루틴 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
def get_access_token():
    # basic auth 인증
    try:
        access_token = requests.post(AUTH_URL, data=FORM_DATA, auth=(ID, PW))
        token_status = access_token.status_code
        if token_status == 200:
            token_data = json.loads(access_token.text)["result"]['access_token']
            print("[" + time_now() + "]" + " GET token success")
            HEADERS = {
                "osType": "ANDROID",
                "osVersion": "10.2.1",
                "appVersion": "1.0.0",
                "Authorization": "bearer " + token_data
            }
            return token_status, HEADERS
    except Exception as e1:
        print("[" + time_now() + "]" + e1)
        message = "[" + time_now() + "]" + " 호스트에서 연결을 거부하여, Basic Auth token 수집 실패"
        send_slack_message(message)
        #send_kakao_message(message)

def vedio_play_check(url_info):
    try:
        tuple_data = get_access_token()     # (token_status, HEADERS)
        if tuple_data[0] == 200:
            play_check = requests.get(url_info.format(upc=UPC), headers=tuple_data[1])
            print("content status:", play_check.status_code)
            message = "[" + time_now() + "]" + " Glad you came 컨텐츠 로드 성공"
            send_slack_message(message)
        else:
            message = "[" + time_now() + "]" + " Glad you came 컨텐츠 로드 실패 <!channel>"
            send_slack_message(message)
            #send_kakao_message(message)
    except Exception as e2:
        message = "[" + time_now() + "]" + e2
        print(message)
        send_slack_message(message)
#========================================
#↓↓↓↓↓↓↓↓↓↓↓↓↓ 스케쥴링 등록 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
sched = BackgroundScheduler(daemon=True)
#sched = BlockingScheduler(dameon=True)     # 이걸 쓰면 서버구동과 스케쥴링을 동시에 실행 불가
#------
#인터벌 방식
#TEST CODE
#sched.add_job(func=url_test_code, args=(url_list[0],), trigger='interval', seconds=10)
#sched.add_job(func=vedio_play_check, args=(URL_SET,), trigger='interval', seconds=5)
#sched.add_job(func=url_test_code, trigger='interval', minutes=15)
#------
#크론 방식 == ex) 각 5배수 분의 10, 30초마다 실행 -> (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
#sched.add_job(url_test_code, 'cron', minute='*/5', second='10, 30')
#SERVICE CODE
sched.add_job(func=url_test_code,  args=(url_list[0],), trigger='cron', minute='*/15')     # URL 체크 루틴 1
sched.add_job(func=url_test_code,  args=(url_list[1],), trigger='cron', minute='*/30')     # URL 체크 루틴 2
sched.add_job(func=vedio_play_check, args=(URL_SET,), trigger='cron', minute='*/20')       # API 체크 루틴
#-----
sched.start()
#-----
atexit.register(lambda : sched.shutdown(wait=False))
atexit.register(lambda : sched.shutdown(wait=False))
atexit.register(lambda : sched.shutdown(wait=False))

def add_sched_job():
    sched.add_job(func=vedio_play_check, args=(URL_SET,), trigger='cron', minute='*/20')

def regis_shutdown():
    atexit.register(lambda: sched.shutdown(wait=False))
    
'''
#========================================
#↓↓↓↓↓↓↓↓↓↓↓ 헬스 체크 라우터 ↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
@app.route("/echo", methods=["GET"])
def echo_check():
    print("에코 응답 요청")
    return make_response("Server is Alive", 200)

@app.route("/file", methods=["GET"])
def slack_send_file():
    print("사진 전송 요청")
    slack.files.upload('제목 없음.png', channels=slack_channel)
    return make_response("upload success", 200)

@app.route("/shutdown", methods=["GET"])
def sched_shutdown():
    schedule_shutdown()
    return make_response("response 200", 200)

@app.route("/sched", methods=["GET"])
def sched_start():
    if schedule_start() == 200:
        return make_response("response 200", 200)
    else:
        return make_response("response 500", 500)
#========================================
#↓↓↓↓↓↓↓↓↓↓↓ 서버 실행 구간 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
if __name__ == '__main__':
    schedule_start()    # 스케쥴러 실행
    app.run(host=HOST, port=PORT, debug=DEBUG, use_reloader=False)