# -*- coding: utf-8 -*-
from import_lib import *

# 실행 스크립트 확인
# with open("app.txt", "r") as file:
#     # app_name = file.read()
#     data = file.read().split()
#     app_name = data[0]
#     if len(data) == 2:
#         app_name_2 = data[1]
#         print(app_name_2)

with open("run_info.csv", "r") as file:
    global run_info
    run_info = dict()
    data = csv.reader(file)
    for n in data:
        run_info[n[0]] = n[1]
    app_name = run_info['product']
# print(run_info)

## 버전명
version = "200409_1.0.0"
###################################################################################
# Debugging Mode == True : 개발 환경 // False : 라이브 환경
with open("setting.txt", "r") as file:
    set = file.read()
if set == 'test':
    test_mode = True
elif set == 'real':
    test_mode = False

## MAC
mac_host = "name"
###################################################################################
## Main info
# 윈도우 스케쥴러 타이밍 == ex. 10분
# 스크립트 내, 라인업 구분 == 20분 단위로 설정
###################################################################################
# 실행 OS ==> 추후 위와 같이 분기처리
# platform = "Android"            # Android // iOS
device_type = run_info['OS']
###################################################################################
## Slack Bot 환경 셋팅
slack_token = 'secret'
slack = Slacker(slack_token)        # Bot 선언
###################################################################################
# device & slack setting
# 개발 PC == secret // 라이브 PC == secret
# dev phone == secret // live phone == secret
# 테스트 채널 == secret // 메인 채널 == secret

if test_mode == True:
    device_id = "secret"
    device_platform_ver = "10.0.0"
    device_name = "GalaxyS10"
    phone_number = 'secret'
    slack_channel = 'secret'

# # 테스트 환경 2
# if test_mode == True:
#     device_id = "R39M2014CZL"
#     device_platform_ver = "10.0.0"
#     device_name = "GalaxyS10"
#     phone_number = 'secret'
#     slack_channel = 'secret'

# 실제 라이브 서비스 환경
elif test_mode == False:
    device_id = "secret"
    device_platform_ver = "10.0.0"
    device_name = "GalaxyS10"
    phone_number = 'secret'
    slack_channel = 'secret'
###################################################################################
# app package setting
if app_name == "britenglish":
    app_package = "com.qualson.britenglish"
    app_package_activity = "com.qualson.britenglish.splash.SplashActivity"
    app_package_kr = '브릿잉글리쉬'
    local_url = '127.0.0.1'
    PORT = "4725"
    appium_address = local_url + ":" + PORT + "/wd/hub"

if app_name == "realclass":
    app_package = "com.qualson.realclass"
    app_package_activity = "com.qualson.realclass.splash.SplashActivity"
    app_package_kr = '리얼클래스'
    local_url = '127.0.0.1'
    PORT = "4726"
    appium_address = local_url + ":" + PORT + "/wd/hub"

if app_name == "drmuzy":
    app_package = "com.qualson.drmuzy"
    app_package_activity = "com.qualson.drmuzy.splash.SplashActivity"
    app_package_kr = '닥터뮤지'
    local_url = '127.0.0.1'
    PORT = "4727"
    appium_address = local_url + ":" + PORT + "/wd/hub"

if app_name == "instagram":
    app_package = "com.instagram.android"
    app_package_activity = "com.instagram.mainactivity.MainActivity"
    app_package_kr = '인스타그램'
    local_url = '127.0.0.1'
    PORT = "4728"
    appium_address = local_url + ":" + PORT + "/wd/hub"

if app_name == "facebook":
    app_package = "com.facebook.katana"
    app_package_activity = "com.facebook.account.login.activity.SimpleLoginActivity"
    app_package_kr = '페이스북'
    local_url = '127.0.0.1'
    PORT = "4729"
    appium_address = local_url + ":" + PORT + "/wd/hub"

###################################################################################
## Appium 환경 셋팅
desired_caps = {
  "platformName": device_type,
  "platformVersion": device_platform_ver,
  "deviceName": device_name,
  "udid": device_id,
  "noReset": "true",
  "appPackage": app_package,
  "appActivity": app_package_activity,
  "automationName": "UiAutomator2",
  "unicodeKeyboard" : "true"
}
# print(desired_caps)
###################################################################################
## Google Vision 환경 셋팅
if desired_caps['platformName'] == 'Android':
    if test_mode == True:
        # AOS_GoogleVisionPath = 'C:\\Users\\jinse\\PycharmProjects\\qualson_project\\11_pre_source\\google_vision.json'
        AOS_GoogleVisionPath = 'C:\\Users\\jinse\\PycharmProjects\\qualson_project\\13_Appium_Projects_ver2\\google_vision.json'
        #
    elif test_mode == False:
        AOS_GoogleVisionPath = 'C:\\Projects_ver2\\bin\\google_vision.json'
    # Google Vision API 사용
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=AOS_GoogleVisionPath   # 구글 Vision API 인증
elif desired_caps['platformName'] == 'iOS':
    if test_mode == True:
        # IOS_Google Vision
        IOS_GoogleVisionPath = '/Users/' + mac_host + '/Projects/build/autotest-2cc76fcdb1f61.json'
    # elif test_mode == False:
        # IOS_GoogleVisionPath =
    # Google Vision API 사용
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=IOS_GoogleVisionPath   # 구글 Vision API 인증
###################################################################################