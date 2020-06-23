#-*- coding:utf-8 -*-
import os
import json
from flask import Flask, request, make_response, render_template
from slacker import Slacker
from threading import Thread
from pprint import pprint
from test_variable_info import *
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import atexit
import pprint
#============================
app = Flask(__name__)
#============================
#테스트 봇 토큰 호출
slack = Slacker(token)
#============================
#options = Options()
#options.add_argument("--start-maximized")
#============================
#테스트 스크립트 실행 구간
def run_test(channel, thread_ts, text_value):
    os.system('cd C:/Users/jinse/PycharmProjects/qualson/2.selenium_test_script')
    #플랫폼 구분하여 스크립트 실행
    if "웹" in text_value:
        slack.chat.post_message(channel, "처리 중입니다.", thread_ts=thread_ts)
        e = os.system('python od_selling_page_test_main.py')

    elif "모바일" in text_value:
        slack.chat.post_message(channel, "처리 중입니다.", thread_ts=thread_ts)
        e = os.system('python od_selling_page_test_main_mobile.py')

    else:
        slack.chat.post_message(channel, "'플랫폼' 명령어가 없습니다.", thread_ts=thread_ts)

    #스크립트 결과 확인
    if e == 0:
        print('test done')
        slack.chat.post_message(channel, "테스트 성공", thread_ts=thread_ts)
    else:
        print('test fail')
        slack.chat.post_message(channel, "테스트 실패", thread_ts=thread_ts)

#============================
def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]              # 메세지 발송 채널
    thread_ts = slack_event['event']['ts']                 # 쓰레드에 메시지를 보내기 위한 타임스탬프
    text_value = slack_event['event']['text']              # 슬랙 메시지 추출
    #parent_ts = slack_event['event']['thread_ts']          # 핀을 설정하기 위한 타임스탬프
    print(text_value)
    #슬랙 텍스트 구분에 따른 수행 케이스 분류
    if event_type == "app_mention":
        # text_value 분석
        if text_value == "<@UR3GU3P16>":
            slack.chat.post_message(channel, "명령어를 입력해주세요", thread_ts=thread_ts)
            return make_response("명령어 누락", 202)
        if "시작" not in text_value or "테스트" not in text_value:
            slack.chat.post_message(channel, "명령어를 다시 확인해주세요", thread_ts=thread_ts)
            return make_response("명령어 누락", 203)
        #
        if "테스트 시작" in text_value:
            # 테스트 수행 쓰레드 실행
            create_thread(channel, thread_ts, text_value)

            return make_response("정상 응답", 200)
        else:
            slack.chat.post_message(channel, "명령어를 확인해주세요.", thread_ts=thread_ts)
            return make_response("명령어 인식 불가", 201)

    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다." % event_type
    return make_response(message, 205, {"X-Slack-No-Retry": 1})

#============================
@app.route("/slack", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)
    print("이벤트 수신")
    print(slack_event)
    print('---')

    #인증 처리
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    #멘션 호출에 대한 처리
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)

    return make_response("슬랙 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry": 1})

#============================
@app.route("/result", methods=["POST"])
def hears_local_test():
    if request.method == "POST":
        if request.form['response_data'] != 200:
            result_data = request.form['test_issue']
            result_url = request.form['url_set'] + " 주소를 확인해주세요."
            print("result_data : ", result_data)
            if "Message: chrome not reachable" in result_data:
                return 'PASS'
            else:
                slack.chat.post_message('GR5MLV2CE', result_url)
                slack.chat.post_message('GR5MLV2CE', result_data) #thread_ts=thread_ts ==> 아직 인자를 넘겨받을 방법을 못찾음
                return 'OK'
    return "It's not a POST"
#============================
def create_thread(channel, thread_ts, text_value):
    # 쓰레드 메서드 호출
    run_thread = Thread(target=run_test, args=(channel, thread_ts, text_value))           # 메서드 대상 지정
    print("create thread")
    print('---')
    # daemon 속성이 False이면, 메인쓰레드가 종료되더라도 서브쓰레드는 작업이 끝날 때까지 계속 실행
    run_thread.setDaemon(False)
    print('테스트 쓰레드 시작 : ', run_thread)
    print('---')
    run_thread.start()

#============================
@app.route("/200", methods=["GET", "POST"])
def test_url():
    return make_response("return 200", 200)

@app.route("/404", methods=["GET", "POST"])
def test_url_2():
    return make_response("return 404", 404)

@app.route("/500", methods=["GET", "POST"])
def test_url_3():
    return make_response("return 500", 500)

#-----
@app.route("/message", methods=["GET"])
def test_url_4():
    message = "테스트입니다."
    slack.chat.post_message('GSYGK4VTR', message)
    return make_response("success", 200)

@app.route("/file", methods=["GET"])
def hello_photo():
    print("사진 전송 요청")
    print(slack.files.upload('제목 없음.png', channels="GR5MLV2CE"))
    return make_response("upload success", 200)
#============================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)