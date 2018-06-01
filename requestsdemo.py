#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: 'Paul.Wang'
# @Time : 2018/5/30 17:37


"""
爬取腾讯视频最近的所有电视剧名称与描述
"""
import requests
from bs4 import BeautifulSoup


# 状态码
# print(response.status_code)
#
# # 响应 URL
# print(response.url)
#
# # 响应短语
# print(response.reason)
#
# 响应内容
# print(response.content)

response = requests.get(url='https://v.qq.com/tv/')    # 最基本的GET请求
soup = BeautifulSoup(response.content,"html5lib")
div = soup.find("div",id = "tv_hot_show")
class_ = div.find("div",class_="mod_figures mod_figure_v")
# title = class_.find("strong").find("a").string
# print(class_)
# print(soup)
# for a in class_.find_all('a'):
#     print(a.string)
# print(title)
title = []
description = []
for c in class_.find_all("strong"):
    title.append(c.find("a").string)

for desc in class_.find_all("div",class_="figure_desc"):
    description.append(desc.string)

tvs = dict(zip(title,description))
for k,v in tvs.items():
    print("%s : %s" % (k,v))
