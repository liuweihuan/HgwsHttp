#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 00:06
# @Author  : liuliuliu
# @Site    : 
# @File    : tttt.py
# @Software: PyCharm
import gzip

import buff as buff
import requests


class Demo2:
    r = requests.get("https://httpbin.testing-studio.com/get")

    print(r.status_code)
    print(r.text)
    print(r.json())