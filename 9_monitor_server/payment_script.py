from import_server_module import *
from config_info import *

options = Options()     # 셀레늄 실행 옵션 설정
options.add_argument("--start-maximized")
slack = Slacker(token)  # 슬랙봇 생성

def time_now():
    return str(datetime.now())[:]   #-7

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

from selenium import webdriver
def payment_check(package, url_info, browser):
    try:
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
            time.sleep(1)
        elif browser == "ie":
            driver = webdriver.Ie()             # 32bit driver로 실행시켜야 다음단계 진행이 가능했음.
            time.sleep(3)
        else:
            print("알수 없는 브라우져")
            return

        driver.get(url_info)
        driver.implicitly_wait(2)
        time.sleep(3)

        elem = driver.find_element_by_xpath(login_text_xpath)                   # 로그인 버튼 클릭
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_xpath(email_xpath)                        # 이메일 입력
        elem.send_keys("test_020@qualson.com")

        elem = driver.find_element_by_xpath(password_xpath)                     # 비밀번호 입력
        elem.send_keys("12345678")

        elem = driver.find_element_by_xpath(login_func_xpath)                   # 로그인 버튼 클릭
        elem.click()
        time.sleep(3)

        elem = driver.find_element_by_xpath(logout_xpath)                       # 로그인 성공 유무 판단
        if elem.text == "로그아웃":                                                 # 로그인 성공
            print("로그인 성공")
            # elem.click()
            time.sleep(3)
            # elem = driver.find_element_by_xpath(logout_xpath)
            # if elem.text == "회원가입":                                             # 로그아웃 성공
            #     print("로그아웃 성공")
            #     message = "[" + time_now() + "]" + " 오케이닥터 로그인/로그아웃 스크립트 성공"
            #     send_slack_message(message)
        else:
            elem = driver.find_element_by_xpath(my_device_xpath)                # 기기변경 창 호출
            elem.click()
            time.sleep(3)
            elem = driver.find_element_by_xpath(change_device_button)
            elem.click()
            time.sleep(3)
            # elem = driver.find_element_by_xpath(logout_xpath)
            # if elem.text == "로그아웃":                                             # 로그인 성공
            #     print("로그인 성공")
            #     elem.click()
            #     time.sleep(3)
            #     elem = driver.find_element_by_xpath(logout_xpath)
            #     if elem.text == "회원가입":                                         # 로그아웃 성공
            #         print("로그아웃 완료")
            #         message = "[" + time_now() + "]" + " 오케이닥터 로그인/로그아웃 스크립트 성공"
            #         send_slack_message(message)

        #패키지 선택
        elem = driver.find_element_by_xpath("//button[@class='form-select']")
        elem.click()
        time.sleep(1)

        #결제 페이지 이동
        elem = driver.find_element_by_xpath("//button[@class='button-form active']")
        elem.click()
        driver.implicitly_wait(2)
        time.sleep(3)

        #결제 이름 입력
        # elem = driver.find_element_by_xpath("//div[@class='input-content']/input[@id='name']")
        elem = driver.find_element_by_id('name')
        elem.send_keys("test")

        #주소검색 버튼 클릭
        elem = driver.find_element_by_xpath("//div[@class='input-content']/button")
        elem.click()
        time.sleep(3)

        # 주소 검색 창으로 접근
        window_list = driver.window_handles
        driver.switch_to.window(window_list[1])
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe")))

        #주소 입력
        elem = driver.find_element_by_id("region_name")
        elem.send_keys("엔씨타워")

        #검색 버튼 클릭
        elem = driver.find_element_by_xpath("//button[@class='btn_search']/span[@class='img_post']")
        elem.click()
        time.sleep(2)

        #주소 클릭
        elem = driver.find_element_by_xpath("//button[@class='link_post']/span[@class='txt_addr']")
        elem.click()

        # 다시 이전 브라우저로 접근
        driver.switch_to.window(window_list[0])
        time.sleep(3)

        # 구매 동의 버튼 클릭
        # elem = driver.find_element_by_id("agree-label")
        driver.execute_script("document.getElementById('agree-label').click()")
        time.sleep(3)

        # 결제하기 버튼 클릭
        driver.execute_script("document.getElementsByClassName('buttons')[0].firstElementChild.click()")
        time.sleep(3)

        # 결제 창으로 접근
        window_list = driver.window_handles
        print(window_list)
        driver.switch_to.window(window_list[-1])
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe")))

        # 전체동의 클릭
        elem = driver.find_element_by_id("assentAll")
        elem.click()

        # 다음 버튼 클릭
        elem = driver.find_element_by_link_text("다음")
        elem.click()

        # 구매 내역 동의 클릭
        elem = driver.find_element_by_id("chk_payinput")
        elem.click()

        # 다음 버튼 클릭
        elem = driver.find_element_by_link_text("다음")
        elem.click()
        time.sleep(3)

        # 카드사 결제모듈 창으로 이동
        window_list = driver.window_handles
        print(window_list)
        driver.switch_to.window(window_list[-1])
        time.sleep(1)

        # 신한카드 - 다른결제 버튼 클릭
        driver.execute_script("doView(2);")
        time.sleep(1)

        # 신한카드 - 일반결제 클릭
        elem = driver.find_element_by_xpath("//div[@id='otherView']/div[@class='npm_content02']/ul/li[2]/a")
        elem.click()

        # 신한카드 - 일반결제 - 카드번호 입력
        elem = driver.find_element_by_xpath("//div[@class='input_area']/input[1]")
        elem.send_keys("1111")
        time.sleep(1)

        elem = driver.find_element_by_xpath("//div[@class='input_area']/input[2]")
        elem.click()
        time.sleep(1)
        # pyautogui.typewrite("1234")
        pyautogui.press(['1','2','3','4'])

        elem = driver.find_element_by_xpath("//div[@class='input_area']/input[3]")
        elem.click()
        time.sleep(1)
        # pyautogui.typewrite("1234")
        pyautogui.press(['1', '2', '3', '4'])

        elem = driver.find_element_by_xpath("//div[@class='input_area']/input[4]")
        elem.send_keys("4444")
        time.sleep(1)

        time.sleep(99999)

    except (Exception, UnboundLocalError) as e:
        print('-----')
        print(e)
        message = "[" + time_now() + "]" + url_info + "Exception Error :: 오케이닥터 로그인 스크립트를 확인해주세요. \n cc.<@UNWSR3FFF>"
        send_slack_message(message)
    finally:
        print("결제 체크 함수 탈출")
        driver.quit()

if __name__ == "__main__":
    payment_check("drmuzy", "http://okaydoctor.co.kr", "chrome")
    # driver = webdriver.Chrome(options=options)
    # driver.get("https://okaydoctor.co.kr")
    # window_org = driver.window_handles
    # print(window_org)
    # time.sleep(1)
    # driver.quit()