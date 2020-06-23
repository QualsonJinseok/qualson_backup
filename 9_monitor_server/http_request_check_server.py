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
    print("스케쥴러 종료 요청")
    schedule_shutdown()
    return make_response("response 200", 200)

@app.route("/sched", methods=["GET"])
def sched_start():
    print("스케쥴러 시작 요청")
    if schedule_start() == 200:
        return make_response("response 200", 200)
    else:
        return make_response("response 500", 500)
#========================================
#↓↓↓↓↓↓↓↓↓↓↓ 서버 실행 구간 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
if __name__ == '__main__':
    schedule_start()    # 스케쥴러 실행
    app.run(host=HOST, port=PORT, debug=DEBUG, use_reloader=USE_RELOADER)