# -*- coding: utf-8 -*-
# 실행 스크립트 app name 기록
with open("app.txt", "w") as file:
    file.write("britenglish")
# 실행 환경 확인
with open("setting.txt", "r") as file:
    set = file.read()

# 실행 정보 기록
with open("run_info.csv", "w") as f:
    f.write("OS,Android\n")
    f.write("platform,App\n")
    f.write("product,britenglish\n")
    f.write("TC,회원가입")
#
import sys
import time
import subprocess
#
if set == 'test':
    sys.path.append('C:\\Users\\jinse\\PycharmProjects\\qualson_project\\13_Appium_Projects_ver2')
    sys.path.append('C:\\Users\\jinse\\PycharmProjects\\qualson_project\\13_Appium_Projects_ver2\\__pycache__')
elif set == 'real':
    sys.path.append('C:\\Projects_ver2\\bin')
#
from function_lib import *
#
###################################################################################
# 카운터
###################################################################################
RUN_COUNT = 0           # 실행 횟수
SUCCESS_COUNT = 0       # 성공 여부
#
LOOP_SWITCH = False      # 루프 실행 = True // 한번만 실행 = False
LOOP_COUNT = 3          # 루프 카운터 == 지정한 횟수만큼 실행
#
LOGIN_CHECK = False     # 로그인 수행 여부
APPIUM_RUN = False      # 앱피움 실행 여부
APPIUM_CONNECT = False  # 앱피움 연결 여부
REBOOT_COUNT = 0        # 리부트 수행 여부
###################################################################################
# 회원가입 > 로그아웃 스크립트
###################################################################################
def run_test_script():
    global RUN_COUNT, SUCCESS_COUNT, LOOP_SWITCH, LOOP_COUNT, LOGIN_CHECK, APPIUM_RUN, APPIUM_CONNECT, REBOOT_COUNT
    subprocess.Popen("taskkill /im node.exe /f")
    subprocess.Popen("adb shell pm clear com.qualson.britenglish", shell=True)
    while RUN_COUNT < 4 and SUCCESS_COUNT < 1:
        try:
            if RUN_COUNT == 0 and APPIUM_RUN == False:
                ### 서버 구동 ###
                #0. Appium 서버 시작
                if appium_server() != 200:
                    total_report("Appium 구동 실패", "info")
                    break
                else:
                    APPIUM_RUN = True
            else:
                cycle_count_reset()
            #
            if RUN_COUNT == 1:
                total_report("1차 검수 실패. 재 확인 진행 ", "notice")
            if RUN_COUNT == 2:
                total_report("2차 검수 실패. 재 확인 진행 ", "notice")
            #######################################################################
            #1. Appium 서버와 모바일 기기 연결 시도
            if appium_connect() != 200:
                # total_report("기기 연결 실패", "warning")
                raise MyError("기기 연결 실패: 재부팅 진행")
            else:
                APPIUM_CONNECT = True
            time.sleep(2)
            ################
            ### 스크립트 ###
            #2. 회원가입 페이지 이동
            id = 'com.qualson.britenglish:id/btn_on_boarding_register'
            if appium_chk_id_click(id, "회원가입 페이지 이동") != 200:
                raise Exception
            time.sleep(2)

            ## 랜덤 계정 생성
            random_text()
            time.sleep(2)

            #3. 이메일 입력
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText'
            if appium_chk_xpath_send_keys(xpath, "email", "이메일 입력") != 200:
                raise Exception
            time.sleep(2)

            #4. 비밀번호 입력
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
            if appium_chk_xpath_send_keys(xpath, "password", "비밀번호 입력") != 200:
                raise Exception
            time.sleep(2)

            #5. 닉네임 입력
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
            if appium_chk_xpath_send_keys(xpath, "nickname", "닉네임 입력") != 200:
                raise Exception
            time.sleep(2)

            #6. 휴대전화 인증 페이지로 이동
            id = 'com.qualson.britenglish:id/tv_toolbar_right'
            if appium_chk_id_click(id, "휴대전화 인증 페이지로 이동") != 200:
                raise Exception
            time.sleep(2)

            #7 휴대전화번호 입력
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
            if appium_chk_xpath_send_keys(xpath, "phonenumber", "휴대전화번호 입력") != 200:
                raise Exception
            time.sleep(3)
            ############################################################
            # 오류 발생 제일 심한 구간
            ############################################################
            #8. 인증번호 받기 터치
            id = 'com.qualson.britenglish:id/phone_auth_get_phone_auth'
            if LOOP_SWITCH == True:
                print("start loop")
                if function_loop(appium_chk_id_click, LOOP_COUNT, id, "인증번호 받기 터치") != 200:
                    raise Exception
            else:
                if appium_chk_id_click(id, "인증번호 받기 터치") != 200:
                    raise Exception
            time.sleep(2)

            #9. 메시지 앱으로 이동
            if start_android_sms() != 200:
                raise Exception
            time.sleep(5)

            #10. 인증문자 발송 시간 추출
            if test_mode == True:
                xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView'
            elif test_mode == False:
                xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView'
            result_value = appium_chk_xpath_sms_time(xpath)
            if result_value[0] != 200:
                raise Exception
            time.sleep(2)

            #11. 시간 오차 체크(=인증문자 정상수신 여부)
            if time_check(result_value[1]) != 200:
                n = 0
                success = False
                while n<3:  # => 3회 반복
                    time.sleep(2)
                    cycle_count_decrease()
                    cycle_count_decrease()
                    cycle_count_decrease()
                    cycle_count_decrease()
                    cycle_count_decrease()
                    #7. 앱 복귀
                    if return_qualson_app(app_package) != 200:
                        raise Exception
                    time.sleep(2)

                    #8. 인증번호 받기 터치
                    id = 'com.qualson.britenglish:id/phone_auth_get_phone_auth'
                    if appium_chk_id_click(id, "인증번호 받기 터치") != 200:
                        raise Exception
                    time.sleep(2)

                    #9. 메시지 앱으로 이동
                    if start_android_sms() != 200:
                        raise Exception
                    time.sleep(2)

                    #10. 인증문자 발송 시간 추출
                    if test_mode == True:
                        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView'
                    elif test_mode == False:
                        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView'
                    result_value = appium_chk_xpath_sms_time(xpath)
                    if result_value[0] != 200:
                        raise Exception
                    time.sleep(2)

                    #11. 시간 오차 체크(=인증문자 정상수신 여부)
                    if time_check(result_value[1]) != 200:
                        n+=1
                    else:
                        success = True
                        break
                if success == False:
                    raise Exception

            #12. SMS 인증번호 추출
            if test_mode == True:
                path = 'C:\\Users\\jinse\\PycharmProjects\\qualson_project\\13_Appium_Projects_ver2'
            else:
                path = 'C:\\Projects_ver2\\bin'
            if appium_image_detect_number(240, 1359, 1228, 1554, path, 'cut', 'png') != 200:
                raise Exception
            time.sleep(2)

            #13. 앱으로 이동
            if return_qualson_app(app_package) != 200:
                raise Exception
            time.sleep(2)

            #14. 인증번호 입력        ==> 인증번호가 안맞는 경우, 예외 처리 필요 // 화면체크를 한번 더 할지 고려할 것.
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
            if appium_chk_xpath_send_keys(xpath, "ocr_result", "인증번호 입력") != 200:
                total_report("가입 버튼 터치 실패(=인증문자 확인 필요)", "warning")
                raise Exception
            time.sleep(2)

            #16. 가입 시도
            id = 'com.qualson.britenglish:id/tv_toolbar_right'
            if appium_chk_id_click(id, "가입 버튼 터치") != 200:
                total_report("가입 버튼 터치 실패(=인증문자 확인 필요)", "warning")
                raise Exception
            time.sleep(2)

            #17. 새로 가입하기 터치
            id = 'com.qualson.britenglish:id/btn_dialog_register'
            if appium_chk_id_click(id, "새로 가입하기 터치") != 200:
                raise Exception
            time.sleep(2)

            ############################################################
            # 아래 구간에서 오류 발생 시, 로그아웃 로직을 넣어야 함 => 앱 데이터 전부 날리기
            ############################################################
            #18. 로그인 완료 팝업 터치
            id = 'com.qualson.britenglish:id/btn_dialog'
            if appium_chk_id_click(id, "로그인 완료 터치") != 200:
                LOGIN_CHECK = True
                raise Exception
            time.sleep(2)

            #19. 마이메뉴 펼치기
            id = 'com.qualson.britenglish:id/iv_main_menu'
            if appium_chk_id_click(id, "마이메뉴 펼치기") != 200:
                LOGIN_CHECK = True
                raise Exception
            time.sleep(2)

            #20. 설정 메뉴 이동
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.TextView'
            if appium_chk_xpath_click(xpath, "설정 메뉴 이동") != 200:
                LOGIN_CHECK = True
                raise Exception

            #21. 로그아웃 터치
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.support.v7.widget.RecyclerView[3]/android.view.ViewGroup[3]'
            if appium_chk_xpath_click(xpath, "로그아웃 메뉴 터치") != 200:
                LOGIN_CHECK = True
                raise Exception

            #22. 로그아웃 확인 버튼 터치
            id = 'com.qualson.britenglish:id/btn_dialog_positive'
            if appium_chk_id_click(id, "로그아웃 확인 터치") != 200:
                LOGIN_CHECK = True
                raise Exception
            time.sleep(2)

            # 앱 종료
            if appium_terminate_app(app_package) != 200:
                raise Exception
            time.sleep(2)

            # 스크립트 성공 처리
            SUCCESS_COUNT = 1
        except MyError as e:
            REBOOT_COUNT += 1
            if REBOOT_COUNT < 3:
                subprocess.Popen("adb reboot", shell=True)
                total_report(str(e), "notice")
                time.sleep(60)
                continue
            else:
                total_report("Reboot 횟수 초과", "notice")
                break

        except Exception:
            time.sleep(2)
            if APPIUM_CONNECT == True:
                RUN_COUNT += 1
            # print("run:", RUN_COUNT)
            # total_report("Exception {}".format(str(RUN_COUNT)),"notice")
            if test_mode == True:
                path = 'C:\\Users\\jinse\\PycharmProjects\\qualson_project\\13_Appium_Projects_ver2\\__pycache__'
            else:
                path = 'C:\\Projects_ver2\\bin'
            aos_appium_save_screenshot(path, "error", "png")    # 스크린샷 찍기
            time.sleep(1)
            filename = "error.png"
            send_slack_file(filename)                           # 에러 시점 스크린샷 전송
            time.sleep(1)
            total_report("스크립트 체크 실패", "notice")
            time.sleep(3)
            # Appium 드라이버 종료
            appium_driver_quit()
            time.sleep(5)
        finally:
            if SUCCESS_COUNT == 1:
                appium_end()
                total_report("{} 검수 성공".format(run_info['TC']), "notice")
                total_report("===================================", "None")  # 구분선 표시
            elif RUN_COUNT == 3:
                appium_end()
                if test_mode == True:
                    report_level = "error_test"
                else:
                    report_level = "error"
                total_report("최종 검수 실패. 장애 여부 확인 필요 ", report_level)
                total_report("===================================", "None")  # 구분선 표시
                break
            else:
                if LOGIN_CHECK == True:
                    subprocess.Popen("adb shell pm clear com.qualson.britenglish", shell=True)
                    LOGIN_CHECK = False
                total_report("-----------------------------------", "None")  # 구분선 표시

if __name__ == "__main__":
    run_test_script()