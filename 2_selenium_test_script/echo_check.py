import requests
import time
from slacker import Slacker
from variable_info import *
#========================================
localhost = 'http://127.0.0.1:8082/echo'
#localhost = ''

slack = Slacker(token)
slack_test_channel = 'GR5MLV2CE'
slack_real_channel = ''
#========================================
def echo_call():
    while True:
        try:
            echo_response = str(requests.get(localhost))
            print(type(echo_response), ":", echo_response)
            if echo_response == "<Response [200]>":
                print("server is alive")
            time.sleep(5)

        except Exception as e:
            print("seriver is dead")
            print(e)
            message = "<!channel>  *셀링페이지 모니터링 서버가 정상적이지 않으니 확인해주세요. "
            slack.chat.post_message(slack_test_channel, message)
            time.sleep(5)

if __name__ == "__main__":
    echo_call()