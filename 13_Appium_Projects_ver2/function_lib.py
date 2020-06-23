# -*- coding: utf-8 -*-
from qualson_config import *
###################################################################################
if test_mode == True:
	print ("!!!!!!!!!!!!! Debugging Mode !!!!!!!!!!!!!")
else:
	print ("!!!!!!!!!!!!!!! Service Mode !!!!!!!!!!!!!!!")
###################################################################################
# 오류 정의
###################################################################################
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

###################################################################################
# 카운터 함수
###################################################################################
CYCLE_COUNT = 0     # 카운터 변수

def cycle_count_increase():
    global CYCLE_COUNT
    CYCLE_COUNT += 1

def cycle_count_decrease():
    global CYCLE_COUNT
    CYCLE_COUNT -= 1

def cycle_count_reset():
    global CYCLE_COUNT
    CYCLE_COUNT = 0

###################################################################################
# 공통 처리 메시지
###################################################################################
REAL_TIME = ""

def datetime_now():
    global REAL_TIME
    REAL_TIME = str(datetime.now())[:]   # -7 => m/s 단위 파싱

def datetime_date():
    return str(datetime.now())[:10]     # yyyy-mm-dd 형식

def get_message():
    # common_message = "[" + REAL_TIME + "]" + app_package_kr + "[{} App]#".format(platform) + str(CYCLE_COUNT) + " "
    common_message = "[{0}][{1}][{2}][{3}]#{4} ".format(REAL_TIME, run_info['OS'], run_info['platform'], run_info['product'], str(CYCLE_COUNT))
    return str(common_message)

def get_message_2():
    # common_message = "[" + REAL_TIME + "]" + app_package_kr + "[{} App] ".format(platform)
    common_message = "[{0}][{1}][{2}][{3}] ".format(REAL_TIME, run_info['OS'], run_info['platform'], run_info['product'])
    return str(common_message)

def get_err_message():
    return

###################################################################################
# 로그 처리 함수
###################################################################################
def write_logging(message):
    if not(os.path.isdir("log")):
        os.makedirs(os.path.join("log"))    # log 디렉토리 생성
    with open("./log/log_{}.txt".format(datetime_date()), "a") as file:     # log_2020-04-10.txt 형식으로 파일 기록
        file.write(message + "\n")    # 로그 기록

###################################################################################
# 슬랙 기능
###################################################################################
# 메시지 전송
def send_slack_massage(message):
    try:
        # edit_message = get_message() + message
        slack.chat.post_message(slack_channel, message)
        return 200
    except Exception as e:
        return 404, str(e)

# 파일 전송
def send_slack_file(filename):
    try:
        slack.files.upload(filename, channels=slack_channel)
        return 200
    except Exception as e:
        return 404, str(e)
###################################################################################
# 통합 메시징 처리 == 프롬프트 & 로그.txt & 슬랙 메시지
###################################################################################
def total_report(text, keyword):
    if keyword == "info":
        datetime_now()                                        #0. 시간 갱신
        final_text = get_message() + text                     #1. 전달 메시지 가공 == 수행 넘버 O
        write_logging(final_text)                             #2. 로그 기록
        if test_mode == True:
            print(final_text)                                 #3. 프롬프트 출력
        send_slack_massage(final_text)                        #4. 슬랙 메시지 전송

    if keyword == "notice":
        datetime_now()                                        #0. 시간 갱신
        final_text = get_message_2() + text                   #1. 전달 메시지 가공 == 수행 넘버 X
        write_logging(final_text)                             #2. 로그 기록
        if test_mode == True:
            print(final_text)                                 #3. 프롬프트 출력
        send_slack_massage(final_text)                        #4. 슬랙 메시지 전송

    if keyword == "warning":
        datetime_now()                                        #0. 시간 갱신
        mention = "<@UNWSR3FFF>"                              # 윤식: <@UL8T21UAK> // 진석: <@UNWSR3FFF>
        final_text = get_message() + text + " " + mention   #1. 전달 메시지 가공
        write_logging(final_text)                             #2. 로그 기록
        if test_mode == True:
            print(final_text)                                 #3. 프롬프트 출력
        send_slack_massage(final_text)                        #4. 슬랙 메시지 전송

    if keyword == "error_test":
        datetime_now()                                        #0. 시간 갱신
        mention = "<@UNWSR3FFF>"
        final_text = get_message_2() + text + " " + mention   #1. 전달 메시지 가공
        write_logging(final_text)                             #2. 로그 기록
        if test_mode == True:
            print(final_text)                                 #3. 프롬프트 출력
        send_slack_massage(final_text)                        #4. 슬랙 메시지 전송

    if keyword == "error":
        datetime_now()                                        #0. 시간 갱신
        mention = "<@UNWSR3FFF>"    # <!channel>
        final_text = get_message_2() + text + " " + mention   #1. 전달 메시지 가공
        write_logging(final_text)                             #2. 로그 기록
        if test_mode == True:
            print(final_text)                                 #3. 프롬프트 출력
        send_slack_massage(final_text)                        #4. 슬랙 메시지 전송

    if keyword == "None":
        final_text = text                                     #1. 전달 메시지 가공
        write_logging(final_text)                             #2. 로그 기록
        if test_mode == True:
            print(final_text)                                 #3. 프롬프트 출력
        send_slack_massage(final_text)                        #4. 슬랙 메시지 전송

    if keyword == "log":
        datetime_now()                                        #0. 시간 갱신
        final_text = get_message() + text                     #1. 전달 메시지 가공 == 수행 넘버 O
        write_logging(final_text)                             #2. 로그 기록

###################################################################################
# 랜덤 계정 생성 함수
###################################################################################
def random_text():
    global random_mail
    global random_pass
    global random_nick
    rtext=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r1=str(random.choice(rtext))
    r2=str(random.choice(rtext))
    r3=str(random.randrange(0,9))
    r4=str(random.choice(rtext))
    r5=str(random.randrange(0,9))
    r6=str(random.choice(rtext))
    r7=str(random.randrange(0,9))
    r8=str(random.choice(rtext))
    r9=str(random.randrange(0,9))
    r10=str(random.choice(rtext))
    r11=str(random.choice(rtext))
    random_mail = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+"_test"+"@qualson.com"
    random_pass = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+"_test"
    random_nick = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+"_test"
    if test_mode == True:
        print("random_mail: " + random_mail)
        print("random_pass: " + random_pass)
        print("random_nick: " + random_nick)

###################################################################################
# Window Process Checikng
###################################################################################
def get_process_id():   # appium_end() function 수행 시, 체크
    for process in psutil.process_iter():
        process_list = ["cmd.exe", "conhost.exe", "node.exe"]
        if process.name() in process_list:
            print(process)
            # process.as_dict(attrs=['pid', 'name', 'cpu_percent'])

# get_process_id()

###################################################################################
# Appium 구동 함수
###################################################################################
def appium_server():
    try:
        cycle_count_reset()
        total_report("{} 검수 시작".format(run_info["TC"]), "notice")
        if test_mode == True:
            total_report("Appium 서버 시작", "info")
        else:
            total_report("Appium 서버 시작", "log")
        # 포트 설정 필요 ex) start appium --address 0.0.0.0 --port 4723
        subprocess.Popen("start appium --address {} --port {}".format(local_url, PORT), shell=True)
        return 200
    except Exception:
        total_report("Appium 서버 시작 오류","warning")
        return 404

def appium_connect():
    try:
        global driver
        cycle_count_increase()
        driver = AP.Remote(appium_address, desired_caps)        # 라인업 별로 지정된 주소:포트에 연결
        if test_mode == True:
            total_report("Appium 서버와 모바일 기기 연결 성공","info")
            # print(str(driver))
        else:
            total_report("Appium 서버와 모바일 기기 연결 성공", "log")
        return 200
    except Exception:
        total_report("Appium 연결 오류","warning")
        return 404

def appium_end():
    try:
        cycle_count_increase()
        # taskkill /im afidev.exe -> 3312, 3313, 3314 afidev.exe 관련 모든 PID 프로세스 종료
        # taskkill /pid 3778 /f == 강제종료 /f
        #
        subprocess.Popen("taskkill /im cmd.exe /f")
        subprocess.Popen("taskkill /im node.exe /f")
        # subprocess.Popen("taskkill /im conhost.exe /f")
        if test_mode == True:
            total_report("Appium 서버 종료", "notice")
        else:
            total_report("Appium 서버 종료", "log")
        return 200
    except Exception:
        total_report("Appium 서버 종료 오류", "warning")
        return 404

def appium_driver_quit():
    try:
        cycle_count_increase()
        # global driver
        driver.quit()
        if test_mode == True:
            total_report("Appium 드라이버 종료", "info")
        else:
            total_report("Appium 드라이버 종료", "log")
        return 200
    except Exception:
        total_report("Appium 드라이버 종료 오류", "warning")
        return 404

###################################################################################
# Appium 요소 식별 함수
###################################################################################
# 버튼 터치(id)
def appium_chk_id_click(id, *args):
    try:
        cycle_count_increase()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id))).click()
        if test_mode == True:
            total_report("동작 수행 완료: {}".format(args[0]),"info")
        else:
            total_report("동작 수행 완료: {}".format(args[0]), "log")
        time.sleep(1)
        return 200
    except Exception:
        total_report("동작 수행 오류: {}".format(args[0]), "warning")
        return 404

# 버튼 터치(xpath)
def appium_chk_xpath_click(xpath, *args):
    try:
        cycle_count_increase()
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        if test_mode == True:
            total_report("동작 수행 완료: {}".format(args[0]),"info")
        else:
            total_report("동작 수행 완료: {}".format(args[0]), "log")
        time.sleep(1)
        return 200
    except Exception:
        total_report("동작 수행 오류: {}".format(args[0]), "warning")
        return 404

# 키워드에 따른 스트링 입력(xpath)
def appium_chk_xpath_send_keys(xpath, keyword, *args):
    try:
        cycle_count_increase()
        if keyword == "email":
            string = random_mail
        elif keyword == "password":
            string = random_pass
        elif keyword == "nickname":
            string = random_nick
        elif keyword == "phonenumber":
            string = phone_number
        elif keyword == "ocr_result":
            string = processing_ocr_number
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(string)
        if test_mode == True:
            total_report("동작 수행 완료: {}".format(args[0]),"info")
        else:
            total_report("동작 수행 완료: {}".format(args[0]), "log")
        time.sleep(1)
        return 200
    except Exception:
        total_report("동작 수행 오류: {}".format(args[0]), "warning")
        return 404

# 키워드에 따른 스트링 입력(id)
def appium_chk_id_send_keys(id, keyword, *args):
    try:
        cycle_count_increase()
        if keyword == "email":
            string = random_mail
        elif keyword == "password":
            string = random_pass
        elif keyword == "nickname":
            string = random_nick
        elif keyword == "phonenumber":
            string = phone_number
        elif keyword == "ocr_result":
            string = processing_ocr_number
        elif keyword == "delivery_name":
            string = "test"
        elif keyword == "delivery_addr":
            string = "엔씨타워"
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id))).send_keys(string)
        if test_mode == True:
            total_report("동작 수행 완료: {}".format(args[0]),"info")
        else:
            total_report("동작 수행 완료: {}".format(args[0]), "log")
        time.sleep(1)
        return 200
    except Exception:
        total_report("동작 수행 오류: {}".format(args[0]), "warning")
        return 404

# 문자메시지 발송 시간 추출(xpath)
def appium_chk_xpath_sms_time(xpath):
    try:
        cycle_count_increase()
        time.sleep(2)
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        time_export = element.text
        if test_mode == True:
            total_report("동작 수행완료: 문자 메시지 발송 시간 추출: " + time_export, "info")
        else:
            total_report("동작 수행완료: 문자 메시지 발송 시간 추출: " + time_export, "log")
        return 200, time_export
    except Exception as e:
        total_report("문자 발송 시간 추출 실패", "warning")
        return 404

###################################################################################
# Appium 기타 동작 함수
###################################################################################
def start_android_sms():
    try:
        cycle_count_increase()
        driver.start_activity("com.samsung.android.messaging", "com.samsung.android.messaging.ui.view.main.WithActivity")
        if test_mode == True:
            total_report("동작 수행완료: 메시지 앱 이동 성공","info")
        else:
            total_report("동작 수행완료: 메시지 앱 이동 성공", "log")
        time.sleep(5)
        return 200
    except Exception:
        total_report("메시지 앱 이동 실패", "warning")
        return 404

def return_qualson_app(package):
    try:
        cycle_count_increase()
        driver.activate_app(package)
        if test_mode == True:
            total_report("{} App 복귀 성공".format(app_package_kr),"info")
        else:
            total_report("{} App 복귀 성공".format(app_package_kr), "log")
        time.sleep(5)
        return 200
    except Exception:
        total_report("{} App 복귀 실패".format(app_package_kr), "warning")
        return 404

def time_check(time):       # time == sms 문자앱으로부터 추출된 시간 값
    try:
        cycle_count_increase()
        except_case = ["-", ".", "월"]
        if except_case[0] in time or except_case[1] in time or except_case[2] in time:
            raise Exception("날짜 형식 오류")
        now = datetime.now()
        now_hh = str(now)[11:13]    # 실제 현재 시간의 "시" 숫자 추출
        sms_hh = time[:2]               # sms 앱에서 "시" 숫자 추출 == 24시각 기준 HH:MM
        # print(sms_hh)
        if now_hh != sms_hh:
            raise Exception("발송 HH 시간이 다름")
        # 발송 시간이 같을 경우, 아래 루틴 진행
        sms_mm = time[-2:]              # sms 앱에서 "분" 숫자 추출
        sms_mm = int(sms_mm)
        now_mm = now.minute         # 실제 현재 시간의 "분" 숫자 추출
        # except_sms_mm = [58, 59]
        except_now_mm = [0,1]
        if sms_mm == 58 and now_mm in except_now_mm:
            now_mm += 60
        if sms_mm == 59 and now_mm in except_now_mm:
            now_mm += 60
        min_value = now_mm-sms_mm
        # print(now_mm, sms_mm)
        # print(min_value)
        if min_value >= 0 and min_value < 2:   # 2분 이내
            if test_mode == True:
                total_report("동작 수행완료: (오차: {}분)".format(min_value), "info")
            else:
                total_report("동작 수행완료: 문자 수신 성공(오차: {}분)".format(min_value), "log")
            return 200
        else:
            if test_mode == True:
                total_report("문자 수신 실패(오차: {}분)".format(min_value), "info")
            else:
                total_report("문자 수신 실패(오차: {}분)".format(min_value), "log")
            return 404
    except Exception as e:
        if test_mode == True:
            total_report(str(e), "info")
        else:
            total_report(str(e), "log")
        return 404

# 화면 스크린샷(aos)
def aos_appium_save_screenshot(path, name, format):
    try:
        driver.save_screenshot(path + "/" + name + "." + format)
        return 200
    except:
        return 404

# 스크린샷 크롭
def img_cropping(y1, y2, x1, x2, path, name , format):
    fullpath = path + "/" + name + "." + format
    img = cv2.imread(fullpath, cv2.IMREAD_GRAYSCALE)
    cropping = img[y1:y2, x1:x2]  # [y시작점:y끝점, x시작점:x끝점]
    cv2.imwrite(fullpath, cropping)

def detect_number(path):
    try:
        client = vision.ImageAnnotatorClient()
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        #
        a = []
        index = 0
        strLen = 0
        maxLen = 0
        count = 0
        #
        for text in texts:
            try:
                sat = ('"{}"'.format(text.description))
            except:
                sat = ('"{}"'.format(text.description.encode('utf-8')))
            strLen = len(sat)
            if strLen > maxLen:
                index = count
                maxLen = strLen
            a.append(sat)
            count += 1
        retString = a[index]
        ocr_result = retString
        ocr_result = re.findall("\d+", ocr_result)
        ocr_result = str(ocr_result)
        ocr_result = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', ocr_result)
        ocr_result = re.sub(' ', '', ocr_result)
        if test_mode == True:
            total_report("동작 수행완료: 인증번호 추출 완료", "info")
        else:
            total_report("동작 수행완료: 인증번호 추출 완료", "log")
        return ocr_result
    except Exception as e:
        total_report(str(e), "warning")

def appium_image_detect_number(x1, y1, x2, y2, path, name, format):
    try:
        cycle_count_increase()
        aos_appium_save_screenshot(path, name, format)          # device 스샷 찍기
        img_cropping(y1, y2, x1, x2, path, name, format)        # 스샷 크롭 처리
        fullpath = path + '/' + name + '.' + format
        global processing_ocr_number
        processing_ocr_number = detect_number(fullpath)
        if test_mode == True:
            total_report("동작 수행완료: 인증번호 파싱 완료: " + processing_ocr_number, "info")
        else:
            total_report("동작 수행완료: 인증번호 파싱 완료: " + processing_ocr_number, "log")
        return 200
    except Exception as e:
        total_report(str(e), "warning")
        return 404

def appium_terminate_app(package):
    try:
        cycle_count_increase()
        driver.terminate_app(package)
        if test_mode == True:
            total_report("앱 정상 종료", "info")
        else:
            total_report("앱 정상 종료", "log")
        return 200
    except Exception as e:
        total_report(str(e), "warning")
        return 404

def appium_scroll(x1,y1,x2,y2,dur=300, cnt=2):  # int startx, int starty, int endx, int endy, int duration
    cycle_count_increase()
    for i in range(2):
        try:
            time.sleep(5)
            for k in range(cnt):
                driver.swipe(x1, y1, x2, y2, dur)
                time.sleep(1)
                if test_mode == True:
                    total_report("동작 수행완료: 스크롤 처리 완료", "info")
                else:
                    total_report("동작 수행완료: 스크롤 처리 완료", "log")
            return 200
        except Exception as e :
            total_report(str(e), "warning")
            return 404

###################################################################################
# 루프 함수
###################################################################################
def function_loop(main_function, count, *args):
    try:
        for i in range(0, count):
            if len(args) == 0:
                func_result = main_function()
                if func_result == 200:
                    if test_mode == True:
                        print("동작 성공")
                    break
                else:
                    if test_mode == True:
                        print("동작 실패")
                    cycle_count_decrease()  # 다음 함수 실행 카운트 -1
                    total_report(" ={}번째 실행 실패".format(i+1), "warning")
                    continue
            elif len(args) == 1:
                func_result = main_function(args[0])
                if func_result == 200:
                    if test_mode == True:
                        print("동작 성공")
                    break
                else:
                    if test_mode == True:
                        print("동작 실패")
                    cycle_count_decrease()  # 다음 함수 실행 카운트 -1
                    total_report(" ={}번째 실행 실패".format(i+1), "warning")
                    continue
            elif len(args) == 2:
                func_result = main_function(args[0], args[1])
                if func_result == 200:
                    if test_mode == True:
                        print("동작 성공")
                    break
                else:
                    if test_mode == True:
                        print("동작 실패")
                    cycle_count_decrease()  # 다음 함수 실행 카운트 -1
                    total_report(" ={}번째 실행 실패".format(i+1), "warning")
                    continue
        return 200
    except Exception:
        total_report("function loop 실패", "warning")
        return 404
###################################################################################
if __name__ == "__main__":
    pass