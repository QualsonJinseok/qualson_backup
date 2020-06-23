#==========
#브릿잉글리쉬
#==========
brit_test_id = "secret"
brit_test_pw = "111111"
#----------
# 카테고리 로그인 버튼 xpath >>>>>>>>>>>> https://britenglish.co.kr/login 페이지로 이동해도 됨
BR_login_text_xpath = "/html/body[@class='home_page membership_page']/div[@class='wrap']/div[@class='header']/div[@class='main_nav']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='lnb']/li[3]/a"
# 이메일 필드 xpath
BR_email_xpath = "//body/div/div[3]/div/div/div/p[1]/label/input"
# 비밀번호 필드 xpath
BR_password_xpath= "//body/div/div[3]/div/div/div/p[2]/label/input"
# 로그인 버튼 xpath
BR_login_func_xpath = "//div[@class='rel_account']/button[@name='btLogin']"
# 로그아웃(=회원가입) xpath
# BR_MY_dropdown = "/html/body[@class='home_page membership_page']/div[@class='wrap']/div[@class='header']/div[@class='main_nav']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='lnb']/li[3]/a[@class='bt_dropdown']"
BR_MY_dropdown = "//body/div/div/div/div/div/ul[2]/li[3]/a"
# BR_logout_xpath = "/html/body[@class='home_page membership_page']/div[@class='wrap']/div[@class='header']/div[@class='main_nav']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='lnb']/li[3]/div[@class='sub_lnb']/a[3]"
BR_logout_xpath = "//body/div/div/div/div/div/ul[2]/li[3]/div/a[3]"
# 등록기기 변경 창
BR_change_device_popup = ""
# 내 기기 버튼 xpath
BR_my_device_xpath = ""
# 기기 변경 버튼 xapth
BR_change_device_button = ""

#==========
#리얼클래스
#==========
real_test_id = "secret"
real_test_pw = "12345678"
#----------
# 카테고리 로그인 버튼 xpath >>>>>>>>>>>>>> https://realclass.co.kr/login 페이지로 이동해도 됨
RC_login_text_xpath = "/html/body[@class='home']/div[@class='wrap']/div[@class='header main_theme']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='sub_nav']/li[2]/a"
# 이메일 필드 xpath
RC_email_xpath = "/html/body/div[@class='wrap']/div[@class='main']/div[@class='inner clearfix']/div[@class='account_form login_form']/div[@class='input_area']/p[1]/input[@id='email']"
# 비밀번호 필드 xpath
RC_password_xpath = "/html/body/div[@class='wrap']/div[@class='main']/div[@class='inner clearfix']/div[@class='account_form login_form']/div[@class='input_area']/p[2]/input[@id='password']"
# 로그인 버튼 xpath
RC_login_func_xpath = "/html/body/div[@class='wrap']/div[@class='main']/div[@class='inner clearfix']/div[@class='account_form login_form']/p[@class='btn_group'][1]/button[@id='doLogin']"
# 로그아웃(=회원가입) xpath
# RC_MY_dropdown = "/html/body[@class='home']/div[@class='wrap']/div[@class='header main_theme']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='sub_nav']/li/a[@class='my_menu class_menu hasSubmenu']"
RC_MY_dropdown = "//body/div/div/div/div/ul[2]/li/a"
# RC_logout_xpath = "/html/body[@class='home']/div[@class='wrap']/div[@class='header main_theme']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='sub_nav']/li/ul[@class='float_nav sub_my_menu']/li[4]/a"
RC_logout_xpath = "//body/div/div/div/div/ul[2]/li/ul/li[4]/a"
# 등록기기 변경 창
RC_change_device_popup = ""
# 내 기기 버튼 xpath
RC_my_device_xpath = ""
# 기기 변경 버튼 xapth
RC_change_device_button = ""

#==========
#홈글리쉬
#==========
home_test_id = "secret"
home_test_pw = "12345678"
#----------
# 카테고리 로그인 버튼 xpath
HG_login_text_xpath = "//body/div/div/div/div/div[2]/div[2]"
# 이메일 필드 xpath
HG_email_xpath = "/html/body/div[@id='modal-root--homeglish']/div[@class='sc-gacfCG intGJw']/div[@class='sc-epGmkI sc-sPYgB IajpG']/div[@class='sc-bvTASY sc-iHhHRJ llIzKL'][1]/input"
# 비밀번호 필드 xpath
HG_password_xpath = "/html/body/div[@id='modal-root--homeglish']/div[@class='sc-gacfCG intGJw']/div[@class='sc-epGmkI sc-sPYgB IajpG']/div[@class='sc-bvTASY sc-iHhHRJ llIzKL'][2]/div/input"
# 로그인 버튼 xpath
HG_login_func_xpath = "/html/body/div[@id='modal-root--homeglish']/div[@class='sc-gacfCG intGJw']/div[@class='sc-epGmkI sc-sPYgB IajpG']/div[@class='sc-dphlzf sc-dHIava jCgJgt']/button"
# 로그아웃(=회원가입) xpath
HG_MY_dropdown = "//body/div/div/div/div/div[2]/div[2]/div[2]"
HG_logout_xpath = "/html/body/div[@id='__next']/div[@class='sc-kRCAcj kBKpyD']/div[@class='sc-bUqnYt eMWONU']/div[@class='sc-fIIFii kzjZwN']/div[@class='sc-fQfKYo bAIjtj']/div[@class='sc-fjNYmT ikarFt'][2]"
# 등록기기 변경 창
HG_change_device_popup = ""
# 내 기기 버튼 xpath
HG_my_device_xpath = ""
# 기기 변경 버튼 xapth
HG_change_device_button = ""

#==========
#오케이닥터
#==========
# 오케이닥터 테스트 계정
okdoctor_test_id = "secret"
okdoctor_test_pw = "12345678"
#----------
# 카테고리 로그인 버튼 xpath
DM_login_text_xpath = "/html/body/div[@id='root']/div[@class='desktop']/header/div[@class='_3GwDZImVGlVe7RrtzYD9MB']/div[@class='site-nav-wrap']/ul[@class='nav-right']/li[@class='line'][1]"
# 이메일 필드 xpath
DM_email_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='tmo1ZGn8PBnvU7CKfq2vA username validation-null error-false']/input[@id='input-username']"
# 비밀번호 필드 xpath
DM_password_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='tmo1ZGn8PBnvU7CKfq2vA password validation-null error-false']/input[@id='input-password']"
# 로그인 기능 xpath
DM_login_func_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='buttons']/button[@class='_3OY37ptzeNAwwBT1cLg7mB btn']"
# 로그아웃(=회원가입) xpath
DM_logout_xpath = "/html/body/div[@id='root']/div[@class='desktop']/header/div[@class='_3GwDZImVGlVe7RrtzYD9MB']/div[@class='site-nav-wrap']/ul[@class='nav-right']/li[2]"
# 등록기기 변경 창
DM_change_device_popup = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/div[@class='title']"
# 내 기기 버튼 xpath
DM_my_device_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/form/div[@class='list-wrapper']/div[@class='device-content']/ul[@class='device-list']/li[5]/span[2]/span[@class='name']"
# 기기 변경 버튼 xapth
DM_change_device_button = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/form/div[@class='_3suviiVZu4wgNQVxCubfEO active']/button"

#=============

package_info = {
    "britenglish" : {
        "test_id" : brit_test_id,
        "test_pw" : brit_test_pw,
        "login_text_xpath" : BR_login_text_xpath,
        "email_xpath" : BR_email_xpath,
        "password_xpath" : BR_password_xpath,
        "login_func_xpath" : BR_login_func_xpath,
        "logout_xpath" : BR_logout_xpath,
        "change_device_popup" : "",
        "my_device_xpath" : "",
        "change_device_button" : "",
        "my_dropdown" : BR_MY_dropdown
    },
    "realclass" : {
        "test_id" : real_test_id,
        "test_pw" : real_test_pw,
        "login_text_xpath": RC_login_text_xpath,
        "email_xpath": RC_email_xpath,
        "password_xpath": RC_password_xpath,
        "login_func_xpath": RC_login_func_xpath,
        "logout_xpath": RC_logout_xpath,
        "change_device_popup" : "",
        "my_device_xpath" : "",
        "change_device_button": "",
        "my_dropdown" : RC_MY_dropdown
    },
    "homeglish" : {
        "test_id" : home_test_id,
        "test_pw" : home_test_pw,
        "login_text_xpath": HG_login_text_xpath,
        "email_xpath": HG_email_xpath,
        "password_xpath": HG_password_xpath,
        "login_func_xpath": HG_login_func_xpath,
        "logout_xpath": HG_logout_xpath,
        "change_device_popup": "",
        "my_device_xpath": "",
        "change_device_button": "",
        "my_dropdown" : HG_MY_dropdown
    },
    "drmuzy" : {
        "test_id" : okdoctor_test_id,
        "test_pw" : okdoctor_test_pw,
        "login_text_xpath": DM_login_text_xpath,
        "email_xpath": DM_email_xpath,
        "password_xpath": DM_password_xpath,
        "login_func_xpath": DM_login_func_xpath,
        "logout_xpath": DM_logout_xpath,
        "change_device_popup": DM_change_device_popup,
        "my_device_xpath": DM_my_device_xpath,
        "change_device_button": DM_change_device_button
    }
}

if __name__ == "__main__":
    print(package_info)