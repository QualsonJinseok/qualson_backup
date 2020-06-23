from variable_info import *
import time
#############################################################
class sellingPageApply2:

    #@unittest.skip("demonstrating skipping")
    def test_1(self):
        print('test_1 is done')

    def send2apply(url_set, driver, phone_result):
        try:
            driver.get(url_set)
            time.sleep(1)

            if "popup" in url_set:
                elem = driver.find_element_by_xpath(coupon_xpath)
                elem.click()
                time.sleep(3)

            #1. 하단셀링바 이름 영역
            elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2Dvda_rYdQJkmNJb4e68O- section']/div[@class='selling-wrap']/div[@class='input-column']/input[@class='name small']")
            elem.click()
            elem.send_keys("QA_test")

            #2. 하단셀링바 전화번호 영역
            elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2Dvda_rYdQJkmNJb4e68O- section']/div[@class='selling-wrap']/div[@class='input-column']/input[@class='phone small']")
            elem.click()
            elem.send_keys(phone_result)
            time.sleep(1)

            #3. 하단셀링바 신청하기 버튼 클릭
            elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2Dvda_rYdQJkmNJb4e68O- section']/div[@class='selling-wrap']/div[@class='counsel-button']/button[@class='_33lkNpAYQbR-wW_UBPZuEV']/div[@class='content']/p")
            driver.execute_script("arguments[0].click()", elem)

            time.sleep(1)

            if driver.find_element_by_xpath(apply_success_xpath).text == "상담신청이 완료되었습니다.":

                #4-1. 패키지 파트 이름 영역
                elem = driver.find_element_by_xpath(
                    "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-input']/input[@id='consult-name']")

                #4-2. 무료 학습 상담신청 화면으로 스크롤
                # element의 좌표값을 찾은 후, 상단 배너크기만큼 빼서 화면에 클릭가능하게 위치 시킨다.
                location_name = int(elem.location['y']) - 150
                driver.execute_script("window.scrollTo(629, {});".format(str(location_name)))

                #5. 패키지 파트 이름 영역 클릭
                elem.click()
                time.sleep(1)
                elem.send_keys("QA_test")

                # 6. 패키지 파트 전화번호 영역
                elem = driver.find_element_by_xpath(
                    "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-input']/input[@class='phone big']")
                elem.click()
                #time.sleep(1)
                elem.send_keys(phone_result)

                # 7. 패키지 파트 무료상담신청
                elem = driver.find_element_by_xpath(
                    "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='apply-button']/button[@class='_33lkNpAYQbR-wW_UBPZuEV apply']/div[@class='content']/p")
                driver.execute_script("arguments[0].click()", elem)

                time.sleep(1)

                if driver.find_element_by_xpath(apply_success_xpath).text == "상담신청이 완료되었습니다.":
                    return 200, "성공"
                else:
                    return 400, "패키지 영역 상담신청 실패" #패키지 영역 상담신청 실패
            else:
                return 401, "하단 플로팅 영역 상담신청 실패" #하단 플로팅 영역 상담신청 실패
        except Exception as ex:
            #print('에러 발생 : ', ex)
            return 402, ex

    def send2applyMobile(url_set, driver, phone_result):
        #from selenium.webdriver.common.touch_actions import TouchActions
        try:
            driver.get(url_set)
            time.sleep(1)
            #touchactions = TouchActions(driver)

            if "popup" in url_set:
                elem = driver.find_element_by_xpath(coupon_xpath_mobile)
                driver.execute_script("arguments[0].click()", elem)
                time.sleep(3)

            # 1. 하단셀링바 신청하기 버튼 클릭
            elem = driver.find_element_by_xpath(
                "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_1COpRe_fDNFNgtUzKZQyyc section']/div[@class='selling-wrap']/div[@class='btn-buy']/img[@alt='input-bg']"
            )
            driver.execute_script("arguments[0].click()", elem)

            # 2. 하단셀링바 이름 영역
            elem = driver.find_element_by_xpath(
                "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='applycounsel']/div[@class='selling-wrap']/div[@class='apply-expanded']/form/input[@class='name small']"
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            elem.send_keys("QA_test")

            # 3. 하단셀링바 전화번호 영역
            elem = driver.find_element_by_xpath(
                "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='applycounsel']/div[@class='selling-wrap']/div[@class='apply-expanded']/form/input[@class='phone small']"
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            elem.send_keys(phone_result)
            time.sleep(1)

            # 4. 신청팝업-신청하기 버튼 클릭
            elem = driver.find_element_by_xpath(
                "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='applycounsel']/div[@class='selling-wrap']/div[@class='apply-expanded']/form/button[@class='_33lkNpAYQbR-wW_UBPZuEV']/div[@class='content']"
            )
            driver.execute_script("arguments[0].click()", elem)
            time.sleep(3)

            if driver.find_element_by_xpath(apply_success_xpath_mobile).text == "상담신청이 완료되었습니다.":
                # 4-1. 패키지 파트 이름 영역
                elem = driver.find_element_by_xpath(
                    "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-input']/input[@id='consult-name']"
                )

                # 4-2. 무료 학습 상담신청 화면으로 스크롤
                # element의 좌표값을 찾은 후, 상단 배너크기만큼 빼서 화면에 클릭가능하게 위치 시킨다.
                location_name = int(elem.location['y']) - 150
                driver.execute_script("window.scrollTo(629, {});".format(str(location_name)))

                # 5. 패키지 파트 이름 영역 클릭
                elem.click()
                time.sleep(1)
                elem.send_keys("QA_test")

                # 6. 패키지 파트 전화번호 영역
                elem = driver.find_element_by_xpath(
                    "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-input']/input[@class='phone big']")
                elem.click()
                time.sleep(1)
                elem.send_keys(phone_result)

                # 7. 패키지 파트 무료상담신청
                elem = driver.find_element_by_xpath(
                    "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-btn']/button"
                )
                driver.execute_script("arguments[0].click()", elem)

                time.sleep(1)

                if driver.find_element_by_xpath(apply_success_xpath).text == "상담신청이 완료되었습니다.":
                    return 200, "성공"
                else:
                    return 400, "패키지 영역 상담신청 실패"  # 패키지 영역 상담신청 실패

            else:
                return 401, "하단 플로팅 영역 상담신청 실패"  # 하단 플로팅 영역 상담신청 실패
        except Exception as ex:
            # print('에러 발생 : ', ex)
            return 402, ex

        except Exception as ex:
            return 402, ex