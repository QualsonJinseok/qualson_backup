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
#크롬 실행 시, 최대화 옵션
options = Options()
options.add_argument("--start-maximized")
mobile_emulation = {
    "deviceName": "iPhone 8"
    #"deviceName": "iPhone X"
}
#크롬을 모바일 환경으로 실행
options.add_experimental_option("mobileEmulation", mobile_emulation)
#options.add_argument("--disable-gpu")
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
            time.sleep(1)
            #기본 검증 구문
            z['response_data'], z['test_issue'] = od_selling_page_test_module.sellingPageApply2.send2applyMobile(url_set, driver, phone_result)

            if z['response_data'] == 200:
                continue
            else:
                requests.post('http://127.0.0.1:8081/result', data=z)
                z['final_result'] = "fail"
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