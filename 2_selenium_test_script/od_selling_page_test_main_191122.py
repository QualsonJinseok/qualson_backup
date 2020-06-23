# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import string
from variable_info import *
#import od_selling_page_test_module
#==================================================
# 랜덤한 하나의 숫자를 뽑아서, 문자열 결합을 한다. == 각 케이스별로 같은 전화번호
# class로 기능 구현해보기
'''
string_pool = string.digits  # --> "0123456789"
_LEGNTH = 4  # --> 010 뒤 8자리 숫자
phone_result = "0109999"
for i in range(_LEGNTH):
    phone_result += random.choice(string_pool)
'''
#-----------
# 크롬 실행 시, 최대화 옵션
options = Options()
options.add_argument("--start-maximized")
#options.add_argument("--disable-gpu")

#==================================================
def sample_sub(ccc):
    url_set = ccc.get(url_staging + path_nsda_list[2])
    return url_set


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
        print(elem.location)
        print(elem.size)
        # 클래스 내에서 좌표찾기 함수 실행 시 == self.xy_value(elem)

    def test_sample_main(self):
        driver = self.driver
        sample_sub(driver)
        
        self.assertIn("영어가 생활이 되는, 오케이닥터", driver.title)

    def test_sendToApplyFormat_floatingBar(self):
        driver = self.driver
        driver.get(url_staging + path_nsda_list[0])

        self.assertIn("영어가 생활이 되는, 오케이닥터", driver.title)

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

        return 200

    def test_sendToApplyFormat_packigingScreen(self):
        driver = self.driver
        driver.get(url_staging + path_nsda_list[0])

        self.assertIn("영어가 생활이 되는, 오케이닥터", driver.title)

        # 4-1. 패키지 카테고리 클릭
        # elem = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@class='_2f4eaKjpzUJBkw1mvt6Bgb section']/div[@class='nav-wrap']/div[@class='title-list']/button[@class='navigation-item item-wrapper'][7]/div[@class='text-wrap']/div[@class='title']")
        # elem.click()
        # time.sleep(3)

        # 4-2. 무료 학습 상담신청 화면으로 스크롤
        driver.execute_script("window.scrollTo(629, 19500);")

        # 5. 패키지 파트 이름 영역
        elem = driver.find_element_by_xpath(
            "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/input[@class='name big']")
        elem.click()
        time.sleep(1)
        elem.send_keys("QA_test")

        # 6. 패키지 파트 전화번호 영역
        elem = driver.find_element_by_xpath(
            "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/input[@class='phone big']")
        elem.click()
        time.sleep(1)
        elem.send_keys(self.phone_result)

        # 7. 패키지 파트 무료상담신청
        elem = driver.find_element_by_xpath(
            "/html/body/div[@id='root']/div[@class='_2nGb-DBFyJGs0ws8x8bUrV']/div[@id='package']/div[@class='consult-apply']/div[@class='selling-wrap']/div[@class='apply-button']/button[@class='_33lkNpAYQbR-wW_UBPZuEV apply']/div[@class='content']/p")
        driver.execute_script("arguments[0].click()", elem)
        time.sleep(1)

    '''    
    # 테스트 케이스 반복하기
    def test_even(self):
        for i in range(0, 3):
            with self.subTest(i=i):
                self.assertEqual(self.test_sendToApplyFormat_floatingBar(), 200)
    '''

#class sellingPageApply_2():


#==================================================
# 테스트 묶음 생성
def suite():
    suite = unittest.TestSuite()
    #suite.addTest(sellingPageApply('test_even'))
    suite.addTest(sellingPageApply('test_sendToApplyFormat_floatingBar'))
    #suite.addTest(sellingPageApply('test_sendToApplyFormat_packigingScreen'))
    #suite.addTest(sellingPageApply_2('test_sendToApplyFormat_packigingScreen'))

    #suite.addTest(SellingPageApply('def_1', *args, **kwargs)) -> 클래스 __init__ 기본값으로 파라미터 전달해서, 변수명 셋팅해보기
    return suite

# 테스트 시작
if __name__ == "__main__":
    #unittest.TextTestRunner().run(suite())
    unittest.TextTestResult().run(suite())
    #unittest.main()