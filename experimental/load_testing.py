import requests
import threading


def req():
    for i in range(20):
        pload = {"input": "def foo():\n\tprint()", "in_lang": "py", "out_lang": "js"}
        url = 'https://cjsback.herokuapp.com/'
        r = requests.post(url, data = pload)
        print(r.json())


for i in range(20):
        t = threading.Thread(target=req)
        t.start()