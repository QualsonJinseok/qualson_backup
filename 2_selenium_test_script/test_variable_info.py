#==============
# slack_webhook_info
#==============
#token = "secret"
token = "secret"    #slack
test_channel = 'secret'
real_channel = 'secret'

tm_token = 'secret'     # telegram
run_channel = -234845754  # 구동 로그 채널 ID
err_channel = -333712900  # 오류 로그 채널 ID
#==============
# url info
url_dev = "https://192.168.4.8"
url_staging = "https://front-dev.okaydoctor.co.kr"
url_real = "https://okaydoctor.co.kr"

#==============
# path info list
path_basic_list = ["/event/preorder", "/event/preordery", "/event/preordersp", "/pops"]
###
path_nsda_list = ["/event/nsda_pops", "/event/nsda_alarm", "/event/nsda_quiz", "/event/nsda_doctor", "/event/nsda_pops2"]
###
path_ntb_list = ["/event/preorderquiz", "/event/preorderquizb", "/event/preorderlecture", "/event/preorderfunction"]
###
path_etc_list = ["/event/preordery_sample", "/event/preorderlecturebenefit", "/event/preordersp", "/event/preorderstudy"]
### popup 페이지는 별도의 팝업을 체크하고 닫는 루틴이 필요.
path_nsda_popup_list = ["/event/popup/10m", "/event/popup/nsda_quiz2", "/event/popup/nsda_pops3", "/event/popup/nsda_alarm", "/event/popup/nsda_doctor"]
#==============
driver_path = "C:/Users/jinse/PycharmProjects/qualson/2.selenium_test_script"
#==============
#실전용
#total_url = path_basic_list + path_nsda_list + path_ntb_list + path_etc_list + path_nsda_popup_list

#테스트용
total_url = ["/selling/v2/package_doctor_new/scholar", "/event/popup/10m",]
#total_url = ["/event/popup/10m", "/event/preorder"]
#==============
#PC 버전
#신청 성공 토스트
apply_success_xpath = "/html/body/div[@id='root']/div[@class='_18SEQ0vgQuWaFsNeaI0gGE']/div[@class='toast-item app appear']/span"
#popup url 쿠폰받기 버튼
coupon_xpath = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='knmqVmOtrevift4qGLlHN pc']/div[@class='popup-wrap']/div[@class='popup-btn-wrap']/button[@class='popup-btn']"
#==============
#모바일 버전
#신청 성공 토스트
apply_success_xpath_mobile = "/html/body/div[@id='root']/div[@class='_18SEQ0vgQuWaFsNeaI0gGE']/div[@class='toast-item app disappear']/span"
#popup url 쿠폰받기 버튼
coupon_xpath_mobile = "/html/body/div[@id='root']/div[@class='_2kKBzp1Cuj93qOFUvpfxih dim-wrapper']/div[@class='knmqVmOtrevift4qGLlHN']/div[@class='popup-wrap']/div[@class='popup-btn-wrap']/button[@class='popup-btn']"
#==============
#total_url = path_basic_list + path_nsda_list + path_ntb_list + path_etc_list + path_nsda_popup_list

#==============
#nsda_pops 메인 유튜브 영상 재생 태그 정보
#재생 전
#html5-video-player ytp-embed ytp-embed-playlist ytp-embeds-smallmode ytp-title-enable-channel-logo unstarted-mode ytp-hide-controls ytp-small-mode

#재생 중 일시정지
#html5-video-player ytp-embed ytp-embed-playlist ytp-embeds-smallmode ytp-small-mode ytp-title-enable-channel-logo paused-mode ytp-expand-pause-overlay

#재생 중
#html5-video-player ytp-embed ytp-embed-playlist ytp-embeds-smallmode ytp-small-mode ytp-title-enable-channel-logo playing-mode

#재생 끝
#html5-video-player ytp-embed ytp-embed-playlist ytp-embeds-smallmode ytp-small-mode ytp-title-enable-channel-logo ended-mode


