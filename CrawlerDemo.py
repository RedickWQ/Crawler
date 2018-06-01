#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: 'Paul.Wang'
# @Time : 2018/6/1 10:26





import requests
from bs4 import BeautifulSoup

r = requests.get(url='https://v.qq.com/')    # 最基本的GET请求
print(r.status_code)    # 获取返回状态
r.encoding = 'utf-8' #没有的话，中文会显示乱码
print(r.text)

soup = BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
