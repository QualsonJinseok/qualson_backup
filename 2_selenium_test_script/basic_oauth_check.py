import json
import requests
from requests.auth import HTTPBasicAuth
#=====
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
#=====
get_access_token = requests.post(AUTH_URL, data=FORM_DATA, auth=(ID, PW))
token_status = get_access_token.status_code
#print("token status:", token_status)
token_data = json.loads(get_access_token.text)["result"]['access_token']
#print(token_data)
#=====
UPC = 602527773728

HEADERS = {
    "osType" : "ANDROID",
    "osVersion" : "10.2.1",
    "appVersion" : "1.0.0",
    "Authorization" : "bearer " + token_data    # 인증 스킴 적용
}

video_play_check = requests.get(URL_SET.format(upc=UPC), headers=HEADERS)
print("content status:", video_play_check.status_code)