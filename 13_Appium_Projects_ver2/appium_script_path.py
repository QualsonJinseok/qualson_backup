#==========
#브릿잉글리쉬
#==========
brit_test_id = "qatest006@qualson.com"
brit_test_pw = "111111"
#----------
# app 파트
#----------
# 카테고리 로그인 버튼 xpath >>>>>>>>>>>> https://britenglish.co.kr/login 페이지로 이동해도 됨
app_BR_login_text_xpath = "/html/body[@class='home_page membership_page']/div[@class='wrap']/div[@class='header']/div[@class='main_nav']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='lnb']/li[3]/a"
# 이메일 필드 xpath
app_BR_email_xpath = "//body/div/div[3]/div/div/div/p[1]/label/input"
# 비밀번호 필드 xpath
app_BR_password_xpath= "//body/div/div[3]/div/div/div/p[2]/label/input"
# 로그인 버튼 xpath
app_BR_login_func_xpath = "//div[@class='rel_account']/button[@name='btLogin']"
# 로그아웃(=회원가입) xpath
# BR_MY_dropdown = "/html/body[@class='home_page membership_page']/div[@class='wrap']/div[@class='header']/div[@class='main_nav']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='lnb']/li[3]/a[@class='bt_dropdown']"
app_BR_MY_dropdown = "//body/div/div/div/div/div/ul[2]/li[3]/a"
# BR_logout_xpath = "/html/body[@class='home_page membership_page']/div[@class='wrap']/div[@class='header']/div[@class='main_nav']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='lnb']/li[3]/div[@class='sub_lnb']/a[3]"
app_BR_logout_xpath = "//body/div/div/div/div/div/ul[2]/li[3]/div/a[3]"
# 등록기기 변경 창
app_BR_change_device_popup = ""
# 내 기기 버튼 xpath
app_BR_my_device_xpath = ""
# 기기 변경 버튼 xapth
app_BR_change_device_button = ""

#==========
#리얼클래스
#==========
real_test_id = "test300@qualson.com"
real_test_pw = "12345678"
#----------
# app 파트
#----------
# 카테고리 로그인 버튼 xpath >>>>>>>>>>>>>> https://realclass.co.kr/login 페이지로 이동해도 됨
app_RC_login_text_xpath = "/html/body[@class='home']/div[@class='wrap']/div[@class='header main_theme']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='sub_nav']/li[2]/a"
# 이메일 필드 xpath
app_RC_email_xpath = "/html/body/div[@class='wrap']/div[@class='main']/div[@class='inner clearfix']/div[@class='account_form login_form']/div[@class='input_area']/p[1]/input[@id='email']"
# 비밀번호 필드 xpath
app_RC_password_xpath = "/html/body/div[@class='wrap']/div[@class='main']/div[@class='inner clearfix']/div[@class='account_form login_form']/div[@class='input_area']/p[2]/input[@id='password']"
# 로그인 버튼 xpath
app_RC_login_func_xpath = "/html/body/div[@class='wrap']/div[@class='main']/div[@class='inner clearfix']/div[@class='account_form login_form']/p[@class='btn_group'][1]/button[@id='doLogin']"
# 로그아웃(=회원가입) xpath
# RC_MY_dropdown = "/html/body[@class='home']/div[@class='wrap']/div[@class='header main_theme']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='sub_nav']/li/a[@class='my_menu class_menu hasSubmenu']"
app_RC_MY_dropdown = "//body/div/div/div/div/ul[2]/li/a"
# RC_logout_xpath = "/html/body[@class='home']/div[@class='wrap']/div[@class='header main_theme']/div[@class='inner']/div[@class='nav_container clearfix']/ul[@class='sub_nav']/li/ul[@class='float_nav sub_my_menu']/li[4]/a"
app_RC_logout_xpath = "//body/div/div/div/div/ul[2]/li/ul/li[4]/a"
# 등록기기 변경 창
app_RC_change_device_popup = ""
# 내 기기 버튼 xpath
app_RC_my_device_xpath = ""
# 기기 변경 버튼 xapth
app_RC_change_device_button = ""

#==========
#홈글리쉬
#==========
home_test_id = "qa200@qualson.com"
home_test_pw = "12345678"
#----------
# app 파트
#----------
# 카테고리 로그인 버튼 xpath
app_HG_login_text_xpath = "//body/div/div/div/div/div[2]/div[2]"
# 이메일 필드 xpath
app_HG_email_xpath = "/html/body/div[@id='modal-root--homeglish']/div[@class='sc-gacfCG intGJw']/div[@class='sc-epGmkI sc-sPYgB IajpG']/div[@class='sc-bvTASY sc-iHhHRJ llIzKL'][1]/input"
# 비밀번호 필드 xpath
app_HG_password_xpath = "/html/body/div[@id='modal-root--homeglish']/div[@class='sc-gacfCG intGJw']/div[@class='sc-epGmkI sc-sPYgB IajpG']/div[@class='sc-bvTASY sc-iHhHRJ llIzKL'][2]/div/input"
# 로그인 버튼 xpath
app_HG_login_func_xpath = "/html/body/div[@id='modal-root--homeglish']/div[@class='sc-gacfCG intGJw']/div[@class='sc-epGmkI sc-sPYgB IajpG']/div[@class='sc-dphlzf sc-dHIava jCgJgt']/button"
# 로그아웃(=회원가입) xpath
app_HG_MY_dropdown = "//body/div/div/div/div/div[2]/div[2]/div[2]"
app_HG_logout_xpath = "/html/body/div[@id='__next']/div[@class='sc-kRCAcj kBKpyD']/div[@class='sc-bUqnYt eMWONU']/div[@class='sc-fIIFii kzjZwN']/div[@class='sc-fQfKYo bAIjtj']/div[@class='sc-fjNYmT ikarFt'][2]"
# 등록기기 변경 창
app_HG_change_device_popup = ""
# 내 기기 버튼 xpath
app_HG_my_device_xpath = ""
# 기기 변경 버튼 xapth
app_HG_change_device_button = ""

#==========
# 닥터뮤지
#==========
# 닥터뮤지 테스트 계정
okdoctor_test_id = "test_002@qualson.com"
okdoctor_test_pw = "12345678"
#----------
# app 파트
#----------
# 카테고리 로그인 버튼 xpath
app_DM_login_text_xpath = "/html/body/div[@id='root']/div[@class='desktop']/header/div[@class='_3GwDZImVGlVe7RrtzYD9MB']/div[@class='site-nav-wrap']/ul[@class='nav-right']/li[@class='line'][1]"
# 이메일 필드 xpath
app_DM_email_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='tmo1ZGn8PBnvU7CKfq2vA username validation-null error-false']/input[@id='input-username']"
# 비밀번호 필드 xpath
app_DM_password_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='tmo1ZGn8PBnvU7CKfq2vA password validation-null error-false']/input[@id='input-password']"
# 로그인 기능 xpath
app_DM_login_func_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='buttons']/button[@class='_3OY37ptzeNAwwBT1cLg7mB btn']"
# 로그아웃(=회원가입) xpath
app_DM_logout_xpath = "/html/body/div[@id='root']/div[@class='desktop']/header/div[@class='_3GwDZImVGlVe7RrtzYD9MB']/div[@class='site-nav-wrap']/ul[@class='nav-right']/li[2]"
# 등록기기 변경 창
app_DM_change_device_popup = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/div[@class='title']"
# 내 기기 버튼 xpath
app_DM_my_device_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/form/div[@class='list-wrapper']/div[@class='device-content']/ul[@class='device-list']/li[5]/span[2]/span[@class='name']"
# 기기 변경 버튼 xapth
app_DM_change_device_button = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/form/div[@class='_3suviiVZu4wgNQVxCubfEO active']/button"

#----------
# inApp 파트
#----------
inApp_DM_click_packageBar_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]'
inApp_Dm_click_classJoin_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.Button'
inApp_DM_buy_nameField_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.widget.EditText'
inApp_DM_buy_nameField_id = 'name'
inApp_DM_buy_searchAddrBT_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View[2]/android.widget.Button'
inApp_DM_buy_addrInputField_id = "region_name"
inApp_DM_buy_addrSearchBT_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[8]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button'
inApp_DM_buy_addrList_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[8]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View/android.widget.ListView/android.view.View[2]/android.widget.Button'
inApp_DM_buy_paymentPopup_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]'
inApp_DM_buy_agreeBox_id = 'agree'
inApp_DM_buy_doPaymentBT_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]'
inApp_DM_LGCNS_agreeAllbox_xpath = '//android.view.View[@content-desc=" 전체 동의 체크"]'

#==========
#인스타그램
#==========
# 인스타그램 로그인 계정
insta_login_id = "hello_qualson"
insta_login_pw = "qualson"
#----------
Insta_login_ID_filed_xpath = ""
Insta_login_PW_filed_xpath = ""
Insta_login_button_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextSwitcher/android.widget.TextView'
Insta_My_tab_id = 'com.instagram.android:id/tab_avatar'
Insta_My_follow_list_button_id = 'com.instagram.android:id/row_profile_header_textview_following_count'
#
Insta_My_follow_list_drmuzy_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
Insta_My_follow_list_realclass_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
Insta_My_follow_list_britenglish_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
Insta_My_follow_list_homeglish_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'
#
Insta_website_link_id = 'com.instagram.android:id/profile_header_website'
#==========
package_info = {
    "app" : {
        "britenglish" : {
            "test_id" : brit_test_id,
            "test_pw" : brit_test_pw,
            "login_text_xpath" : app_BR_login_text_xpath,
            "email_xpath" : app_BR_email_xpath,
            "password_xpath" : app_BR_password_xpath,
            "login_func_xpath" : app_BR_login_func_xpath,
            "logout_xpath" : app_BR_logout_xpath,
            "change_device_popup" : "",
            "my_device_xpath" : "",
            "change_device_button" : "",
            "my_dropdown" : app_BR_MY_dropdown
    },
        "realclass" : {
            "test_id" : real_test_id,
            "test_pw" : real_test_pw,
            "login_text_xpath": app_RC_login_text_xpath,
            "email_xpath": app_RC_email_xpath,
            "password_xpath": app_RC_password_xpath,
            "login_func_xpath": app_RC_login_func_xpath,
            "logout_xpath": app_RC_logout_xpath,
            "change_device_popup" : "",
            "my_device_xpath" : "",
            "change_device_button": "",
            "my_dropdown" : app_RC_MY_dropdown
    },
        "homeglish" : {
            "test_id" : home_test_id,
            "test_pw" : home_test_pw,
            "login_text_xpath": app_HG_login_text_xpath,
            "email_xpath": app_HG_email_xpath,
            "password_xpath": app_HG_password_xpath,
            "login_func_xpath": app_HG_login_func_xpath,
            "logout_xpath": app_HG_logout_xpath,
            "change_device_popup": "",
            "my_device_xpath": "",
            "change_device_button": "",
            "my_dropdown" : app_HG_MY_dropdown
    },
        "drmuzy" : {
            "test_id" : okdoctor_test_id,
            "test_pw" : okdoctor_test_pw,
            "login_text_xpath": app_DM_login_text_xpath,
            "email_xpath": app_DM_email_xpath,
            "password_xpath": app_DM_password_xpath,
            "login_func_xpath": app_DM_login_func_xpath,
            "logout_xpath": app_DM_logout_xpath,
            "change_device_popup": app_DM_change_device_popup,
            "my_device_xpath": app_DM_my_device_xpath,
            "change_device_button": app_DM_change_device_button
        }
    },
    "inApp":{
        "drmuzy" : {
            "packageBar_xpath" : inApp_DM_click_packageBar_xpath,
            "classJoin_xpath" : inApp_Dm_click_classJoin_xpath,
            "buy_nameField_xpath" : inApp_DM_buy_nameField_xpath,
            "buy_nameField_id" : inApp_DM_buy_nameField_id,
            "buy_searchAddr_xpath" : inApp_DM_buy_searchAddrBT_xpath,
            "buy_addrInputField_id" : inApp_DM_buy_addrInputField_id,
            "buy_addrSearchBT_xpath" : inApp_DM_buy_addrSearchBT_xpath,
            "buy_addrList_xpath" : inApp_DM_buy_addrList_xpath,
            "buy_paymentPopup_xpath" : inApp_DM_buy_paymentPopup_xpath,
            "buy_agreeBox_id" : inApp_DM_buy_agreeBox_id,
            "buy_doPaymentBT_xpath" : inApp_DM_buy_doPaymentBT_xpath,
            "LGCNS_agreeAllbox_xpath" : inApp_DM_LGCNS_agreeAllbox_xpath
        }
    }
}


if __name__ == "__main__":
    print(package_info)