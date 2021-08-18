import requests
import json
import cloudscraper
import threading
import os
import time

fileDir = os.path.dirname(os.path.realpath('__file__'))
scraper = cloudscraper.create_scraper()

popedNumber = 0

ogrecaptcha = '09AGTLn28SxrDOwHEP4HuBLmVzswWHA-JWeGXIk9F_c3SxxDCdJ8-lgMTNoVv5ZXu3UTi0QeNF1sEci3xDAsBPm1Y'
#            '09AGTLn2-Y4RrZGDoYb-3A_tAZXEl6Ai6VCeKHVy6ett1kXjx9vp8icr8yQvuGhd7K1ROKmXO_jIGlCQizuYReQi0'



def getToken(grecaptcha):
    cb = 'wuwde4gsjgfk'
    k = '6Ledv1IaAAAAAKFJSR7VKPE8e-4kht4ZmLzencES'

    url = 'https://recaptcha.net/recaptcha/api2/reload'

    headers = {
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'content-type': 'application/x-protobuffer',
    'accept': '*/*',
    'origin': 'https://recaptcha.net',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://recaptcha.net/recaptcha/api2/anchor?ar=2&k='+k+'&co=aHR0cHM6Ly9wb3BjYXQuY2xpY2s6NDQz&hl=zh-TW&v=tFhBvPrftr7Y91fo1S1ASkA6&size=invisible&cb='+cb,
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_GRECAPTCHA='+grecaptcha,
    }

    params = {
        'k' : k
    }

    f = open('./text.dat','rb')
    data = f.read()
    try:

        res = requests.post(url,data,params=params,headers=headers)
    except:
        print('captcha ERROR')
        return 'HFcXptYgNKMD5uXn5YX1BJXhQZCQwNBR0QEwZlJWVgLicsfRElD0MtLSt8SyFEe2tvZQE-FQlvFQkUX0RKUz4eCWsNe1lld1d1aj5UfUI5d3hnV0J-D1ksNXkBIngJAglmfAhyEE93T0dxRgBCAxt-fWwSQS4TbFEmIA0bcnI'
    split = res.text.replace('"', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').split()

    ogrecaptcha = split[16]
    return split[3]

def pop(captcha_token, pop_count='800', timeout = 25):


    # print(captcha_token)
    url = 'https://stats.popcat.click/pop?pop_count='+pop_count+'&captcha_token='+captcha_token#+'&token='+token

    try:


        res = scraper.get(url)

        code = res.status_code

        res = res.text
        # print(code)
        if  "!DOCTYPE html" in res:
            #print('Error============================================')
            return -1
        else:
        
            res = json.loads(res)
            print(res['Location']['Name'], end='\t')
            if  "Location" in res:
                global popedNumber
                popedNumber += int(pop_count)

            return code
    except  Exception as e:
        print('Error:')
        print(e)

        return code

    #time.sleep(30.1)
#
# from urllib.request import urlopen
# import re
# def getPublicIp():
#     data = str(urlopen('http://checkip.dyndns.com/').read())
#     # data = '<html><head><title>Current IP Check</title></head><body>Current IP Address: 65.96.168.198</body></html>\r\n'
#
#     return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
#
# ip = getPublicIp()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

import datetime
import csv
from pathlib import Path


while True:

    captcha_token = getToken(ogrecaptcha)
    for i in range(100):

        maximum_tries = 40
        for i in range(maximum_tries):
            status = pop(captcha_token = captcha_token)
            if status != -1:

                print(ip, status)
                status = '201'

                Path("./logs").mkdir(parents=True, exist_ok=True)
                with open('./logs/output.csv', 'a', newline='') as csvfile:
                  # 建立 CSV 檔寫入器
                  writer = csv.writer(csvfile)

                  current_time = datetime.datetime.now()
                  datetime_format = current_time.strftime("%Y/%m/%d %H:%M:%S")

                  # 寫入一列資料
                  writer.writerow([datetime_format, ip, status])


                break

            time.sleep(0.5)
            scraper = cloudscraper.create_scraper()
            captcha_token = getToken(ogrecaptcha)


            if i == 99:
                print('Unable to connect : reach maximum_tries')
        time.sleep(30)
