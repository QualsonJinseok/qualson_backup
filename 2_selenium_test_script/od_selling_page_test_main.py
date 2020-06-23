# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
#import json
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import string
from variable_info import *
import od_selling_page_test_module
import requests
#==================================================
# 크롬 실행 시, 최대화 옵션
options = Options()
options.add_argument("--start-maximized")
#obile_emulation = {
#    "deviceName": "iPhone 8"
    #"deviceName": "iPhone X"
#}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
#options.add_argument("--disable-gpu")
#==================================================
'''
class sellingPageApply(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options)

        # 랜덤한 하나의 숫자를 뽑아서, 문자열 결합을 한다. == 각 케이스별로 다른 전화번호
        self.string_pool = string.digits  # --> "0123456789"
        self._LEGNTH = 8  # --> 010 뒤 8자리 숫자
        self.phone_result = "017"
        for i in range(self._LEGNTH):
            self.phone_result += random.choice(self.string_pool)

    def tearDown(self):
        self.driver.quit()

    def xy_value(self, elem):
        # 페이지 좌표 찾기
        # 클래스 내에서 좌표찾기 함수 실행 시 == self.xy_value(elem)
        print(elem.location)
        print(elem.size)
    #####
    def sendToApplyFormat(self, driver):
        #driver = self.driver
        #driver.get(url_staging + path_nsda_list[0])
        #self.assertIn("영어가 생활이 되는, 오케이닥터", driver.title)

        #1. 하단셀링바 이름 영역
        elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2Dvda_rYdQJkmNJb4e68O- section']/div[@class='selling-wrap']/div[@class='input-column']/input[@class='name small']")
        elem.click()
        elem.send_keys("QA_test")

        #2. 하단셀링바 전화번호 영역
        elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2Dvda_rYdQJkmNJb4e68O- section']/div[@class='selling-wrap']/div[@class='input-column']/input[@class='phone small']")
        elem.click()
        elem.send_keys(self.phone_result)
        time.sleep(1)

        #3. 하단셀링바 신청하기 버튼 클릭
        elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2Dvda_rYdQJkmNJb4e68O- section']/div[@class='selling-wrap']/div[@class='counsel-button']/button[@class='_33lkNpAYQbR-wW_UBPZuEV']/div[@class='content']/p")
        driver.execute_script("arguments[0].click()", elem)

        time.sleep(1)
        self.assertIn("상담신청이 완료되었습니다.", driver.find_element_by_xpath(apply_success_xpath).text)

        #4. 무료 학습 상담신청 화면으로 스크롤
        driver.execute_script("window.scrollTo(629, 19500);")

        #5. 패키지 파트 이름 영역
        elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-input']/input[@id='consult-name']")
        elem.click()
        time.sleep(1)
        elem.send_keys("QA_test")

        #6. 패키지 파트 전화번호 영역
        elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='counsel-input-wrap']/div[@class='counsel-input']/input[@class='phone big']")
        elem.click()
        time.sleep(1)
        elem.send_keys(self.phone_result)

        #7. 패키지 파트 무료상담신청
        elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='apply-button']/button[@class='_33lkNpAYQbR-wW_UBPZuEV apply']/div[@class='content']/p")
        driver.execute_script("arguments[0].click()", elem)
        time.sleep(1)
        return 200

    def sample_sub(self):
        for i in path_nsda_list:
            yield url_staging + i

    # 테스트 케이스 반복하기
    def test_loop(self):
        my_generator = self.sample_sub()
        driver = self.driver

        for i in range(len(path_nsda_list)):
            url_1 = next(my_generator)
            #print(url_1)
            driver.get(url_1)
            # 검증 시작
            time.sleep(1)
            self.assertIn("영어가 생활이 되는, 오케이닥터", driver.title)
            self.assertIs(self.sendToApplyFormat(driver), 200)

    #@unittest.skip("demonstrating skipping")
    def test_1(self):
        print('test_1 is done')
'''
#==================================================
class ThisIsSampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options)

        # 랜덤한 하나의 숫자를 뽑아서, 문자열 결합을 한다. == 각 케이스별로 다른 전화번호
        self.string_pool = string.digits  # --> "0123456789"
        self._LEGNTH = 8  # --> 010 뒤 8자리 숫자
        self.phone_result = "017"
        for i in range(self._LEGNTH):
            self.phone_result += random.choice(self.string_pool)

    def tearDown(self):
        self.driver.quit()

    # 테스트 URL 조합
    def sample_sub(self):
        for i in total_url:
        #for i in path_nsda_popup_list:
        #for i in path_nsda_list:
            yield url_staging + i

    # 셀링페이지 상담신청하기 기능 테스트 케이스 반복하기
    def test_loop(self):
        my_generator = self.sample_sub()
        driver = self.driver
        phone_result = self.phone_result
        z = dict()
        z['final_result'] = "success"

        for i in range(len(total_url)): #url 배열 갯수만큼 진행
            url_set = next(my_generator)
            z['url_set'] = url_set
            time.sleep(1)
            #기본 검증 구문
            z['response_data'], z['test_issue'] = od_selling_page_test_module.sellingPageApply2.send2apply(url_set, driver, phone_result)

            if z['response_data'] == 200:
                continue
            else:
                requests.post('http://127.0.0.1:8081/result', data=z)
                z['final_result'] = "fail"
                continue
        print(z['final_result'])
        self.assertEqual(z['final_result'], "success", z['test_issue'])

#==================================================
# 테스트 묶음 생성
#def suite():
    #suite = unittest.TestSuite()
    #suite.addTest(SellingPageApply('def_1', *args, **kwargs)) -> 클래스 __init__ 기본값으로 파라미터 전달해서, 변수명 셋팅 가능
    #suite.addTest(ThisIsSampleTest('test_loop'))
    #suite.addTests([sellingPageApply('test_loop'), sellingPageApply('test_1')])
    #return suite
#==================================================
# 테스트 시작
if __name__ == "__main__":
    #unittest.TextTestRunner().run()
    #unittest.TextTestResult().run()
    unittest.main()
    #runner = unittest.TextTestResult()
    #runner.run(suite())