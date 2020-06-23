from import_server_module import *
from config_info import *
from script_path import *
#========================================
options = Options()     # 셀레늄 실행 옵션 설정
options.add_argument("--start-maximized")
slack = Slacker(token)  # 슬랙봇 생성
# logging.basicConfig()   #로거 셋팅
# logging.getLogger('apscheduler').setLevel(logging.INFO)
#-----------------------------------------
#↓↓↓↓↓↓↓↓↓↓↓↓ 메시지 발송 함수 ↓↓↓↓↓↓↓↓↓↓↓↓
#-----------------------------------------
def time_now():
    return str(datetime.now())[:]   #-7

def time_print():
    print(time_now())
    print('---')

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
        return 200, "Success to Send Slack Mesasge"
    except Exception as e:
        print(e)
        return 404, "Fail to Send Slack Message"
#========================================
# 성공 시, 실서버 url을 Selenium 으로 체크
#========================================
def auto_check_browser(package, url_info, browser):
    try:
        package_list = ["drmuzy", "realclass", "homeglish", "britenglish"]
        error_list = ["", " ", "Page Not Found", "404 NOT FOUND", "죄송합니다", "페이지에 문제가 생겼어요",
                      "This page could not be found.", "상태 404", "찾을 수 없음"]
        package_text = "패키지수강 패키지 수강 신청하기"

        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
            time.sleep(1)
        elif browser == "ie":
            driver = webdriver.Ie()             # 32bit driver로 실행시켜야 다음단계 진행이 가능했음.
            time.sleep(10)
        else:
            print("알수 없는 브라우져")
            return

        driver.get(url_info)
        driver.implicitly_wait(10)

        try:
            if package == package_list[0]:
                element_value = driver.find_element_by_link_text("수강 신청").text   #수강 신청
            elif package == package_list[1]:
                element_value = driver.find_element_by_class_name("hasSubmenu").text    #패키지 수강
            elif package == package_list[2]:
                element_value = driver.find_element_by_class_name("fOwNTV").text   #수강 신청하기
            elif package == package_list[3]:
                element_value = driver.find_element_by_class_name("btn_link").text     #패키지 수강 신청하기

            if element_value in package_text:
                message = "[{}][{}]".format(time_now(), "PC " + browser) + url_info + " == 페이지 로드 정상."
                print(message)
                send_slack_message(message)
                # return 200, "Load Success"      # 성공 시 로그인 스크립트 수행 필요. driver object를 func에 전달?
                return login_check(package, url_info, browser, driver)

        except Exception as e1:
            print(str(e1))
            if package == package_list[0]:
                script_text = driver.find_element_by_id("root").text
            elif package == package_list[1]:
                script_text = driver.find_element_by_class_name("error_page").text
            elif package == package_list[2]:
                script_text = driver.find_element_by_xpath("//body").text
            elif package == package_list[3]:
                script_text = driver.find_element_by_xpath("//body").text

            if error_list[0] == script_text or error_list[1] == script_text:
                message = "[{}][{}]".format(time_now(),"PC " + browser) + url_info + " == 페이지 스크립트를 불러올 수 없습니다. cc.<@UNWSR3FFF>"
                print(message)
                send_slack_message(message)
                return 405, "Page Script is None"

            elif error_list[2] in script_text or error_list[3] in script_text:
                message = "[{}][{}]".format(time_now(),"PC " + browser) + url_info + " == 페이지를 찾을 수 없습니다. <@UNWSR3FFF>"
                print(message)
                send_slack_message(message)
                return 404, "Page Not Found"

    except Exception as e2:
        print(str(e2))
        message = "[{}][{}]".format(time_now(), "PC " + browser) + url_info + " " + str(e2) + "<@UNWSR3FFF>"
        send_slack_message(message)
    finally:
        driver.quit()

def url_test_code(package, url_info, browser):
    url_status = requests.get(url_info, timeout=3).status_code
    if url_status >= 200 and url_status < 300:
        print("[{}][{}]".format(time_now(), "PC " + browser) + " == response 200. But we need to double check")
        auto_check_browser(package, url_info, browser)        #성공 시, 실제 url 체크하는 함수 실행

    if url_status >= 400 and url_status < 500:
        print("[" + time_now() + "]" + " Fail to Page Load")
        message = "[{}][{}]".format(time_now(), "PC " + browser) + url_info + " == 페이지를 찾을 수 없습니다. <@UNWSR3FFF>"
        send_slack_message(message)

    if url_status >= 500:
        print("[" + time_now() + "]" + " Server Error")
        message = "[{}][{}]".format(time_now(), "PC " + browser) + url_info + " == 서버 에러 <@UNWSR3FFF>"
        send_slack_message(message)

#========================================
#↓↓↓↓↓↓↓↓↓↓↓↓ API 체크 루틴 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
def get_song_info():
    global  result
    result = []
    with open("song_info.csv", "r", encoding='utf-8') as f:
        data = csv.reader(f)
        for n in data:
            result.append(n)
    random_song = random.choice(result)
    return random_song

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
            song_info = get_song_info()
            play_check = requests.get(url_info.format(upc=int(song_info[0])), headers=tuple_data[1])
            print("content status:", play_check.status_code)
            message = "[{}] 닥터뮤지 {} - {} 곡 호출 성공".format(time_now(), song_info[2], song_info[1])
            send_slack_message(message)
        else:
            message = "[{}] 닥터뮤지 {} - {} 곡 호출 실패 <!here>".format(time_now(), song_info[2], song_info[1])
            send_slack_message(message)
            #send_kakao_message(message)
    except Exception as e2:
        message = "[" + time_now() + "]" + e2
        print(message)
        send_slack_message(message)
#========================================
#↓↓↓↓↓↓↓↓↓↓ 로그인 체크 루틴 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
def login_check(package, url_info, browser, *args):
    try:
        # if browser == "chrome":
        #     driver = webdriver.Chrome(options=options)
        #
        # driver.get(url_info)
        # driver.implicitly_wait(2)
        # time.sleep(3)

        driver = args[0]

        elem = driver.find_element_by_xpath(package_info[package]["login_text_xpath"])                   # 로그인 버튼 클릭
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_xpath(package_info[package]["email_xpath"])                        # 이메일 입력
        elem.send_keys(package_info[package]["test_id"])

        elem = driver.find_element_by_xpath(package_info[package]["password_xpath"])                     # 비밀번호 입력
        elem.send_keys(package_info[package]["test_pw"])

        elem = driver.find_element_by_xpath(package_info[package]["login_func_xpath"])                   # 로그인 버튼 클릭
        elem.click()
        time.sleep(3)

        if package == "drmuzy":
            elem = driver.find_element_by_xpath(package_info[package]["logout_xpath"])                       # 로그인 성공 유무 판단
            if elem.text == "로그아웃":
                print("로그인 성공")
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_xpath(package_info[package]["logout_xpath"])
                if elem.text == "회원가입":
                    print("로그아웃 성공")
                    message = "[{}] {} 로그인 스크립트 성공".format(time_now(),package)
                    send_slack_message(message)
            else:
                elem = driver.find_element_by_xpath(package_info[package]["my_device_xpath"])                # 기기변경 창 호출
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_xpath(package_info[package]["change_device_button"])
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_xpath(package_info[package]["logout_xpath"])
                if elem.text == "로그아웃":
                    print("로그인 성공")
                    elem.click()
                    time.sleep(3)
                    elem = driver.find_element_by_xpath(package_info[package]["logout_xpath"])
                    if elem.text == "회원가입":
                        print("로그아웃 완료")
                        # message = "[" + time_now() + "]" + " 오케이닥터 로그인/로그아웃 스크립트 성공"
                        message = "[{}] {} 로그인 스크립트 성공".format(time_now(),package)
                        send_slack_message(message)
                else:
                    raise Exception
        elif package == "homeglish":
            elem = driver.find_element_by_xpath(package_info[package]["my_dropdown"])
            if elem.text == package_info[package]["test_id"][:-12]:
                print("로그인 성공")
                message = "[{}] {} 로그인 스크립트 성공".format(time_now(), package)
                send_slack_message(message)
            else:
                raise Exception
        else:
            elem = driver.find_element_by_xpath(package_info[package]["my_dropdown"])
            if elem.text == "MY" or elem.text == "My":
                print("로그인 성공")
                message = "[{}] {} 로그인 스크립트 성공".format(time_now(), package)
                send_slack_message(message)
            else:
                raise Exception
    except (Exception, UnboundLocalError) as e:
        print(e)
        message = "[{}] {} Script Error :: 스크립트를 확인해주세요. cc.<@UNWSR3FFF> \n {}".format(time_now(), package, str(e))
        send_slack_message(message)
    finally:
        print("로그인 체크 함수 탈출")
        driver.quit()

#========================================
#↓↓↓↓↓↓↓↓↓↓↓↓↓ 스케쥴링 등록 ↓↓↓↓↓↓↓↓↓↓↓↓↓
#========================================
def schedule_start():
    try:
        global sched, sched2, sched3, COUNTER
        if COUNTER == 0:
            # 스케쥴러 추가 옵션
            executors = {
                'default': ThreadPoolExecutor(20),
                'processpool': ProcessPoolExecutor(5)
            }
            job_defaults = {
                'coalesce': False,
                'max_instances': 5
            }
            #
            sched = BackgroundScheduler(daemon=True, executors=executors, job_defaults=job_defaults)
            sched2 = BackgroundScheduler(daemon=True, executors=executors, job_defaults=job_defaults)
            sched3 = BackgroundScheduler(daemon=True, executors=executors, job_defaults=job_defaults)
            #
            # SERVICE CODE
            minute='15'
            minute2='45'
            minute3='*/10'
            #
            sched.add_job(func=url_test_code, args=("drmuzy", url_list[0], "chrome",), trigger='cron', minute=minute)           # URL 체크 루틴 1
            # sched.add_job(func=url_test_code, args=("drmuzy", url_list[1], "chrome",), trigger='cron', minute=minute)           # URL 체크 루틴 2
            sched.add_job(func=url_test_code, args=("realclass", url_list[2], "chrome",), trigger='cron', minute=minute)        # URL 체크 루틴 3
            sched.add_job(func=url_test_code, args=("britenglish", url_list[3], "chrome",), trigger='cron', minute=minute)      # URL 체크 루틴 4
            sched.add_job(func=url_test_code, args=("homeglish", url_list[4], "chrome",), trigger='cron', minute=minute)        # URL 체크 루틴 5
            #
            # sched2.add_job(func=url_test_code, args=("drmuzy", url_list[0], "ie",), trigger='cron', minute=minute2, second='00')               # URL 체크 루틴 6
            # sched2.add_job(func=url_test_code, args=("realclass", url_list[2], "ie",), trigger='cron', minute=minute2, second='15')            # URL 체크 루틴 7
            # sched2.add_job(func=url_test_code, args=("britenglish", url_list[3], "ie",), trigger='cron', minute=minute2, second='30')          # URL 체크 루틴 8
            # sched2.add_job(func=url_test_code, args=("homeglish", url_list[4], "ie",), trigger='cron', minute=minute2, second='45')            # URL 체크 루틴 9
            #
            sched3.add_job(func=vedio_play_check, args=(URL_SET,), trigger='cron', minute=minute3)                                # 뮤지 API 체크 루틴
            # sched3.add_job(func=login_check, args=("drmuzy", url_list[0], "chrome",), trigger='cron', minute=minute3)             # 뮤지 로그인 체크 루틴 == url체크와의 통합으로 제거
            print("스케쥴러 등록 완료")
            #
            sched.start()
            # sched2.start()
            sched3.start()
            print("스케쥴러 시작 완료")
            #
            # 스케쥴러 등록 처리
            COUNTER = 1
            return 200
        else:
            raise Exception
    except Exception as e:
        print(e)
        return 500

def schedule_shutdown():
    global COUNTER
    if COUNTER == 1:
        sched.shutdown(wait=False)
        COUNTER = 0
        print("shutdown done")
        return 200
    else:
        return 404

if __name__ == "__main__":
    pass