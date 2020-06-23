#==============
HOST = '0.0.0.0'
PORT = 8084
DEBUG = True
USE_RELOADER = False
#==============
#token = "secret"
token = "secret"    #slack
test_channel = 'secret'  # 테스트 채널
real_channel = 'secret'  # 메인 채널
#-----
tm_token = 'secret'     # telegram
run_channel = -234845754  # 구동 로그 채널 ID
err_channel = -333712900  # 오류 로그 채널 ID
#-----
# url info
#url_dev = "https://192.168.4.8"
url_dev = "https://front-dev.okaydoctor.co.kr"
url_staging = "https://front-stage.okaydoctor.co.kr"
url_real = "https://okaydoctor.co.kr"
#-----
# Test Url Info
url_list = ["http://okaydoctor.co.kr/", "http://okaydoctor.co.kr/list/", "https://realclass.co.kr/", "https://britenglish.co.kr/", "https://homeglish.com/"]
#-----
# path info list
url_path = []
#-----
driver_path = "C:/Users/jinse/PycharmProjects/qualson/2.selenium_test_script/9_monitor_server"
#==========
#오케이닥터
#==========
# 카테고리 로그인 버튼 xpath
login_text_xpath = "/html/body/div[@id='root']/div[@class='desktop']/header/div[@class='_3GwDZImVGlVe7RrtzYD9MB']/div[@class='site-nav-wrap']/ul[@class='nav-right']/li[@class='line'][1]"
# 이메일 필드 xpath
email_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='tmo1ZGn8PBnvU7CKfq2vA username validation-null error-false']/input[@id='input-username']"
# 비밀번호 필드 xpath
password_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='tmo1ZGn8PBnvU7CKfq2vA password validation-null error-false']/input[@id='input-password']"
# 로그인 기능 xpath
login_func_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='_1oNo7ULVfdYEQzsmQL5G8g']/form/div[@class='buttons']/button[@class='_3OY37ptzeNAwwBT1cLg7mB btn']"
# 로그아웃(=회원가입) xpath
logout_xpath = "/html/body/div[@id='root']/div[@class='desktop']/header/div[@class='_3GwDZImVGlVe7RrtzYD9MB']/div[@class='site-nav-wrap']/ul[@class='nav-right']/li[2]"
# 등록기기 변경 창
change_device_popup = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/div[@class='title']"
# 내 기기 버튼 xpath
my_device_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/form/div[@class='list-wrapper']/div[@class='device-content']/ul[@class='device-list']/li[5]/span[2]/span[@class='name']"
# 기기 변경 버튼 xapth
change_device_button = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='GK1MjitvmlgPQjwvjQuL isController-false']/form/div[@class='_3suviiVZu4wgNQVxCubfEO active']/button"
#-----
# 오케이닥터 테스트 계정
okdoctor_test_id = "secret"
okdoctor_test_pw = "12345678"
#==========
# 슬랙봇 채널 셋팅
channel_switch = False
#channel_switch = True
#-----
# 카카오톡 메시지 발송 여부 셋팅
#kakao_setting = True
kakao_setting = False
#========================================
############# API 체크 셋팅 #############
#========================================
ID = 'secret'
PW = 'secret'
#-----
API_URL = 'https://api.okaydoctor.co.kr'
AUTH_PATH = '/oauth/token'
URL_PATH = '/player/{upc}'
#-----
AUTH_URL = API_URL + AUTH_PATH
URL_SET = API_URL + URL_PATH
#-----
FORM_DATA = {
    'grant_type':'password',
    'username' : 'secret',
    'password' : '12345678'
}
#-----
UPC = 60252777372       # == Glad you came

COUNTER = 0

