#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 00:49
# @Author  : liuliuliu
# @Site    : 
# @File    : test_cookie.py
# @Software: PyCharm
import requests


def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {"Cookie": "hogwarts=school"}
    r = requests.get(url=url, headers=header)
    print(r.request.headers)


def test_demo01():
    url = "https://httpbin.testing-studio.com/cookies"
    cookie_data = {
        "hogwarts": "school",
        "cookies2": "111"
    }
    r = requests.get(url=url, cookies=cookie_data)
    print(r.request.headers)
