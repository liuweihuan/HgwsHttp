#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 21:36
# @Author  : liuliuliu
# @Site    : 
# @File    : base_api.py
# @Software: PyCharm
import requests


class BaseApi:
    def send(self, **data):
        print(data)
        return requests.request(**data).json()
