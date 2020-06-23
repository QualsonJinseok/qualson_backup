#==============
HOST = '0.0.0.0'
PORT = 8082
DEBUG = True
#==============
#token = "xoxb-17323563908-853572125040-xzy0BvQV5lwHRn7hW5JhJ7pu"
token = "xoxb-17323563908-853572125040-3Bb11h4hTjLMXhGILgf5soR1"    #slack
test_channel = 'GR5MLV2CE'  # 테스트 채널
real_channel = 'GSYGK4VTR'  # 메인 채널
#-----
tm_token = '1054925468:AAGO1mfY13B8p7uoo90uZWeECnLfvJua4u4'     # telegram
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
url_list = ["http://okaydoctor.co.kr/", "http://okaydoctor.co.kr/list", "http://127.0.0.1:8081/404"]
#-----
# path info list
url_path = []
#-----
driver_path = "C:/Users/jinse/PycharmProjects/qualson/2.selenium_test_script/9_monitor_server"
#-----
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
ID = 'drmuzy.com-client'
PW = 'KjsdE;!aV-4ua4G@@T?4q#KCpGVey2'
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
    'username' : 'test_001@qualson.com',
    'password' : '12345678'
}
#-----
UPC = 60252777372