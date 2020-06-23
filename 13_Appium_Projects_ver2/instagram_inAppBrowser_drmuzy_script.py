# -*- coding: utf-8 -*-
# 실행 환경 확인
with open("setting.txt", "r") as file:
    set = file.read()

# 실행 정보 기록
with open("run_info.csv", "w") as f:
    f.write("OS,Android\n")
    f.write("platform,inAppBrowser-drmuzy\n")
    f.write("product,instagram\n")
    f.write("TC,로그인")

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
from appium_script_path import *
#
###################################################################################
# 카운터 변수
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
# (회원가입) > 로그인 > 로그아웃 스크립트
###################################################################################
def run_test_script():
    global RUN_COUNT, SUCCESS_COUNT, LOOP_SWITCH, LOOP_COUNT, LOGIN_CHECK, APPIUM_RUN, APPIUM_CONNECT, REBOOT_COUNT
    subprocess.Popen("taskkill /im node.exe /f")
    subprocess.Popen("adb shell pm clear com.instagram.android", shell=True)
    while RUN_COUNT < 4 and SUCCESS_COUNT < 1:
        try:
            if RUN_COUNT == 0 and APPIUM_RUN == False:
                ### 서버 구동 ###
                # 0. Appium 서버 시작
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
            #2. 로그인 버튼 터치
            if appium_chk_xpath_click(Insta_login_button_xpath, "로그인 버튼 터치") != 200:
                raise Exception
            time.sleep(2)

            #3. 내 계정으로 이동
            if appium_chk_id_click(Insta_My_tab_id, "내 계정으로 이동") != 200:
                raise Exception
            time.sleep(2)

            #4. 팔로우 목록으로 이동
            if appium_chk_id_click(Insta_My_follow_list_button_id, "팔로우 목록으로 이동") != 200:
                raise Exception
            time.sleep(2)

            #5. 라인업 터치
            if 'drmuzy' in run_info['platform']:
                xpath = Insta_My_follow_list_drmuzy_xpath
            if 'realclass' in run_info['platform']:
                xpath = Insta_My_follow_list_realclass_xpath
            if 'britenglish' in run_info['platform']:
                xpath = Insta_My_follow_list_britenglish_xpath
            if 'homeglish' in run_info['platform']:
                xpath = Insta_My_follow_list_homeglish_xpath
            if appium_chk_xpath_click(xpath, "{} 계정으로 이동".format(run_info['platform'][13:])) != 200:
                raise Exception
            time.sleep(2)

            #6. 선택한 라인업의 웹사이트로 이동
            if appium_chk_id_click(Insta_website_link_id, "{} 홈페이지로 이동".format(run_info['platform'][13:])) != 200:
                raise Exception
            time.sleep(5)

            ##########################################################
            # 닥터뮤지 시나리오 진행
            # 현재 시작 구간을 처리 모하고 있음
            ##########################################################
            #7. 패키지 선택하기
            if appium_chk_xpath_click(package_info['inApp']['packageBar_xpath'], "패키지 선택하기 버튼 터치") != 200:
                raise Exception
            time.sleep(2)

            #8. 수강 신청하기
            if appium_chk_xpath_click(package_info['inApp']['classJoin_xpath'], "수강 신청하기 버튼 터치") != 200:
                raise Exception
            time.sleep(2)

            ##########################################################
            # 회원가입 시나리오?!
            # == 캐쉬 날리고 인스타 앱에 진입했을 때, 로그인 세션이 날라갔는지 확인 필요
            ##########################################################

            #9. 이름 입력
            if appium_chk_id_send_keys(package_info['inApp']['buy_nameField_id'], "delivery_name", "배송정보 이름 입력"):
                raise Exception
            time.sleep(2)

            #10. 주소검색 버튼 터치
            if appium_chk_xpath_click(package_info['inApp']['buy_searchAddr_xpath'], "주소검색 버튼 터치") != 200:
                raise Exception
            time.sleep(2)

            #11. 주소 키워드 입력
            if appium_chk_id_send_keys(package_info['inApp']['buy_addrInputField_id'], "delivery_addr", "주소 입력"):
                raise Exception
            time.sleep(2)

            #12. 검색 버튼 터치
            if appium_chk_xpath_click(package_info['inApp']['buy_addrSearchBT_xpath'], "주소검색 수행") != 200:
                raise Exception
            time.sleep(2)

            #13. 주소 선택
            if appium_chk_xpath_click(package_info['inApp']['buy_addrList_xpath'], "주소선택") != 200:
                raise Exception
            time.sleep(2)

            #14. 결제확인팝업 표시
            if appium_chk_xpath_click(package_info['inApp']['buy_paymentPopup_xpath'], "결제확인 팝업 표시") != 200:
                raise Exception
            time.sleep(2)

            #15. 구매동의 체크
            if appium_chk_id_click(package_info['inApp']['buy_agreeBox_id'], "구매동의 체크") != 200:
                raise Exception
            time.sleep(2)

            #16. 결제 창 호출
            if appium_chk_xpath_click(package_info['inApp']['buy_doPaymentBT_xpath'], "결제창 호출") != 200:
                raise Exception
            time.sleep(2)

            #17. 결제 창 호출 확인
            if appium_chk_xpath_click(package_info['inApp']['LGCNS_agreeAllbox_xpath'], "약관 전체 동의") != 200:
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
                    subprocess.Popen("adb shell pm clear com.qualson.drmuzy", shell=True)
                    LOGIN_CHECK = False
                total_report("-----------------------------------", "None")  # 구분선 표시


if __name__ == "__main__":
    run_test_script()
    # print(run_info['platform'][13:])