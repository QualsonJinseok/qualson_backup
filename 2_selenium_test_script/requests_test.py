import requests

def test_1():
    try:
        a = requests.post('http://127.0.0.1:8081/200')
        b = "test"
        print("status code:", a.status_code)
        return a.status_code, b
    except Exception as e:
        print(e)

print(test_1())
print(test_1()[1])


d = test_1()
print("d:", d)
print(type(d))
