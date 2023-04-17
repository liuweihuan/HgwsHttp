#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 21:43
# @Author  : liuliuliu
# @Site    : 
# @File    : test_auth.py
# @Software: PyCharm
import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    r = requests.get("https://httpbin.testing-studio.com/basic-auth/banner/123", auth=HTTPBasicAuth("banner", "123"))
    print(r.text)
