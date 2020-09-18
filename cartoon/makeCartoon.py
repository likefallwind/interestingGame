# encoding:utf-8

import requests
import base64

'''
人像动漫化
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
# 二进制方式打开图片文件
f = open('1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())