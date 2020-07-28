import requests
import threading
import datetime


def req():
    for i in range(40):
        pload = {"input": "def foo():\n\tprint()", "in_lang": "py", "out_lang": "js"}
        url = 'https://cjsback.herokuapp.com/'
        r = requests.post(url, data = pload)
        print(r.json())

threads = []
begin_time = 0
for i in range(10):
    if i == 1:
        begin_time = datetime.datetime.now()
    t = threading.Thread(target=req)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print(datetime.datetime.now()-begin_time)